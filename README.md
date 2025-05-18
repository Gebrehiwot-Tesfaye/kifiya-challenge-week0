# Solar Data Analysis Project

## Overview

This project analyzes solar radiation data from three African countries (Benin, Sierra Leone, and Togo) to identify optimal locations for solar installations. The analysis includes data cleaning, exploratory data analysis, and interactive visualizations through a Streamlit dashboard.

## Features

- Data cleaning and preprocessing
- Statistical analysis of solar radiation metrics
- Interactive data visualization
- Cross-country comparison
- Time series analysis
- Temperature correlation studies

## Project Structure

```
kifiya-challenge-week0/
├── app/
│   ├── main.py          # Streamlit dashboard application
│   └── utils.py         # Data processing utilities
├── data/                # Solar radiation data files
├── notebooks/           # Jupyter notebooks for analysis
├── scripts/             # Processing scripts
├── tests/              # Unit tests
└── README.md           # Project documentation
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd kifiya-challenge-week0
```

2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit dashboard:

```bash
streamlit run app/main.py
```

2. Use the sidebar controls to:
   - Select country
   - Choose metric (GHI, DNI, DHI)
   - Set date range
   - View different visualizations

## Development

- Follow PEP 8 style guidelines
- Write docstrings for all functions and classes
- Add unit tests for new features
- Use meaningful commit messages

## Data Sources

The solar radiation data includes:

- Global Horizontal Irradiance (GHI)
- Direct Normal Irradiance (DNI)
- Diffuse Horizontal Irradiance (DHI)
- Temperature and other environmental metrics

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes with descriptive messages
4. Push to your fork
5. Submit a pull request

## License

[Add your license information here]

```bash
streamlit run app/main.py
```

## Data Files

- `data/benin_clean.csv`: Cleaned Benin solar data
- `data/sierra_leone_clean.csv`: Cleaned Sierra Leone solar data
- `data/togo_clean.csv`: Cleaned Togo solar data

## Dashboard Features

- Date range selection
- Country-specific data visualization
- Summary statistics display
- Interactive charts

## Project Structure

- `app/`: Streamlit app files
- `data/`: Cleaned data files
- `notebooks/`: Jupyter notebooks for data exploration
- `requirements.txt`: Python dependencies
- `README.md`: Project overview

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes and commit them
4. Push to your fork
5. Create a pull request
