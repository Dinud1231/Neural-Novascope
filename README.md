# 🌍 A World Away: Hunting for Exoplanets with AI

## 🚀 About the Project
Our project leverages Artificial Intelligence (AI) and Machine Learning (ML) to automatically identify *exoplanets* from NASA’s open-source datasets.  
Traditionally, many exoplanets were discovered manually — our model accelerates this process by detecting planetary patterns, classifying exoplanets, and estimating their habitability potential using AI.

This project is developed as part of the *NASA International Space Apps Challenge 2025* at *Caldwell University, New Jersey (USA)*.

---

## 👩‍🚀 Team Members

•⁠  ⁠*Muhammad Tasveeb Khan* — Computer Science  
  Skills: Python, Machine Learning, Data Analytics, Docker, API Integration  
  📧 Email: muhammadtasveebkhan@gmail.com  
  
•⁠  ⁠*Dinud Fernando* — Computer Science & Business Analytics
  Skills: Machine Learning, Data Cleaning, Model Evaluation, Deployment  

•⁠  ⁠*Divash Tuladhar* — Computer Science & Business Analytics  
  Skills: Data Science, AI/ML Modeling, Cloud Computing, Data Visualization  

•⁠  ⁠*Sara Rani Sen* — Finance  
  Skills: Financial Modeling, Data Interpretation, Research, Economic Forecasting, Budget Analysis  

•⁠  ⁠*Vakhtangi Jvarsheishvili* — Business Analytics  
  Skills: Data Analysis, Project Planning, Business Modeling, Strategy & Reporting  

---

## 🌌 Challenge
*A World Away: Hunting for Exoplanets with AI*

### Challenge Overview
Data from various space-based exoplanet survey missions have led to thousands of discoveries, but most of these exoplanets were identified manually.  
With advances in *AI and ML*, we aim to build a model trained on NASA's open exoplanet datasets to:
•⁠  ⁠Automatically analyze large data sets  
•⁠  ⁠Accurately identify exoplanets  
•⁠  ⁠Classify exoplanets by type and potential habitability  

---

## 🧠 AI / Machine Learning Models

1.⁠ ⁠*Nearest Neighbors (KNN)*  
   Finds exoplanets with similar physical characteristics for pattern analysis.

2.⁠ ⁠*Classification Models (Random Forest / Logistic Regression)*  
   Classifies exoplanets into known categories (Neptunian, Super Earth, Gas Giant, Terrestrial).

3.⁠ ⁠*Clustering Analysis (K-Means)*  
   Groups exoplanets based on their shared features to reveal hidden patterns.

4.⁠ ⁠*LLM-Based Habitability Analysis (ChatGPT API)*  
   Uses Large Language Models to analyze planetary parameters (size, temperature, orbit)  
   and determine habitability potential in real time.

---

## 📊 NASA Data Sources

•⁠  ⁠*NASA Exoplanet Archive:*  
  [https://exoplanetarchive.ipac.caltech.edu/](https://exoplanetarchive.ipac.caltech.edu/)

•⁠  ⁠*Kepler and TESS Mission Data*  
  Used for model training and validation.

•⁠  ⁠*OpenAI GPT API (LLM integration)*  
  For natural language reasoning and habitability scoring.

---

## 🧰 Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| *Language* | Python |
| *Frameworks* | TensorFlow, Scikit-learn, Pandas, NumPy |
| *AI / LLM API* | OpenAI GPT |
| *Data Visualization* | Matplotlib, Plotly |
| *Containerization* | Docker |
| *Version Control* | Git + GitHub |

---

## 🛰️ How It Works

1.⁠ ⁠*Data Collection:*  
   We use NASA's Exoplanet Archive and preprocess datasets (removing noise, missing values).

2.⁠ ⁠*Feature Engineering:*  
   Extract physical and orbital features (mass, radius, stellar flux, orbital period).

3.⁠ ⁠*Model Training:*  
   Train ML algorithms (classification + clustering) to predict and categorize exoplanets.

4.⁠ ⁠*Prediction & Visualization:*  
   Generate visual outputs and habitability scores for new exoplanet data.

---

## 💻 Project Setup (Local or Docker)

### Run Locally
```bash
# Clone this repository
git clone https://github.com/<your-username>/<repo-name>.git

# Go into the project folder
cd <repo-name>

# Install dependencies
pip install -r requirements.txt

# Run main script
python main.py
