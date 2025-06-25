import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

# Load dataset
df = pd.read_csv("train.csv")

# Input and Output
x = df['text']  # Agar 'text' column nahi ho, toh 'title' ya 'content' check karo
y = df['label']  # 0 = Fake, 1 = Real

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
x_vect = vectorizer.fit_transform(x)

# Train model
model = PassiveAggressiveClassifier(max_iter=50)
model.fit(x_vect, y)

# Save model and vectorizer
joblib.dump(model, "fake_news_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model trained and saved successfully!")
