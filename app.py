import streamlit as st

# ---------------- Page Configuration ---------------- #
st.set_page_config(
    page_title="Amazon Review Sentiment Analysis",
    page_icon="🛍️",
    layout="wide"
)
st.markdown("""
<style>

.main-title {
    font-size: 32px;
    font-weight: 800;
    color: #2E86DE;
    text-align: center;
    margin-bottom: 0px;
}

.sub-title {
    font-size: 18px;
    color: #555555;
    text-align: center;
    margin-top: -10px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)
# ---------------- Header ---------------- #
st.markdown(
    '<div class="main-title">🛍️ Amazon Review Sentiment Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">AI-powered Sentiment Classification using Natural Language Processing</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- About ---------------- #
st.header("📖 About the Project")

st.write("""
This application analyzes Amazon customer reviews and predicts whether a review
expresses **Positive** or **Negative** sentiment.

The review text is cleaned using Natural Language Processing (NLP), transformed
into numerical features using **TF-IDF Vectorization**, and classified using a
trained **Logistic Regression** model.
""")

st.markdown("---")

# ---------------- Project Highlights ---------------- #
st.header("📌 Project Highlights")

col1, col2 = st.columns(2)

with col1:
    st.info("""
**📂 Dataset**

- Amazon Alexa Reviews
- 3,149 customer reviews
- Binary Sentiment Classification
""")

with col2:
    st.success("""
**🤖 Best Model**

- Logistic Regression
- TF-IDF Vectorization
- Accuracy: **92.22%**
""")

st.markdown("---")

# ---------------- Features ---------------- #
st.header("✨ Dashboard Features")

st.markdown("""
- 📊 View the sentiment distribution of customer reviews.
- ☁️ Explore Word Clouds for positive and negative reviews.
- 😊 Predict the sentiment of any custom Amazon review.
- 📈 View the model's confidence score for each prediction.
""")

st.markdown("---")

st.success("👈 Use the sidebar to explore the Data Overview and Sentiment Predictor pages.")