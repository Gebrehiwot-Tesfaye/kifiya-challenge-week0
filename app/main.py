import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils import clean_solar_data, calculate_summary_stats

st.set_page_config(page_title="Solar Data Analysis", layout="wide")

st.title('Solar Data Analysis Dashboard')

# Update the file mapping
FILE_MAPPING = {
    'Benin': 'benin-malanville.csv',
    'Sierra Leone': 'sierraleone-bumbuna.csv',
    'Togo': 'togo-dapaong_qc.csv'
}

# Load data first to get date range
@st.cache_data
def load_data(country):
    try:
        filename = FILE_MAPPING[country]
        df = pd.read_csv(f'data/{filename}')
        
        # Basic data validation
        required_cols = ['Timestamp', 'GHI', 'DNI', 'DHI', 'Tamb']
        if not all(col in df.columns for col in required_cols):
            raise ValueError("Missing required columns in the dataset")
            
        # Convert Timestamp
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        
        # Clean the data
        df_clean = clean_solar_data(df)
        return df_clean
        
    except Exception as e:
        st.error(f"Error loading data for {country}: {str(e)}")
        return None

# Load initial data to get date range
df = load_data('Benin')
if df is not None:
    min_date = df['Timestamp'].min().date()
    max_date = df['Timestamp'].max().date()
else:
    min_date = pd.to_datetime('2023-01-01').date()
    max_date = pd.to_datetime('2023-12-31').date()

# Sidebar controls with dynamic date range
st.sidebar.header('Controls')
country = st.sidebar.selectbox('Select Country', ['Benin', 'Sierra Leone', 'Togo'])
metric = st.sidebar.selectbox('Select Metric', ['GHI', 'DNI', 'DHI'])
time_range = st.sidebar.date_input('Select Date Range', 
                                  value=[min_date, max_date],
                                  min_value=min_date,
                                  max_value=max_date)

@st.cache_data
def load_data(country):
    try:
        filename = FILE_MAPPING[country]
        # Read the CSV file
        df = pd.read_csv(f'data/{filename}')
        
        # Basic data validation
        required_cols = ['Timestamp', 'GHI', 'DNI', 'DHI', 'Tamb']
        if not all(col in df.columns for col in required_cols):
            raise ValueError("Missing required columns in the dataset")
            
        # Convert Timestamp
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        
        # Clean the data
        df_clean = clean_solar_data(df)
        
        # Verify we have valid data
        if df_clean.empty or df_clean[['GHI', 'DNI', 'DHI']].isna().all().any():
            raise ValueError("No valid data after cleaning")
            
        return df_clean
        
    except Exception as e:
        st.error(f"Error loading data for {country}: {str(e)}")
        return None

try:
    # Load and process data
    df = load_data(country)
    if df is None:
        st.error("Failed to load data")
    else:
        # Filter by date range
        mask = (df['Timestamp'].dt.date >= time_range[0]) & (df['Timestamp'].dt.date <= time_range[1])
        df_filtered = df.loc[mask].copy()
        
        if len(df_filtered) == 0:
            st.warning("No data available for the selected date range")
        else:
            # Display metrics
            stats = calculate_summary_stats(df_filtered)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Average " + metric, f"{stats[metric]['mean']:.2f} W/m²")
            col2.metric("Max " + metric, f"{stats[metric]['max']:.2f} W/m²")
            col3.metric("Std Dev " + metric, f"{stats[metric]['std']:.2f} W/m²")
            
            # Add data info
            st.info(f"Showing {len(df_filtered):,} measurements from {df_filtered['Timestamp'].min().strftime('%Y-%m-%d')} to {df_filtered['Timestamp'].max().strftime('%Y-%m-%d')}")
            
            # Time series plot
            st.subheader('Solar Radiation Over Time')
            fig = px.line(df_filtered, x='Timestamp', y=metric,
                          title=f'{metric} Values - {country}')
            st.plotly_chart(fig, use_container_width=True)
            
            # Additional analysis
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader('Distribution Analysis')
                fig = px.histogram(df_filtered, x=metric,
                                  title=f'{metric} Distribution')
                st.plotly_chart(fig)
                
            with col2:
                st.subheader('Correlation with Temperature')
                try:
                    fig = px.scatter(
                        df_filtered, 
                        x='Tamb', 
                        y=metric,
                        title=f'{metric} vs Temperature',
                        trendline="ols"
                    )
                except ImportError:
                    # Fallback to basic scatter plot if statsmodels isn't available
                    fig = px.scatter(
                        df_filtered, 
                        x='Tamb', 
                        y=metric,
                        title=f'{metric} vs Temperature'
                    )
                fig.update_layout(
                    xaxis_title='Temperature (°C)',
                    yaxis_title=f'{metric} (W/m²)'
                )
                st.plotly_chart(fig)

except Exception as e:
    st.error(f"Error loading data: {str(e)}") 