#!/usr/bin/env python3

import sys
from openai import OpenAI
import math
import argparse
import os
from typing import List, Dict, Tuple, Optional
import json
import time
from os import getenv

def get_class_probability(
    content: str,
    classes: List[str],
    model: str,
    temperature: float,
    examples: Optional[List[Dict[str, str]]] = None,
    custom_prompt: Optional[str] = None
) -> Tuple[str, float]:
    """
    Get the class and probability for the given content using OpenAI API.

    Args:
        content (str): The content to classify.
        classes (List[str]): List of possible classes.
        model (str): The model to use for classification.
        temperature (float): The temperature for the API call.
        examples (Optional[List[Dict[str, str]]]): List of example classifications.
        custom_prompt (Optional[str]): Custom instructions prompt.

    Returns:
        Tuple[str, float]: The classified class and its probability.
    """
    if "openrouter" in model:
        model = f"{model.split('/')[1]}/{model.split('/')[-1]}"
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=getenv("OPENROUTER_API_KEY"),
        )
    else:
        client = OpenAI(api_key=getenv("OPENAI_API_KEY"))
        
    if custom_prompt:
        prompt = custom_prompt
    else:
        prompt = f"""
<INSTRUCTIONS>
Your task is to classify the given content into ONE of the provided categories. Respond with ONLY the category name. 

<CLASSES>
{', '.join(classes)}
</CLASSES>
... 

Content: {content}
Class: 
</INSTRUCTIONS>
"""

    if examples:
        prompt += "Examples:"
        for example in examples:
            prompt += f"""
    Content: {example['content']}
    Class: {example['class']}"""

    prompt += f"""</INSTRUCTIONS>
Input: {content}
Class:"""
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=10,
                logprobs=True,
                temperature=temperature
            )

            generated_text = response.choices[0].message.content.strip().lower()
            logprobs = response.choices[0].logprobs.content
            # Calculate probabilities for each class
            class_probs = {class_: 0.0 for class_ in classes}
            for token_info in logprobs:
                token = token_info.token.lower()
                token_prob = math.exp(token_info.logprob)
                for class_ in classes:
                    if token in class_.lower():
                        class_probs[class_] += token_prob

            # Normalize probabilities
            total_prob = sum(class_probs.values())
            if total_prob > 0:
                class_probs = {k: v / total_prob for k, v in class_probs.items()}

            # Find the class with the highest probability
            best_class = generated_text
            best_prob = math.exp(sum(token_info.logprob for token_info in logprobs))

            # If no class was matched, fall back to the generated text
            if best_prob == 0:
                return generated_text, 0.0

            return best_class, best_prob

        except Exception as e:
            if attempt < max_retries - 1:
                print(f"An error occurred: {e}. Retrying...")
                time.sleep(2 ** attempt)
            else:
                print(f"Max retries reached. An error occurred: {e}")
                return "Error", 0

def classify_content(
    content: List[str],
    classes: List[str],
    model: str,
    temperature: float,
    examples: Optional[List[Dict[str, str]]] = None,
    custom_prompt: Optional[str] = None,
    no_content: bool = False
) -> List[Dict[str, Optional[str]]]:
    results = []
    for item in content:
        winner, probability = get_class_probability(
            item, classes, model, temperature, examples, custom_prompt
        )
        result = {"class": winner, "score": probability}
        if not no_content:
            result["content"] = item
        results.append(result)
    return results

def main():
    parser = argparse.ArgumentParser(description="Classify content using OpenAI API")
    parser.add_argument("content", nargs='*', help="The content(s) to classify")
    parser.add_argument("-c", "--classes", nargs='+', required=True, help="Class options for classification")
    parser.add_argument("-m", "--model", default="gpt-3.5-turbo", help="OpenAI model to use")
    parser.add_argument("-t", "--temperature", type=float, default=0, help="Temperature for API call")
    parser.add_argument("-e", "--examples", nargs='+', help="Examples in the format 'content:class'")
    parser.add_argument("-p", "--prompt", help="Custom prompt template")
    parser.add_argument("--no-content", action="store_true", help="Exclude content from the output")
    args = parser.parse_args()

    if len(args.classes) < 2:
        raise ValueError("At least two classes must be provided")
    
    if args.temperature < 0 or args.temperature > 1:
        raise ValueError("Temperature must be between 0 and 1")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not provided. Use --api-key or set OPENAI_API_KEY environment variable.")

    examples = None
    if args.examples:
        examples = []
        for example in args.examples:
            content, class_ = example.split(':')
            examples.append({"content": content.strip(), "class": class_.strip()})
    
    if not args.content:
        args.content = [line.strip() for line in sys.stdin]
    
    results = classify_content(
        args.content, args.classes, args.model, args.temperature, examples, args.prompt, args.no_content
    )
    
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
