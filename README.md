
# 🔮 AI-Based Astrology Prediction System using RNN
<img width="1280" height="780" alt="Screenshot 2026-03-30 114621" src="https://github.com/user-attachments/assets/68ccc57e-cf8f-4db9-bdda-2d1ca3710181" />
<img width="1425" height="848" alt="Screenshot 2026-03-30 114643" src="https://github.com/user-attachments/assets/e6e1bb0d-6adc-423e-902c-58fd5e838a48" />
<img width="1478" height="869" alt="Screenshot 2026-03-30 114656" src="https://github.com/user-attachments/assets/8e91b2c3-221a-4ab3-90b4-48bbfe6c5f4d" />


An advanced AI-powered web application that predicts probable life events such as **marriage, career growth, and financial stability** using **Recurrent Neural Networks (RNN)** and astrological data.

---

## 🚀 Project Overview

This project combines **Astrology + Deep Learning (RNN/LSTM) + Streamlit Dashboard** to analyze patterns from birth details and generate **probabilistic future insights**.

⚠️ Note: This system provides **AI-based predictions based on patterns**, not guaranteed or deterministic future outcomes.

---

## 🎯 Features

* 📅 Input birth details:

  * Date of Birth
  * Time of Birth
  * Place of Birth

* 🧠 AI Predictions:

  * Marriage Age Prediction
  * Career Success Probability
  * Financial Stability Score

* 📊 Interactive Dashboard (Streamlit)

* 📈 Visualization of prediction results

* 🌍 Location-based input (Latitude & Longitude)

* ⚡ Fast and user-friendly UI

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Machine Learning:** TensorFlow / Keras (RNN, LSTM)
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib / Plotly
* **APIs (Optional):** Geopy / Astrology APIs

---

## 📂 Project Structure

```
AI-Astrology-Predictor/
│
├── app.py              # Streamlit Dashboard
├── model.py            # RNN Model Training
├── utils.py            # Feature Engineering
├── dataset.csv         # Sample Dataset
├── model.h5            # Trained Model
├── requirements.txt    # Dependencies
└── README.md           # Project Documentation
```

---

## 📊 Dataset Details

The dataset includes:

* Birth Date & Time
* Location (Latitude, Longitude)
* Planetary Positions (simulated or API-based)
* Historical labels:

  * Marriage Age
  * Career Success Score
  * Financial Score

---

## 🧠 Model Architecture

* Recurrent Neural Network (RNN)
* LSTM Layers for sequence learning
* Dropout for regularization
* Multi-output prediction:

  * Marriage Age
  * Career Probability
  * Financial Score

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-Astrology-Predictor.git
cd AI-Astrology-Predictor
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🌐 Deployment

You can deploy this project easily on:

* Streamlit Cloud
* Render
* AWS / Azure

### Streamlit Cloud Steps:

1. Push project to GitHub
2. Go to Streamlit Cloud
3. Connect repository
4. Select `app.py`
5. Deploy 🚀

---

## 📸 Demo (Optional)

Add screenshots here:

* Dashboard UI
* Prediction Output
* Graphs

---

## 🔍 Future Enhancements

* 🔗 Integration with real astrology APIs
* 📊 More accurate datasets
* 🧠 Advanced models (Transformers)
* 📱 Mobile-friendly UI
* 💾 User history tracking

---

## ⚠️ Disclaimer

This project is intended for **educational and research purposes only**.

Predictions are based on **machine learning patterns**, not actual astrological certainty. Results should not be used for real-life decision-making.

---

## 👨‍💻 Author

**Your Name**

* GitHub: https://github.com/your-username
* LinkedIn: Your Profile

---

## ⭐ Support

If you like this project:

⭐ Star this repository
🍴 Fork it
📢 Share it

---

## 💡 Inspiration

Combining ancient astrology concepts with modern AI techniques to explore **pattern-based life predictions**.

---
