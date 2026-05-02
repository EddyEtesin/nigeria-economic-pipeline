# 🇳🇬 Nigeria Economic Pulse Pipeline

An end-to-end data engineering pipeline that automatically extracts, transforms, loads and visualizes Nigeria's key economic indicators.

## Dashboard Preview
*![alt text](image.png)*

## 🏗️ Architecture
 
Extract (APIs) → Transform (Pandas) → Load (SQLite) → Visualize (Streamlit)

## Data Sources
- **Exchange Rate** — ExchangeRate API (Live USD/NGN rate)
- **Inflation Rate** — World Bank API (Last 10 years)
- **GDP** — World Bank API (Last 10 years)

## Tech Stack
- Python
- Pandas
- SQLite
- Streamlit
- Plotly
- Schedule (Automation)
- Git & GitHub

## How to Run Locally

1. Clone the repo
```bash
git clone https://github.com/your-username/nigeria-economic-pipeline.git
cd nigeria-economic-pipeline
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the full pipeline
```bash
python pipeline.py
```

5. Launch the dashboard
```bash
streamlit run dashboard.py
```

## Built By
**Ediomo Usoro Etesin**  
Electrical & Electronics Engineer | Certified Data Analyst | Data Engineering Trainee  
[LinkedIn](https://linkedin.com/in/ediomoetesin) | [GitHub](https://github.com/EddyEtesin)
