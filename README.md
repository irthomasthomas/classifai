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
   [
   {
      "content": "Superintelligence is within reach.\n\nBuilding safe superintelligence (SSI) is the most important technical problem of our\u200b\u200b time.\n\nWe've started the world\u2019s first straight-shot SSI lab, with one goal and one product: a safe superintelligence.",
      "classification": "MACHINE-LEARNING",
      "score": 0.833334466588825
   }
   ]
   ```

## Example Use-Cases

### 1. Sentiment Analysis
You can use Classifai to classify text into positive, negative, or neutral sentiments.


## Advanced Usage Example: Tweet Classifier

Here's an example of how to use `classifai` in a bash function to classify tweets and perform actions based on the classification:

```bash
classify_tweet() {
    tweet="$1"
    result=
    
    if [ "$result" == "ai" ]; then
        echo "🤖 This tweet is about AI: $tweet"
    else
        echo "🧑 This tweet is not about AI: $tweet"
    fi
}

# Usage examples:
classify_tweet "ChatGPT is revolutionizing natural language processing."
classify_tweet "I love watching sunsets at the beach."
```

This function uses our `classifai.py` script to determine if a tweet is about AI or not. It then uses `jq` to parse the JSON output and echo an appropriate message with an emoji.

Note: Make sure that `classifai.py` is in your current directory or provide the full path to the script.

You can add this function to your `.bashrc` or `.zshrc` file to use it in your terminal sessions, adjusting the path to `classifai.py` as needed.

