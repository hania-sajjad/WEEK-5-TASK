import streamlit as st

st.title("🗂️ Dataset Overview")

st.write(
    """
This page provides an overview of the Amazon Reviews dataset through
visualizations generated during the exploratory data analysis phase.
"""
)

st.markdown("---")

st.header("📌 Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Reviews",
        value="3,149"
    )

with col2:
    st.metric(
        label="Positive Reviews",
        value="91.87%"
    )

with col3:
    st.metric(
        label="Negative Reviews",
        value="8.13%"
    )

with col4:
    st.metric(
        label="Best Model",
        value="Logistic Regression"
    )

st.markdown("---")

# -------------------------------
# Sentiment Distribution
# -------------------------------

st.header("📈 Sentiment Distribution")

st.write(
    """
The chart below shows the distribution of positive and negative reviews
in the dataset.
"""
)

st.image(
    "./assets/class_distribution.png",
    use_container_width=True
)

st.info(
    "The dataset is imbalanced, with significantly more positive reviews than negative reviews."
)

st.markdown("---")

# -------------------------------
# Word Clouds
# -------------------------------

st.header("☁️ Word Clouds")

st.write(
    """
The Word Clouds below display the most frequently occurring words in
positive and negative customer reviews after text preprocessing.
"""
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("😊 Positive Reviews")
    st.image(
        "./assets/positive_wordcloud.png",
        use_container_width=True
    )

with col2:
    st.subheader("😞 Negative Reviews")
    st.image(
        "./assets/negative_wordcloud.png",
        use_container_width=True
    )

st.markdown("---")

# -------------------------------
# Key Insights
# -------------------------------

st.header("🔍 Key Insights")

st.header("💡 Key Insights")

st.markdown("""
- 📊 The dataset contains **3,149** Amazon customer reviews.

- 😊 Around **92%** of the reviews are positive, while only **8%** are negative.

- ☁️ Positive and negative Word Clouds highlight the most frequent words used in customer feedback.

- ⚖️ Because the dataset is imbalanced, **balanced class weights** were used while training the Logistic Regression model.

- 🤖 Logistic Regression achieved the best overall performance and was selected for deployment.
""")