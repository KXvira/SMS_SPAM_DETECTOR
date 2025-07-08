# 📩 SMS Spam Detection App

Welcome to the **SMS Spam Detection App**, a simple web tool that uses machine learning to detect whether SMS messages are **Spam** or **Not Spam**.

This app is built with **Streamlit** and hosted on Hugging Face Spaces. 🚀

---

## 💡 How It Works

✅ Enter a single SMS message in the text box to classify it as Spam or Not Spam.

✅ Or upload a **CSV file** with multiple SMS messages for batch prediction.

- The app will add a `Prediction` column to your uploaded file.
- You can download the results as a CSV.

---

## ⚙️ How It Was Built

- **Dataset:** [UCI SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
- **Model:** Logistic Regression trained on TF-IDF features
- **Libraries:**  
  - scikit-learn
  - pandas
  - Streamlit
  - joblib

---

## 📂 CSV Upload Format

Your CSV file should have a single column named:

```

message

````

Example CSV:

| message                          |
|----------------------------------|
| Hey, are we still meeting today? |
| Congratulations! You've won a prize. |

---

## 🚀 Running Locally

If you'd like to run this app on your machine:

1. Clone the repository:

```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/sms-spam-detector
   cd sms-spam-detector
````

2. Install requirements:

```bash
   pip install -r requirements.txt
 ```

3. Run the app:

```bash
   streamlit run app.py
 ```

---

## 🔗 Try it Live!

👉 **[Launch the app here!](https://YOUR_USERNAME-sms-spam-detector.hf.space)**

---

## 👨‍💻 Author

This mini-project was built by Kevin and team as part of an AI mini-project exercise.

---

```

---

# ✅ How to Use This README

✅ Save the text above in your repo as:

```

README.md

```

✅ Replace this link:

```

[https://YOUR\_USERNAME-sms-spam-detector.hf.space](https://YOUR_USERNAME-sms-spam-detector.hf.space)

```

…with your actual Hugging Face Spaces URL once deployed!

---

Let me know if you’d like:
- A shorter README
- More technical details
- A specific license badge or image

Let’s get this project shipped! 🚀
```
