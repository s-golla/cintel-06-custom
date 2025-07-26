# Restaurant Tips Dashboard

An interactive dashboard built with Shiny Express for Python, visualizing restaurant tips data from the seaborn library.

## Features

- Sidebar with emoji icons, colored headers, and filters:
  - Day of the week
  - Smoker status
  - Total bill range (slider)
  - Sex
- Metric cards for:
  - Total bills analyzed
  - Average tip percentage
  - Number of records
- Charts:
  - Tip vs Total Bill (scatter plot)
  - Average Tip by Day (bar chart)
  - Tip Distribution by Sex (violin plot)
- Filtered data table

## Usage

1. Install requirements:
   ```powershell
   pip install -r requirements.txt
   ```
2. Run the dashboard:
   ```powershell
   shiny run --reload dashboard/app.py
   ```

## Tech Stack

- Shiny Express for Python
- pandas
- matplotlib
- seaborn

## File Structure

- dashboard/app.py: Main dashboard code
- requirements.txt: Python dependencies
- README.md: Project documentation
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