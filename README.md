# 📰 Fake News Detection Using Machine Learning

This project is an AI-based Fake News Detection system that classifies news articles as **Real** or **Fake** using Natural Language Processing and Machine Learning techniques.

---

## 📌 Overview

With the rise of misinformation, fake news detection has become a critical challenge. In this project, we:
- Collected real and fake news articles
- Combined and labeled them for ML training
- Built a machine learning model using TF-IDF and Passive Aggressive Classifier
- Deployed the model as a web app using Streamlit

---

## 🛠️ Tools & Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Passive Aggressive Classifier
- Joblib
- Streamlit
- Jupyter Notebook / VS Code

---

## 📂 Project Structure

```
📁 FakeNewsApp/
├── Fake.csv                    # Fake news dataset
├── True.csv                    # Real news dataset
├── train.csv                   # Combined + labeled dataset
├── prepare_dataset.py          # Data cleaning and merge script
├── train_model.py              # Model training script
├── fake_news_model.pkl         # Trained ML model
├── vectorizer.pkl              # Trained TF-IDF vectorizer
├── fake_news_app.py            # Streamlit web app
├── requirements.txt            # Python dependencies
├── Fake_News_Project_Report.pdf  # 2-page internship report
└── README.md
```

---

## 📥 Dataset Download

You can download the dataset from Kaggle:

👉 [**Click here to open dataset on Kaggle**](https://www.kaggle.com/datasets/vishalpancham/fake-news-detector-ai-project )

_The dataset includes `Fake.csv`, `True.csv`, and a combined `train combine.csv` file._

---

## 🚀 How to Run This Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

(If `requirements.txt` not available, manually install: `pandas`, `scikit-learn`, `joblib`, `streamlit`)

### 4. Train the Model

```bash
python train_model.py
```

### 5. Run the Streamlit App

```bash
streamlit run fake_news_app.py
```

---

## ✅ Conclusion

This project provides a foundation for building an AI-powered tool that detects fake news based on text content.  
Future improvements may include using advanced models like BERT, live news API integration, and multilingual support.

---

## 📄 License

This project is for educational use under Elevate Labs Internship.  
Dataset license: `CC BY-NC-SA 4.0`
