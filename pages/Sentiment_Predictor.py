import streamlit as st
import joblib
import re
import nltk

from nltk.corpus import stopwords

# Download stopwords if not already available
nltk.download("stopwords")

# -------------------------------
# Load Model and Vectorizer
# -------------------------------

model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

stop_words = set(stopwords.words("english"))

# -------------------------------
# Text Cleaning Function
# -------------------------------

def clean_text(text):
    text = text.lower()

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = text.split()

    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# -------------------------------
# Page Title
# -------------------------------

st.title("😊 Sentiment Predictor")

st.write(
    """
Enter an Amazon customer review below and click **Predict Sentiment**.
The model will classify the review as **Positive** or **Negative** and display its confidence score.
"""
)

st.markdown("---")

# -------------------------------
# User Input
# -------------------------------

review = st.text_area(
    "✍️ Enter your review",
    height=180,
    placeholder="Example: This product exceeded my expectations. The sound quality is excellent!"
)

# -------------------------------
# Prediction
# -------------------------------

if st.button("🔍 Predict Sentiment"):

    if review.strip() == "":

        st.warning("Please enter a review before making a prediction.")

    else:

        cleaned_review = clean_text(review)

        vectorized_review = vectorizer.transform([cleaned_review])

        prediction = model.predict(vectorized_review)[0]

        confidence = model.predict_proba(vectorized_review).max() * 100

        st.markdown("---")

        st.subheader("Prediction Result")

        if prediction == 1:

            st.success("🟢 Positive Review")

            st.write(
                "The model predicts that this review expresses **positive customer sentiment**."
            )

        else:

            st.error("🔴 Negative Review")

            st.write(
                "The model predicts that this review expresses **negative customer sentiment**."
            )

        st.metric(
            label="Confidence Score",
            value=f"{confidence:.2f}%"
        )
        st.progress(confidence / 100)