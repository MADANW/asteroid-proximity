# Asteroid Close-Approach Explorer

An interactive data science project to explore near-Earth asteroid data using NASA’s NeoWs API, with EDA, visualizations, a logistic regression classifier, and a Streamlit dashboard.

## Project Overview
- Fetches and analyzes near-Earth asteroid data
- Explores distributions of size, velocity, and closest approaches
- Implements a logistic regression classifier to predict hazardous asteroids
- Interactive Streamlit app for data exploration and ML results

## Features
- Data fetching and cleaning from NASA NeoWs API
- Exploratory Data Analysis (EDA) with histograms, scatter plots, and summary tables
- Top-10 closest asteroids table
- Streamlit dashboard with interactive charts, data preview, and classifier results
- Logistic regression classifier with accuracy and AUROC metrics

## Setup
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
  - The app will load asteroid data, display interactive charts and tables, and let you run the classifier interactively.

## Example Visualizations
- Asteroid size and velocity histograms
- Scatter plot: size vs. miss distance
- Top-10 closest approaches table
- Classifier metrics: accuracy, AUROC, and classification report

## Credits
- Data: [NASA NeoWs API](https://api.nasa.gov/)
- Built with Python, pandas, matplotlib, seaborn, scikit-learn, and Streamlit

## License
MIT License