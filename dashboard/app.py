from shiny import App, reactive, render, ui
import pandas as pd
import plotly.express as px
from pathlib import Path

# ===== Continuous update setup using reactive.file_reader =====
@reactive.file_reader(Path("data/tips.csv"))
def read_tips():
    # Automatically reload data when file changes
    return pd.read_csv("data/tips.csv")

# ===== UI layout =====
app_ui = ui.page_fluid(
    ui.h2("💸 Restaurant Tips Dashboard"),
    
    # Input: Select day of week
    ui.input_select(
        "selected_day", 
        "Select Day of the Week:", 
        choices=["All", "Thur", "Fri", "Sat", "Sun"], 
        selected="All"
    ),
    
    # Input: Show/hide smoker status
    ui.input_checkbox("show_smoker", "Include Smoker Data", True),
    
    # Output: Confirm input selection
    ui.output_text_verbatim("info"),

    # Output: Chart
    ui.output_image("chart", height="400px"),
    
    # Output: Table
    ui.output_data_frame("table") 
    
)

# ===== Server logic =====
def server(input, output, session):
    
    @reactive.calc
    def filtered_data():
        df = read_tips()
        
        # Filter by day if not 'All'
        if input.selected_day() != "All":
            df = df[df["day"] == input.selected_day()]
        
        # Filter by smoker status
        if not input.show_smoker():
            df = df[df["smoker"] == "No"]
        
        return df

    @output
    @render.text
    def info():
        return f"Showing data for day: {input.selected_day()}, Smoker included: {input.show_smoker()}"

    @output
    @render.image
    def chart():
        df = filtered_data()
        fig = px.scatter(
            df,
            x="total_bill",
            y="tip",
            color="sex",
            title="Tip vs Total Bill"
        )
        img_path = "chart.png"
        fig.write_image(img_path)
        return {
            "src": img_path,
            "alt": "Tip vs Total Bill",
            "width": "auto",
            "height": "400px"
        }

    @output
    @render.data_frame
    def table():
        return filtered_data()

    

# ===== App instance =====
app = App(app_ui, server)