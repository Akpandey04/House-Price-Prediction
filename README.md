# 🏠 Bengaluru House Price Prediction Web App

A machine learning–powered web application that predicts **house prices in Bengaluru** based on user inputs such as total area, location, number of bedrooms, bathrooms, floor level, and city. Built using Python, scikit-learn, and deployed via Render.

🔗 **Live App**: [Click Here to Try It](https://house-price-prediction-rpf5.onrender.com/)

---

## 📌 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Input Parameters](#input-parameters)
- [Model Training](#model-training)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Future Work](#future-work)
- [Author](#author)

---

## 📖 About

This project demonstrates a complete machine learning pipeline applied to the real estate domain in **Bengaluru**. The goal is to predict the selling price of a house based on multiple user-defined features. It also calculates the rate per square foot to give users additional insights.

The app is trained on a Bengaluru housing dataset and is deployed with a simple, responsive web interface.

---

## ✅ Features

- Predicts **house price in Bengaluru** using ML models    
- Accepts multiple real-world inputs (e.g., bedrooms, location, area, etc.)  
- Supports **all major locations in Bengaluru**  
- Deployed online using **Render**  
- Clean UI with Bootstrap

---

## ⚙️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Python, Flask / Streamlit  
- **Machine Learning**: scikit-learn (Random Forest, Linear Regression, Ridge)  
- **Data Handling**: Pandas, NumPy  
- **Deployment**: Render  
- **Version Control**: Git, GitHub

---

## 🔍 How It Works

1. User enters:
   - Total Area (in sqft)
   - Location (within Bengaluru)
   - Number of Bedrooms
   - Number of Bathrooms

2. The app uses a trained ML model to predict:
   - **Selling Price (in ₹)**

---

## 🧾 Input Parameters

| Feature         | Type    | Description                           |
|-----------------|---------|---------------------------------------|
| Area (sqft)     | Float   | Total area of the house               |
| City            | String  | City name (Bengaluru)                 |
| Location        | String  | Locality/area within Bengaluru        |
| Bedrooms        | Integer | Number of bedrooms                    |
| Bathrooms       | Integer | Number of bathrooms                   |

---

## 🧠 Model Training

- **Dataset**: Bengaluru Housing Prices Dataset (`bangalore.csv`)
- **Algorithms Used**:
  - Random Forest Regressor
  - Linear Regression
  - Ridge

- **Evaluation Metrics**:
  - R² Score
  - Mean Absolute Error
  - Cross-validation

- **Data Preprocessing**:
  - Label Encoding of locations
  - Handling missing values
  - Removing outliers
  - Feature scaling 

---

## 🚀 Getting Started (Run Locally)

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- pip

### Setup

```bash
git clone https://github.com/Akpandey04/House-Price-Prediction.git
cd House-Price-Prediction
pip install -r requirements.txt
python app.py
```

📍 For Streamlit users:
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```bash
├── app.py             # Main web app file (Flask/Streamlit)
├── model.pkl          # Trained ML model (pickle format)
├── locations.pkl      # Encoded list of Bengaluru locations
├── bangalore.csv      # Cleaned dataset
├── requirements.txt   # Python dependencies
├── templates/         # HTML templates (if using Flask)
│   └── index.html
└── README.md          # Project documentation
```

---

## 🖼️ Screenshots

> screenshot is attached![Screenshot 2025-07-01 210415](https://github.com/user-attachments/assets/85adc8d7-f4fd-4f14-ac1d-416080fd736b)
![Screenshot 2025-07-01 210350](https://github.com/user-attachments/assets/7126a657-c102-4d0e-97aa-08aaaefebdab)
  
Example:  
```md
![Homepage](https://raw.githubusercontent.com/yourusername/repo/main/screenshots/homepage.png)
```

---

## 🔮 Future Work

- Expand to support other Indian cities  
- Integrate Google Maps API  
- Add rental price prediction   
- Add login functionality and save user predictions  
- Improve UI with charts and animations

---

## 👤 Author

**Adarsh Kumar Pandey**   
🌐 GitHub: [@Akpandey04](https://github.com/Akpandey04)  
🔗 LinkedIn: [@akpandey4](https://www.linkedin.com/in/akpandey4?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

---

## ⭐️ Show Your Support

If you liked this project, please ⭐️ the repo and share it!

---
