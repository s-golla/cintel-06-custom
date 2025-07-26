from shiny import App, reactive, render, ui
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
tips = sns.load_dataset("tips")

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
        df = tips
        
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
    @render.plot
    def chart():
        df = filtered_data()
        fig, ax = plt.subplots()
        colors = {'Male': 'blue', 'Female': 'red'}
        for sex, group in df.groupby('sex', observed=False):
            ax.scatter(group['total_bill'], group['tip'], label=sex, color=colors.get(sex, 'gray'))
        ax.set_xlabel('Total Bill')
        ax.set_ylabel('Tip')
        ax.set_title('Tip vs Total Bill')
        ax.legend()
        fig.tight_layout()
        return fig

    @output
    @render.data_frame
    def table():
        return filtered_data()

    

# ===== App instance =====
app = App(app_ui, server)