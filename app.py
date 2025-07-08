import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="centered",
)

st.title("📩 SMS Spam Detector")
st.markdown(
    """
    This app predicts whether an SMS message is **Spam** or **Not Spam** using a machine learning model.
    """
)

# Single Message Prediction
st.markdown("## Single Message Prediction")

message = st.text_area(
    "Enter your SMS text here:",
    height=150,
    placeholder="e.g. Congratulations! You won a $1000 gift card. Click here..."
)

if st.button("Predict Spam or Not"):
    if message.strip() == "":
        st.warning("Please enter a message to classify.")
    else:
        msg_vec = vectorizer.transform([message])
        prediction = model.predict(msg_vec)[0]
        proba = model.predict_proba(msg_vec)[0]

        label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
        confidence = proba[prediction]

        st.success(f"**Prediction:** {label}")
        st.write(f"Confidence: {confidence:.2%}")
        st.progress(int(confidence * 100))

# Batch Prediction from CSV
st.markdown("## Batch Prediction from CSV")

uploaded_file = st.file_uploader("Upload a CSV file containing SMS messages.", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if 'message' not in df.columns:
        st.error("CSV must contain a column named 'message'.")
    else:
        st.write(f"✅ Uploaded {df.shape[0]} messages.")
        X_batch = vectorizer.transform(df['message'])
        predictions = model.predict(X_batch)
        labels = ["Spam" if p == 1 else "Not Spam" for p in predictions]
        df['Prediction'] = labels

        st.dataframe(df.head(10))

        # Optional: download result
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download predictions as CSV",
            csv,
            "spam_predictions.csv",
            "text/csv",
            key='download-csv'
        )
