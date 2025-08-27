
import os
import requests
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load API key from .env
load_dotenv()
API_KEY = os.getenv('NASA_API_KEY')

# Set date range (last 7 days)
end_date = datetime.today()
start_date = end_date - timedelta(days=7)

API_URL = 'https://api.nasa.gov/neo/rest/v1/feed'
params = {
    'start_date': start_date.strftime('%Y-%m-%d'),
    'end_date': end_date.strftime('%Y-%m-%d'),
    'api_key': API_KEY
}

response = requests.get(API_URL, params=params)
data = response.json()

asteroids = []
for date in data['near_earth_objects']:
    for obj in data['near_earth_objects'][date]:
        name = obj['name']
        approach = obj['close_approach_data'][0]
        size_km = (obj['estimated_diameter']['kilometers']['estimated_diameter_min'] +
                   obj['estimated_diameter']['kilometers']['estimated_diameter_max']) / 2
        rel_vel_kps = float(approach['relative_velocity']['kilometers_per_second'])
        miss_km = float(approach['miss_distance']['kilometers'])
        pha_flag = obj['is_potentially_hazardous_asteroid']
        asteroids.append({
            'name': name,
            'date': approach['close_approach_date'],
            'size_km': size_km,
            'rel_vel_kps': rel_vel_kps,
            'miss_km': miss_km,
            'pha_flag': pha_flag
        })

# Save to CSV
df = pd.DataFrame(asteroids)
df.to_csv('data/asteroids.csv', index=False)

# Save to Excel using xlsxwriter
excel_path = 'data/asteroids.xlsx'
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Asteroids')

print(f"Saved {len(df)} asteroid records to data/asteroids.csv and {excel_path}")
