import pandas as pd
import numpy as np

def clean_solar_data(df):
    """Clean solar data by removing outliers and handling missing values"""
    df_clean = df.copy()
    
    # Convert timestamp
    df_clean['Timestamp'] = pd.to_datetime(df_clean['Timestamp'])
    
    # Handle missing values first
    numeric_cols = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb']
    for col in numeric_cols:
        if col in df_clean.columns:
            # Fill missing values with median of the column
            median_val = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(median_val)
            
            # Remove negative values for radiation metrics
            if col in ['GHI', 'DNI', 'DHI']:
                df_clean[col] = df_clean[col].clip(lower=0)
            
            # Remove outliers using percentile method
            Q1 = df_clean[col].quantile(0.25)
            Q3 = df_clean[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df_clean[col] = df_clean[col].clip(lower=lower_bound, upper=upper_bound)
    
    return df_clean

def calculate_summary_stats(df):
    """Calculate summary statistics for solar metrics"""
    metrics = ['GHI', 'DNI', 'DHI']
    summary = {}
    
    for metric in metrics:
        if metric in df.columns:
            valid_data = df[metric].dropna()
            summary[metric] = {
                'mean': valid_data.mean(),
                'median': valid_data.median(),
                'std': valid_data.std(),
                'max': valid_data.max(),
                'min': valid_data.min(),
                'count': len(valid_data)
            }
    
    return summary 