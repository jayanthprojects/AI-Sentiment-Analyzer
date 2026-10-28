from textblob import TextBlob
import streamlit as st

st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="🤖")

st.title("🤖 AI Sentiment Analyzer")
st.write("Analyze the sentiment of custom text or upload a review using TextBlob.")


# Analyze sentiment function
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


# UI Input
user_text = st.text_area("Enter your sentence or review:")

if st.button("Analyze Sentiment"):
    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        polarity, sentiment = analyze_sentiment(user_text)

        st.markdown("---")
        st.subheader("Results")
        st.metric(label="Sentiment", value=sentiment)
        st.write(f"**Polarity Score:** {round(polarity, 3)}")

        if sentiment == "Positive":
            st.success("This is a positive review! 😊")
        elif sentiment == "Negative":
            st.error("This is a negative review. ")
        else:
            st.info("This is a neutral review. 😐")
