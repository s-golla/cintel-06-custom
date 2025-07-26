from shiny.express import ui, input, render
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the tips dataset
tips = sns.load_dataset("tips")

# Page options
ui.page_opts(title="Restaurant Tips Dashboard", fillable=True)

# Sidebar layout and filters
with ui.sidebar(title="🌈 Data Filters", style="padding:4px 4px 4px 4px;"):
    ui.h6("📅 Day & 🚬 Smoker", style="color:#1976d2;background-color:#e3f2fd;padding:1px 2px;border-radius:4px;font-size:0.95rem;margin-bottom:8px;")
    ui.input_select(
        "selected_day",
        "Day of the Week:",
        choices=["All", "Thur", "Fri", "Sat", "Sun"],
        selected="All"
    )
    ui.input_checkbox("show_smoker", "Include Smoker Data", True)
    ui.hr(style="border-top:1px solid #1976d2;margin:6px 0;")
    ui.h6("💵 Bill & 👤 Sex", style="color:#388e3c;background-color:#e8f5e9;padding:1px 2px;border-radius:4px;font-size:0.95rem;margin-bottom:8px;")
    ui.input_slider(
        "bill_range",
        "Total Bill Range:",
        min=float(tips["total_bill"].min()),
        max=float(tips["total_bill"].max()),
        value=(float(tips["total_bill"].min()), float(tips["total_bill"].max())),
        step=0.5
    )
    ui.input_select(
        "selected_sex",
        "Sex:",
        choices=["All", "Male", "Female"],
        selected="All"
    )
    ui.hr(style="border-top:1px solid #388e3c;margin:6px 0;")
    ui.h6("🧭 Dashboard Information", style="color:#6d4c41;background-color:#fff3e0;padding:1px 2px;border-radius:4px;font-size:0.95rem;margin-bottom:8px;")
    @render.text
    def info():
        bill_min, bill_max = input.bill_range()
        return (
            f"Day: {input.selected_day()}\n"
            f"Smoker: {'Included' if input.show_smoker() else 'Excluded'}\n"
            f"Bill Range: ${bill_min:.2f} - ${bill_max:.2f}\n"
            f"Sex: {input.selected_sex()}"
        )

with ui.layout_columns():  # Metric cards row
    with ui.card(style="background-color:lightblue; height:180px; width:360px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;"):
        ui.h4("💰 Total Bills Analyzed")
        @render.text
        def total_bills():
            return f"${filtered_data()['total_bill'].sum():.2f}"

    with ui.card(style="background-color:moccasin; height:180px; width:360px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;"):
        ui.h4("📊 Average Tip Percentage")
        @render.text
        def avg_tip_percent():
            df = filtered_data()
            if not df.empty:
                return f"{((df['tip'] / df['total_bill']).mean() * 100):.2f}%"
            return "N/A"

    with ui.card(style="background-color:honeydew; height:180px; width:360px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;"):
        ui.h4("👥 Number of Records")
        @render.text
        def num_records():
            return f"{len(filtered_data())} records"


with ui.layout_columns():  # Charts and data table row
    with ui.card(full_screen=True):
        ui.card_header("Tip vs Total Bill by Sex (Scatter)")
        @render.plot
        def chart_scatter():
            df = filtered_data()
            fig, ax = plt.subplots()
            colors = {'Male': 'blue', 'Female': 'red'}
            for sex, group in df.groupby('sex', observed=False):
                ax.scatter(group['total_bill'], group['tip'], label=sex, color=colors.get(sex, 'gray'))
            ax.set_xlabel('Total Bill ($)')
            ax.set_ylabel('Tip ($)')
            ax.set_title('Tip vs Total Bill')
            ax.legend(title='Sex')
            fig.tight_layout()
            return fig

    with ui.card(full_screen=True):
        ui.card_header("Average Tip by Day (Bar Chart)")
        @render.plot
        def chart_bar():
            df = filtered_data()
            avg_tip = df.groupby('day', observed=False)['tip'].mean()
            fig, ax = plt.subplots()
            avg_tip.plot(kind='bar', ax=ax, color='skyblue')
            ax.set_xlabel('Day')
            ax.set_ylabel('Average Tip ($)')
            ax.set_title('Average Tip by Day')
            fig.tight_layout()
            return fig

    with ui.card(full_screen=True):
        ui.card_header("Tip Distribution by Sex (Violin Plot)")
        @render.plot
        def chart_violin():
            df = filtered_data()
            fig, ax = plt.subplots()
            sexes = ["Male", "Female"]
            data = [df[df["sex"] == sex]["tip"] for sex in sexes]
            parts = ax.violinplot(data, showmeans=True, showmedians=True)
            ax.set_xticks([1, 2])
            ax.set_xticklabels(sexes)
            ax.set_xlabel('Sex')
            ax.set_ylabel('Tip ($)')
            ax.set_title('Tip Distribution by Sex')
            fig.tight_layout()
            return fig

    with ui.card(full_screen=True):
        ui.card_header("Filtered Tips Data")
        @render.data_frame
        def table():
            return filtered_data()


def filtered_data():
    """
    Returns a filtered DataFrame based on sidebar selections.
    Filters: day, smoker, bill range, sex.
    """
    df = tips.copy()
    if input.selected_day() != "All":
        df = df[df["day"] == input.selected_day()]
    if not input.show_smoker():
        df = df[df["smoker"] == "No"]
    bill_min, bill_max = input.bill_range()
    df = df[(df["total_bill"] >= bill_min) & (df["total_bill"] <= bill_max)]
    if input.selected_sex() != "All":
        df = df[df["sex"] == input.selected_sex()]
    return df

