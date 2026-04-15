# 1- Machine Learning & 3- XAI (SHAP/LIME)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import shap
import pickle
import os
import matplotlib.pyplot as plt

# Dinamik Dosya Yolları
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "diabetes.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "diabetes_model.pkl")
PLOT_PATH = os.path.join(BASE_DIR, "models", "shap_plot.png")

def train_diabetes_model():
    if not os.path.exists(DATA_PATH):
        print(f"HATA: Veri dosyası bulunamadı -> {DATA_PATH}")
        return

    df = pd.read_csv(DATA_PATH)
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 1. Machine Learning
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Modeli Kaydet
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    
    # 3. Explainable AI (XAI)
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_train)
    shap.summary_plot(shap_values, X_train, show=False)
    plt.savefig(PLOT_PATH, bbox_inches='tight')
    plt.close()
    
    print("✓ ML Modeli ve XAI Grafiği hazır!")

if __name__ == "__main__":
    train_diabetes_model()