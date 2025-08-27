import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Asteroid Close-Approach Explorer')

# Load data
data_path = '../data/asteroids.csv'
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
