```python
from textblob import TextBlob
import csv
import json
import os

CSV_FILE = "reviews.csv"
JSON_FILE = "sentiment_results.json"


# Analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.10:
        sentiment = "Positive"
    elif polarity < -0.10:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return polarity, sentiment


# Load reviews from CSV
def load_reviews():
    if not os.path.exists(CSV_FILE):
        print("reviews.csv file not found.")
        return []

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


# Save results to JSON
def save_results(results):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print(f"\nResults saved to {JSON_FILE}")


# Analyze CSV reviews
def analyze_csv_reviews():
    reviews = load_reviews()

    if not reviews:
        return

    results = []

    print("\n" + "=" * 70)
    print("             AI SENTIMENT ANALYZER")
    print("=" * 70)

    for review in reviews:

        polarity, sentiment = analyze_sentiment(
            review["review"]
        )

        result = {
            "id": review["id"],
            "review": review["review"],
            "polarity": round(polarity, 3),
            "sentiment": sentiment
        }

        results.append(result)

        print("\nID:", review["id"])
        print("Review:", review["review"])
        print("Polarity:", round(polarity, 3))
        print("Sentiment:", sentiment)

    # Summary
    positive = 0
    negative = 0
    neutral = 0

    for result in results:
        if result["sentiment"] == "Positive":
            positive += 1
        elif result["sentiment"] == "Negative":
            negative += 1
        else:
            neutral += 1

    print("\n" + "-" * 40)
    print("SENTIMENT SUMMARY")
    print("-" * 40)
    print("Positive:", positive)
    print("Negative:", negative)
    print("Neutral :", neutral)

    save_results(results)


# Analyze user-entered text
def analyze_custom_text():

    text = input("\nEnter your sentence/review: ")

    if text.strip() == "":
        print("Please enter some text.")
        return

    polarity, sentiment = analyze_sentiment(text)

    print("\n" + "-" * 40)
    print("SENTIMENT RESULT")
    print("-" * 40)

    print("Text:", text)
    print("Polarity:", round(polarity, 3))
    print("Sentiment:", sentiment)


# Main menu
def main():

    while True:

        print("\n======================================")
        print("        AI SENTIMENT ANALYZER")
        print("======================================")

        print("1. Analyze CSV Reviews")
        print("2. Analyze Custom Text")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            analyze_csv_reviews()

        elif choice == "2":
            analyze_custom_text()

        elif choice == "3":
            print("\nThank you for using AI Sentiment Analyzer!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


# Start program
if __name__ == "__main__":
    main()
```

### Install the required library

Open Command Prompt/Terminal inside the project folder and run:

```bash
pip install textblob
```

### Run the project

```bash
python sentiment_analyzer.py
```  
