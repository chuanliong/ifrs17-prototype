# IFRS 17 Python Prototype

A Python-based IFRS 17 valuation engine built to demonstrate actuarial 
and accounting concepts using real-world insurance contract data.

## Project Structure
- `data/contracts.csv` - Input contract data
- `src/classifier.py` - PAA vs GMM classification engine
- `src/calculations.py` - Risk adjustment and CSM release calculations
- `src/report.py` - Portfolio summary and interactive charts
- `main.py` - Main pipeline that ties everything together

## Features
- Automatic contract classification (PAA vs GMM)
- Best Estimate Liability (BEL) calculation
- Risk Adjustment calculation
- CSM release schedule (GMM contracts only)
- Portfolio summary with totals
- Interactive charts using Plotly

## How to Run
1. Install dependencies: `pip3 install pandas plotly`
2. Run: `python3 main.py`

## Tools & Libraries
- Python 3.14
- Pandas
- NumPy
- Plotly

## Background
Built as part of a learning journey combining actuarial domain knowledge with Python programming skills.