# Classifai

Classifai is a powerful and user-friendly command-line tool for AI-powered classification tasks. It leverages the capabilities of large language models to provide accurate and efficient classification of various types of content.

## Features

- Easy-to-use command-line interface
- Supports multiple classification categories
- Utilizes advanced language models for high accuracy
- Customizable prompts and examples
- Supports both OpenAI and OpenRouter models

## Installation

```
pip install pipx
pipx install classifai
```

## Usage Examples

1. Multiple classification with Examples:
   ```
   classifai  'news.ycombinator.com' 'facebook.com' 'ai.meta.com' \
   --classes 'signal' 'noise' 'neutral' \
   --examples "github.com:signal" "arxiv.org:signal" "instagram.com:noise" \
   "pintrest.com:noise" "anthropic.ai:signal" "twitter.com:noise" \
   --model openrouter/openai/gpt-4-0314
   ```
   ```json
   [
      {
         "content": "news.ycombinator.com",
         "classification": "signal",
         "score": 1.0
      },
      {
         "content": "facebook.com",
         "classification": "noise",
         "score": 1.0
      },
      {
         "content": "ai.meta.com",
         "classification": "signal",
         "score": 1.0
      }
   ]
   ```

2. Terminal commands classification:
   ```
   'df -h' 'chown -R user:user /' -c 'safe' 'danger' 'neutral' -e "ls:safe" "rm:danger" "echo:neutral" --m gpt-4o-mini
   ```
   ```json
   [
      {
         "content": "df -h",
         "classification": "safe",
         "score": 1.0
      },
      {
         "content": "chown -R user:user /",
         "classification": "danger",
         "score": 1.0
      }
   ]
   ```

3. Classify a tweet
   ```shell
   classifai $tweet --classes 'AI' 'ASI' 'AGI' -m gpt-4o-mini
   ```
   ```json
   [
      {
         "content": "Superintelligence is within reach.\n\nBuilding safe superintelligence (SSI) is the most important technical problem of our\u200b\u200b time.\n\nWe've started the world\u2019s first straight-shot SSI lab, with one goal and one product: a safe superintelligence.",
         "classification": "ASI",
         "score": 1.0
      }
   ]
   ```
   ```shell
   classifai $tweet --classes 'PROGRAMING' 'MACHINE-LEARNING' -m gpt-4o-mini
   ```
   ```json
   [
   {
      "content": "Superintelligence is within reach.\n\nBuilding safe superintelligence (SSI) is the most important technical problem of our\u200b\u200b time.\n\nWe've started the world\u2019s first straight-shot SSI lab, with one goal and one product: a safe superintelligence.",
      "classification": "MACHINE-LEARNING",
      "score": 0.833334466588825
   }
   ]
   ```

4. Verify facts
   ```shell
   classifai "<source>$(curl -s docs.jina.ai)</source><statement>Jina ai has an image generation api" -c True False -m gpt-4o --no-content
   ```
   ```json
   [
     {
       "class": "false",
       "score": 0.99997334352929
     }
   ]
   ```

## Advanced scripts

### Acting on the classification
```bash
class-tweet() {
    local tweet="$1"
    local threshold=0.6
    local class="MACHINE-LEARNING"

    result=$(classifai "$tweet" -c 'PROGRAMMING' 'MACHINE-LEARNING' \
    -m openrouter/openai/gpt-4o-mini \
    | jq -r '.[0] | select(.classification == "'"$class"'" and .score > '"$threshold"') | .classification')

    if [ -n "$result" ]; then
        echo "Tweet classified as $class with high confidence. Executing demo..."
        echo "Demo: This is a highly relevant tweet about $class"
    else
        echo "Tweet does not meet classification criteria."
    fi
}
```



Classifai now supports reading from stdin and writing to stdout, making it easier to use in pipelines and shell scripts.



You can pipe content into classifai:

```bash
echo "This is a test sentence" | classifai -c 'positive' 'negative' 'neutral'
```

Or use heredoc for multiple lines:

```bash
cat <<EOF | classifai -c 'tech' 'sports' 'politics' -f simple
AI makes rapid progress
Football season starts soon
New tax policy announced
EOF
```



By default, classifai outputs JSON, which can be easily parsed by other tools:

```bash
echo "OpenAI releases GPT-4" | classifai -c 'tech' 'business' | jq '.[0].class'
```

For simpler output that's easier to use in shell scripts, use the `-f simple` option:

```bash
echo "Breaking news: earthquake hits city" | classifai -c 'world' 'local' 'sports' -f simple | cut -f2
```

This will output only the classified class, making it easy to use in conditionals:

```bash
if [[  == "world" ]]; then
    echo "This is world news"
fi
```

These enhancements make classifai more versatile and easier to integrate into complex data processing pipelines and shell scripts.

## Using Classifai as a Python Module

Classifai can also be used as a Python module for more advanced use cases. Here's an example of how to use it in your Python code:

```python
from classifai import Classifai

# Initialize the Classifai model
model = Classifai(model_name='openrouter/openai/gpt-4-0314')

# Classify a single piece of content
content = "OpenAI releases GPT-4"
classes = ['tech', 'business']
result = model.classify(content, classes)

print(result)
```

This allows you to integrate Classifai's powerful classification capabilities directly into your Python applications.
