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

## Usage

```
classifai [OPTIONS] CONTENT [CONTENT ...]
```

For more details, run `classifai --help`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Usage Examples

1. Multiple classification with Examples:
   ```
   classifai  'news.ycombinator.com' 'facebook.com' 'ai.meta.com' --classes 'signal' 'noise' 'neutral' --examples "github.com:signal" "dailymail.com:noise" "arxiv.org:signal" "instagram.com:noise" "pintrest.com:noise" "anthropic.ai:signal" "stackoverflow.com:signal" "twitter.com:noise --model openrouter/openai/gpt-4-0314
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

## Advanced scripts

### Acting on the classification
```bash
class-tweet() {
    local tweet="$1"
    local threshold=0.6
    local class="MACHINE-LEARNING"

    result=$(classifai "$tweet" --classes 'PROGRAMMING' 'MACHINE-LEARNING' -m gpt-4o-mini | jq -r '.[0] | select(.classification == "'"$class"'" and .score > '"$threshold"') | .classification')

    if [ -n "$result" ]; then
        echo "Tweet classified as $class with high confidence. Executing demo..."
        echo "Demo: This is a highly relevant tweet about $class"
    else
        echo "Tweet does not meet classification criteria."
    fi
}
```


