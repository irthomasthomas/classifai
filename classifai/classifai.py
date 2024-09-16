from openai import OpenAI
import math
import argparse
import os
from typing import List, Dict, Tuple, Optional
import json
import time
import sys
from os import getenv

def get_class_probability(
    content: str,
    classes: List[str],
    model: str,
    temperature: float,
    examples: Optional[List[Dict[str, str]]] = None,
    custom_prompt: Optional[str] = None
) -> Tuple[str, float]:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    prompt = custom_prompt or f"Classify the following content into one of these classes: {', '.join(classes)}. Content: {content}"
    
    if examples:
        prompt += "Examples:"
        for example in examples:
            prompt += f"Content: {example['content']} Class: {example['class']}"
    
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    
    classification = response.choices[0].message.content.strip()
    
    
    for class_ in classes:
        if class_.lower() in classification.lower():
            return class_, 1.0  
    
    return "Unknown", 0.0

def main():
    parser = argparse.ArgumentParser(description="Classify content using OpenAI API")
    parser.add_argument("content", nargs='*', help="The content(s) to classify")
    parser.add_argument("-c", "--classes", nargs='+', required=True, help="Class options for classification")
    parser.add_argument("-m", "--model", default="gpt-3.5-turbo", help="OpenAI model to use")
    parser.add_argument("-t", "--temperature", type=float, default=0, help="Temperature for API call")
    parser.add_argument("-e", "--examples", nargs='+', help="Examples in the format 'content:class'")
    parser.add_argument("-p", "--prompt", help="Custom prompt template")
    parser.add_argument("-f", "--format", choices=['json', 'simple'], default='json', help="Output format")
    args = parser.parse_args()

    if len(args.classes) < 2:
        sys.stderr.write("Error: At least two classes must be provided")
        sys.exit(1)
    
    if args.temperature < 0 or args.temperature > 1:
        sys.stderr.write("Error: Temperature must be between 0 and 1")
        sys.exit(1)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.stderr.write("Error: OpenAI API key not provided. Use --api-key or set OPENAI_API_KEY environment variable.")
        sys.exit(1)

    examples = None
    if args.examples:
        examples = []
        for example in args.examples:
            content, class_ = example.split(':')
            examples.append({"content": content.strip(), "class": class_.strip()})

    if not args.content:
        args.content = [line.strip() for line in sys.stdin]

    results = []
    for content in args.content:
        winner, probability = get_class_probability(
            content, args.classes, args.model, args.temperature, examples, args.prompt
        )
        results.append({"content": content, "class": winner, "score": probability})
    
    if args.format == 'json':
        json.dump(results, sys.stdout, indent=2)
    else:  
        for result in results:
            print(f"{result['content']}	{result['class']}	{result['score']}")

if __name__ == "__main__":
    main()
