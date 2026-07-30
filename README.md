# WEEK-5-TASK
Natural Language Processing & Sentiment Analysis Dashboard

## Project Overview

This project performs sentiment analysis on Amazon customer reviews using Natural Language Processing (NLP) and Machine Learning. Customer reviews are preprocessed, converted into numerical features using TF-IDF Vectorization, and classified as either **Positive** or **Negative**. The best-performing model is deployed through an interactive Streamlit dashboard that allows users to predict the sentiment of custom reviews in real time.

---

## Objectives

- Clean and preprocess raw customer review text.
- Generate Word Clouds for positive and negative reviews.
- Convert text into numerical features using TF-IDF.
- Train and compare multiple machine learning models.
- Evaluate model performance using classification metrics and confusion matrices.
- Deploy the best-performing model using Streamlit.

---

## Dataset

- **Dataset:** Amazon Product Reviews Dataset
- **Source:** Kaggle
- **Total Reviews:** 3,149
- **Classes:** Positive and Negative

---

## Project Structure

```text
WEEK-5-TASK/
│
├── app.py
├── assets/
├── data/
├── models/
├── notebooks/
├── pages/
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- TF-IDF Vectorizer
- Scikit-learn
- Logistic Regression
- Streamlit
- Matplotlib
- WordCloud
- Joblib

---

## Machine Learning Workflow

1. Load and inspect the dataset.
2. Clean and preprocess review text.
3. Generate positive and negative Word Clouds.
4. Convert text into numerical features using TF-IDF.
5. Split the dataset into training and testing sets.
6. Train Multinomial Naive Bayes and Logistic Regression models.
7. Evaluate models using classification metrics and confusion matrices.
8. Save the best-performing model and vectorizer.
9. Deploy the model using Streamlit.

---

## Results

| Model | Accuracy |
|--------|----------|
| Multinomial Naive Bayes | 92.06% |
| Logistic Regression | **92.22%** |

The Logistic Regression model was selected for deployment because it achieved the best overall performance and provided a better balance between precision and recall, particularly for the minority (negative) class.

---

## How to Run the Project

### Clone the repository

```bash
git clone https://github.com/hania-sajjad/WEEK-5-TASK
```

### Navigate to the project folder

```bash
cd WEEK-5-TASK
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## Future Improvements

- Train deep learning models such as LSTM or BERT for improved performance.
- Support multi-class sentiment classification.
- Deploy the application to the cloud.
- Expand the dataset with reviews from multiple product categories.

---

## Author

**Hania Sajjad**

ITSimplera Institute Internship – Week 5 Task