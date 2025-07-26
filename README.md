# 💸 Restaurant Tips Dashboard

This project is a Shiny for Python web application that visualizes restaurant tips data using the built-in `seaborn` tips dataset, with interactive controls and a matplotlib chart.

## Features
- Select day of the week to filter data
- Option to include/exclude smoker data
- Data table and summary info
- Interactive scatter plot (total bill vs tip) using matplotlib
- Uses the built-in dataset, so no external data file is required

## Setup Instructions

### 1. Create and Activate Virtual Environment
A virtual environment is already set up in `.venv`. To activate it:

```powershell
.venv\Scripts\Activate
```

### 2. Install Requirements
Install all required packages:

```powershell
pip install -r requirements.txt
```



### 3. Run the App
Start the Shiny app (from the project root):

```powershell
shiny run --reload dashboard/app.py
```


## File Structure
- `dashboard/app.py` — Main Shiny app code
- `requirements.txt` — Python dependencies
- `README.md` — Project instructions

## Usage
- Select a day and toggle smoker data to filter the table and chart.
- The chart is rendered interactively using matplotlib in the app.
- No need to provide a data file; the app loads the tips dataset automatically.

## Troubleshooting
- If you see errors about missing packages, ensure you have activated the virtual environment and installed all requirements.


## Deployment Notes
This app requires a Python server environment to run. GitHub Pages only supports static content and cannot host Python apps. To deploy your Shiny for Python app, use a platform like [Shiny for Python hosting](https://www.shiny.posit.co/py/), Heroku, or similar Python web hosting services.

---

Made with [Shiny for Python](https://shiny.posit.co/py/) and [matplotlib](https://matplotlib.org/).