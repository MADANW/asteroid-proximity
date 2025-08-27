# Asteroid Close-Approach Explorer

An interactive data science project to explore near-Earth asteroid data using NASA’s NeoWs API, with EDA, visualizations, and a Streamlit dashboard.

##  Project Overview
- Fetches and analyzes near-Earth asteroid data
- Explores distributions of size, velocity, and closest approaches
- a simple logistic regression classifier to predict hazardous asteroids
- Interactive Streamlit app for data exploration

##  Features
- Data fetching and cleaning from NASA NeoWs API
- Exploratory Data Analysis (EDA) with histograms, scatter plots, and summary tables
- Top-10 closest asteroids table
- Streamlit dashboard with interactive charts and data preview
- (Optional) Hazard classifier results tab

##  Setup
1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd asteroid-proximity
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv myenv
   source myenv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **(Optional) Get a NASA API key:**
   - Visit https://api.nasa.gov/ to get a free API key (recommended to avoid DEMO_KEY rate limits).

## 🚦 Usage
- **Jupyter Notebook:**
  - Run EDA and ML steps in `notebooks/asteroid.ipynb`.
- **Streamlit App:**
  - From the project root, launch the dashboard:
    ```sh
    streamlit run app/streamlit_app.py
    ```
  - The app will load asteroid data and display interactive charts and tables.

## 📊 Example Visualizations
- Asteroid size and velocity histograms
- Scatter plot: size vs. miss distance
- Top-10 closest approaches table

## 📝 Credits
- Data: [NASA NeoWs API](https://api.nasa.gov/)
- Built with Python, pandas, matplotlib, seaborn, and Streamlit

## 📄 License
MIT License