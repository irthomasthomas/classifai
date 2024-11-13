#!/bin/bash

CLASSIFAI_PATH="/home/ShellLM/Projects/ASI/multimodel/sonnet-3.5/classifai/classifai.py"

# Helper function to parse JSON output
parse_json_output() {
    local json_output="$1"
    local class=$(echo "$json_output" | jq -r '.[0].class')
    local score=$(echo "$json_output" | jq -r '.[0].score')
    echo "$class:$score"
}

# 1. Sentiment Analysis
sentiment_analysis() {
    local text="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$text" -c positive neutral negative -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# 2. Language Detection
detect_language() {
    local text="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$text" -c english spanish french german chinese japanese -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# 3. Content Moderation
moderate_content() {
    local text="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$text" -c safe sensitive explicit -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# 4. Email Classification
classify_email() {
    local email_content="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$email_content" -c personal work spam promotion -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# 5. Customer Feedback Categorization
categorize_feedback() {
    local feedback="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$feedback" -c bug feature_request compliment complaint question -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# 6. News Article Topic Classification
classify_news_topic() {
    local article="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$article" -c politics technology sports entertainment science business -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# 7. Product Review Sentiment Analysis
analyze_product_review() {
    local review="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$review" -c positive neutral negative -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# 8. Social Media Post Categorization
categorize_social_post() {
    local post="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$post" -c personal promotional informative entertainment controversial -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# 9. Document Type Classification
classify_document_type() {
    local document="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$document" -c resume report contract invoice letter -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# 10. Movie Genre Prediction
predict_movie_genre() {
    local movie_description="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$movie_description" -c action comedy drama horror sci-fi romance -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# 11. Music Mood Classification
classify_music_mood() {
    local lyrics="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$lyrics" -c happy sad energetic relaxing angry romantic -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# 12. Food Cuisine Categorization
categorize_food_cuisine() {
    local recipe="$1"
    local model="${2:-gpt-3.5-turbo}"
    local temperature="${3:-0}"
    local result=$(python3 "$CLASSIFAI_PATH" "$recipe" -c italian mexican chinese indian french japanese -m "$model" -t "$temperature")
    parse_json_output "$result"
}

# Usage examples
# sentiment_analysis "I love this product! It's amazing!"
# detect_language "Bonjour, comment allez-vous?"
# moderate_content "This is a family-friendly message."
# classify_email "Dear Sir, I am writing to inquire about your services."
# categorize_feedback "The app crashes every time I try to save my progress."
# classify_news_topic "Scientists discover a new planet in the habitable zone of a nearby star."
# analyze_product_review "This smartphone has excellent battery life and a great camera."
# categorize_social_post "Check out my new vacation photos! #summervibes"
# classify_document_type "Dear hiring manager, I am writing to apply for the position of software engineer."
# predict_movie_genre "In a world where robots have taken over, one man fights to save humanity."
# classify_music_mood "I'm walking on sunshine, whoa! And don't it feel good?"
# categorize_food_cuisine "Mix pasta with tomato sauce, basil, and Parmesan cheese."

# Usage Instructions and Examples

echo "AI Decision Functions - Usage Instructions and Examples"
echo "======================================================="
echo ""
echo "To use these functions, first source this script in your bash session or another script:"
echo "source ai_decision_functions.sh"
echo ""
echo "Then you can call the functions as follows:"
echo ""
echo "1. Sentiment Analysis:"
echo "   sentiment_analysis \"I love this product! It's amazing!\""
echo ""
echo "2. Language Detection:"
echo "   detect_language \"Bonjour, comment allez-vous?\""
echo ""
echo "3. Content Moderation:"
echo "   moderate_content \"This is a family-friendly message.\""
echo ""
echo "4. Email Classification:"
echo "   classify_email \"Dear Sir, I am writing to inquire about your services.\""
echo ""
echo "5. Customer Feedback Categorization:"
echo "   categorize_feedback \"The app crashes every time I try to save my progress.\""
echo ""
echo "6. News Article Topic Classification:"
echo "   classify_news_topic \"Scientists discover a new planet in the habitable zone of a nearby star.\""
echo ""
echo "7. Product Review Sentiment Analysis:"
echo "   analyze_product_review \"This smartphone has excellent battery life and a great camera.\""
echo ""
echo "8. Social Media Post Categorization:"
echo "   categorize_social_post \"Check out my new vacation photos! #summervibes\""
echo ""
echo "9. Document Type Classification:"
echo "   classify_document_type \"Dear hiring manager, I am writing to apply for the position of software engineer.\""
echo ""
echo "10. Movie Genre Prediction:"
echo "    predict_movie_genre \"In a world where robots have taken over, one man fights to save humanity.\""
echo ""
echo "11. Music Mood Classification:"
echo "    classify_music_mood \"I'm walking on sunshine, whoa! And don't it feel good?\""
echo ""
echo "12. Food Cuisine Categorization:"
echo "    categorize_food_cuisine \"Mix pasta with tomato sauce, basil, and Parmesan cheese.\""
echo ""
echo "Each function returns the result in the format: category:score"
echo ""
echo "You can also specify a different model or temperature:"
echo "sentiment_analysis \"This is great!\" \"gpt-4\" 0.7"
echo ""
echo "Note: These functions make API calls to OpenAI, which may incur costs and have associated latency."
echo "Always handle sensitive data with care when using these functions."
echo ""
echo "For more information, refer to the comments in the script or the original classifai.py documentation."
