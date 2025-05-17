import pandas as pd
import sys
sys.path.append('..')
from app.utils import clean_solar_data

# Process each country's data
countries = {
    'Benin': 'benin-malanville.csv',
    'Sierra Leone': 'sierralione-bumbuna.csv',
    'Togo': 'togo-dapaong_qc.csv'
}

for country, filename in countries.items():
    # Load data
    df = pd.read_csv(f'data/{filename}')
    
    # Clean data
    df_clean = clean_solar_data(df)
    
    # Save cleaned data
    clean_filename = f"data/{country.lower().replace(' ', '_')}_clean.csv"
    df_clean.to_csv(clean_filename, index=False)
    print(f"Processed {country}: {clean_filename}") 