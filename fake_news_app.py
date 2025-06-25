import streamlit as st
import joblib

# Load trained model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# App Title
st.title("📰 Fake News Detector")

# User Input
text = st.text_area("Paste the news article content below:")

# Predict Button
if st.button("Predict"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        # Transform and Predict
        vector = vectorizer.transform([text])
        result = model.predict(vector)[0]
        
        if result == 1:
            st.success("✅ This is Real News")
        else:
            st.error("❌ This is Fake News")
