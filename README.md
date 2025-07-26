# 💸 Restaurant Tips Dashboard

This project is a Shiny for Python web application that visualizes restaurant tips data from `data/tips.csv` using interactive controls and a Plotly chart.

## Features
- Select day of the week to filter data
- Option to include/exclude smoker data
- Data table and summary info
- Interactive scatter plot (total bill vs tip)
- Auto-reloads data when `data/tips.csv` changes

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

> Note: For Plotly image export, you may need to install `kaleido`:
> ```powershell
> pip install kaleido
> ```

### 3. Run the App
Start the Shiny app (from the project root):

```powershell
shiny run --reload dashboard/app.py
```


## File Structure
- `dashboard/app.py` — Main Shiny app code
- `data/tips.csv` — Data file
- `requirements.txt` — Python dependencies
- `README.md` — Project instructions

## Usage
- Select a day and toggle smoker data to filter the table and chart.
- The chart is saved as `chart.png` and displayed as an image in the app.

## Troubleshooting
- If you see errors about missing packages, ensure you have activated the virtual environment and installed all requirements.
- For image export issues, make sure `kaleido` is installed.

---

Made with [Shiny for Python](https://shiny.posit.co/py/) and [Plotly](https://plotly.com/python/).