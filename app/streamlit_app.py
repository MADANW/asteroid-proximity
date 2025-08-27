
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))
from classifier import run_logistic_regression

st.title('Asteroid Close-Approach Explorer')

# Load data using an absolute path based on the project root
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'asteroids.csv')
try:
    df = pd.read_csv(data_path)
    st.success(f"Loaded data from {data_path}")
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()

# Show data preview
st.subheader('Data Preview')
st.dataframe(df.head())

# Plot: Asteroid Size Distribution
st.subheader('Asteroid Size Distribution (km)')
fig1, ax1 = plt.subplots()
sns.histplot(df['size_km'], bins=30, kde=True, ax=ax1)
ax1.set_xlabel('Size (km)')
ax1.set_ylabel('Count')
st.pyplot(fig1)

# Plot: Relative Velocity Distribution
st.subheader('Relative Velocity Distribution (km/s)')
fig2, ax2 = plt.subplots()
sns.histplot(df['rel_vel_kps'], bins=30, kde=True, color='orange', ax=ax2)
ax2.set_xlabel('Relative Velocity (km/s)')
ax2.set_ylabel('Count')
st.pyplot(fig2)

# Classifier Results
st.subheader('Hazardous Asteroid Classifier (Logistic Regression)')
if st.button('Run Classifier'):
    results = run_logistic_regression(df)
    st.metric('Accuracy', f"{results['accuracy']:.3f}")
    st.metric('AUROC', f"{results['auroc']:.3f}")
    st.text('Classification Report:')
    st.text(results['report'])
