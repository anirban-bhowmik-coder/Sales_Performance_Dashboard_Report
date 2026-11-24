
import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# 2. PROFESSIONAL WHITE THEME - CSS FIX
# ==========================================


st.markdown("""
<style>

/* ---------- FORCE LIGHT SCHEME ---------- */
:root { color-scheme: light !important; }

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background: #F4F7FB !important;
    color: #17243A !important;
}

/* TOP HEADER BAR (was dark) */
[data-testid="stHeader"],
[data-testid="stToolbar"] {
    background: #F4F7FB !important;
}
[data-testid="stHeader"] *,
[data-testid="stToolbar"] * {
    color: #17243A !important;
}

/* ALL TEXT */
h1, h2, h3, h4, h5, h6, p, label, span, li, div,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] * {
    color: #17243A;
}
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] * {
    color: #4A5B73 !important;
    opacity: 1 !important;
}

/* SIDEBAR */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div {
    background: #FFFFFF !important;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] small {
    color: #17243A !important;
}

/* INPUT WRAPPERS: these inner divs carry the dark background in dark mode */
[data-testid="stDateInput"] div,
[data-testid="stDateInputField"],
[data-testid="stMultiSelect"] div,
[data-testid="stSelectbox"] div {
    background: #FFFFFF !important;
}

[data-testid="stDateInput"] div,
[data-testid="stMultiSelect"] div,
[data-testid="stSelectbox"] div {
    border-color: #AABBD0 !important;
}

/* date segments (yyyy/mm/dd) + placeholders + icons */
[data-testid="stDateInputField"],
[data-testid="stDateInputField"] *,
[data-testid="stMultiSelect"] input,
[data-testid="stSelectbox"] input,
[data-testid="stSelectbox"] [data-baseweb="select"] div {
    color: #17243A !important;
    -webkit-text-fill-color: #17243A !important;
    opacity: 1 !important;
}
[data-testid="stMultiSelect"] svg,
[data-testid="stSelectbox"] svg {
    fill: #174B91 !important;
    color: #174B91 !important;
    opacity: 1 !important;
}

/* DATE INPUT (box + text) */
[data-testid="stDateInput"] > div,
[data-testid="stDateInput"] [data-baseweb="input"],
[data-testid="stDateInput"] [data-baseweb="base-input"] {
    background: #FFFFFF !important;
    border-color: #AABBD0 !important;
    border-radius: 8px !important;
}
[data-testid="stDateInput"] input {
    background: #FFFFFF !important;
    color: #17243A !important;
    -webkit-text-fill-color: #17243A !important;
    font-weight: 600 !important;
}
[data-testid="stDateInput"] svg {
    fill: #174B91 !important;
    color: #174B91 !important;
}

/* CALENDAR POPUP */
[data-baseweb="calendar"],
[data-baseweb="calendar"] > div,
[data-baseweb="datepicker"] {
    background: #FFFFFF !important;
}
[data-baseweb="calendar"] * {
    color: #17243A !important;
    -webkit-text-fill-color: #17243A !important;
}
[data-baseweb="calendar"] svg { fill: #17243A !important; }
[data-baseweb="calendar"] button { background: transparent !important; }
[data-baseweb="calendar"] [role="gridcell"] [aria-selected="true"],
[data-baseweb="calendar"] [role="gridcell"] [aria-selected="true"] * {
    background: #2868C7 !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}
[data-baseweb="calendar"] [aria-disabled="true"],
[data-baseweb="calendar"] [aria-disabled="true"] * {
    color: #9AA8BC !important;
    -webkit-text-fill-color: #9AA8BC !important;
}

/* SELECT / MULTISELECT BOX */
[data-baseweb="select"],
[data-baseweb="select"] > div,
[data-baseweb="select"] [data-baseweb="input"] {
    background: #FFFFFF !important;
    border-color: #AABBD0 !important;
}
[data-baseweb="select"] input,
[data-baseweb="select"] div,
[data-baseweb="select"] span {
    color: #17243A !important;
    -webkit-text-fill-color: #17243A !important;
}
[data-baseweb="select"] svg {
    fill: #174B91 !important;
    color: #174B91 !important;
}

/* DROPDOWN OPTION LIST */
[data-baseweb="popover"],
[data-baseweb="popover"] > div,
[data-baseweb="menu"],
[role="listbox"],
[role="listbox"] ul {
    background: #FFFFFF !important;
}
[role="option"],
[role="option"] * {
    background: #FFFFFF !important;
    color: #17243A !important;
    -webkit-text-fill-color: #17243A !important;
}
[role="option"]:hover,
[role="option"]:hover *,
[role="option"][aria-selected="true"],
[role="option"][aria-selected="true"] * {
    background: #E5EEFF !important;
    color: #174B91 !important;
    -webkit-text-fill-color: #174B91 !important;
}

/* SELECTED FILTER TAGS (were red / dark-on-blue) - old + new Streamlit markup */
[data-baseweb="tag"],
[data-testid="stMultiSelectTagsContainer"] span {
    background: #DCEAFF !important;
}
[data-baseweb="tag"] *,
[data-baseweb="tag"] span,
[data-testid="stMultiSelectTagsContainer"] span,
[data-testid="stMultiSelectTagsContainer"] span * {
    color: #174B91 !important;
    -webkit-text-fill-color: #174B91 !important;
}
[data-baseweb="tag"] svg,
[data-testid="stMultiSelectTagsContainer"] svg {
    fill: #174B91 !important;
    color: #174B91 !important;
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] section {
    background: #FFFFFF !important;
    border: 1px dashed #9BB2D0 !important;
}
[data-testid="stFileUploader"] section *,
[data-testid="stFileUploaderFile"] * {
    color: #17243A !important;
}

/* BUTTONS (kept AFTER the generic rules so white text wins) */
.stButton button,
.stDownloadButton button,
[data-testid="stFileUploader"] button {
    background: #2868C7 !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}
.stButton button *,
.stDownloadButton button *,
[data-testid="stFileUploader"] button *,
[data-testid="stSidebar"] [data-testid="stFileUploader"] button span {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    fill: #FFFFFF !important;
}
.stButton button:hover,
.stDownloadButton button:hover,
[data-testid="stFileUploader"] button:hover {
    background: #174B91 !important;
}

/* KPI CARDS */
[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1px solid #DCE5F0 !important;
    border-radius: 12px !important;
    padding: 20px !important;
    box-shadow: 0 3px 12px rgba(20,40,70,0.06);
}
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] *,
[data-testid="stMetricValue"],
[data-testid="stMetricValue"] * {
    color: #17243A !important;
}

/* ALERTS: info / success / warning / error (all dark text on light bg) */
[data-testid="stAlert"],
[data-testid="stAlertContainer"] {
    border-radius: 10px !important;
}
[data-testid="stAlert"],
[data-testid="stAlertContainer"] {
    background: #E8F1FF !important;
    border: 1px solid #B8D0F5 !important;
}
[data-testid="stAlertContainer"] div {
    background: transparent !important;
}
[data-testid="stAlert"] *,
[data-testid="stAlertContainer"] * {
    color: #17365D !important;
    -webkit-text-fill-color: #17365D !important;
}

/* DATA TABLE (canvas based - theme is also set in .streamlit/config.toml) */
[data-testid="stDataFrame"] {
    background: #FFFFFF !important;
    border: 1px solid #DCE5F0 !important;
    border-radius: 10px !important;
}

/* TOOLTIPS */
[data-baseweb="tooltip"] *,
[data-testid="stTooltipContent"] {
    background: #17365D !important;
    color: #FFFFFF !important;
}

/* DIVIDERS */
hr { border-color: #DCE5F0 !important; }

</style>
""", unsafe_allow_html=True)



# ==========================================
# 3. PROJECT HEADER
# ==========================================

st.title("📊 Sales Performance Dashboard")

st.markdown(
    "### Business Intelligence and Sales Analytics"
)

st.markdown("""
**GROUP PROJECT | DEVELOPED BY**

- Yash Jain (25SCS1003000621)
- Jahnvi Verma (25SCS1003005395)
- Tanishq Ahuja (25SCS1003000590)
- Anirban Bhowmik (25SCS1003005398)
- Vansh Dhangar (25SCS1003002263)
""")

st.divider()


# ==========================================
# 4. DATASET UPLOAD
# ==========================================

st.sidebar.title("Dashboard Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload Sales Dataset (CSV)",
    type=["csv"]
)


@st.cache_data
def load_csv(file):
    return pd.read_csv(file)


@st.cache_data
def create_demo_data():

    data = {
        "Order ID": [
            f"ORD-{i:04d}" for i in range(1, 101)
        ],

        "Order Date": pd.date_range(
            start="2021-01-01",
            periods=100,
            freq="10D"
        ),

        "Sales": [
            500 + (i * 37) % 2000
            for i in range(100)
        ],

        "Profit": [
            80 + (i * 17) % 400
            for i in range(100)
        ],

        "Category": [
            ["Furniture", "Technology", "Office Supplies"][i % 3]
            for i in range(100)
        ],

        "Region": [
            ["East", "West", "Central", "South"][i % 4]
            for i in range(100)
        ],

        "Segment": [
            ["Consumer", "Corporate", "Home Office"][i % 3]
            for i in range(100)
        ]
    }

    return pd.DataFrame(data)


if uploaded_file:

    try:
        df = load_csv(uploaded_file)
        st.sidebar.success("Dataset uploaded successfully!")

    except Exception as e:
        st.error(f"Unable to read CSV: {e}")
        st.stop()

else:

    df = create_demo_data()

    st.info(
        "Demo mode is active. Upload your original sales CSV "
        "to analyse actual sales data."
    )


# ==========================================
# 5. DATA CLEANING
# ==========================================

df.columns = df.columns.str.strip()

column_lookup = {
    col.lower().strip(): col
    for col in df.columns
}


def find_column(name):
    return column_lookup.get(name.lower())


required_columns = [
    "Order Date",
    "Sales",
    "Profit",
    "Order ID",
    "Category",
    "Region",
    "Segment"
]

missing = [
    name for name in required_columns
    if find_column(name) is None
]

if missing:

    st.error(
        "Required columns are missing: "
        + ", ".join(missing)
    )

    st.write("Available columns:", list(df.columns))
    st.stop()


df = df.rename(
    columns={
        find_column(name): name
        for name in required_columns
    }
)

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

for col in ["Sales", "Profit"]:

    df[col] = pd.to_numeric(
        df[col].astype(str).str.replace(
            r"[$,]", "", regex=True
        ),
        errors="coerce"
    )

df = df.dropna(
    subset=[
        "Order Date",
        "Sales",
        "Profit",
        "Order ID"
    ]
)

if df.empty:
    st.error("No valid records found.")
    st.stop()


# ==========================================
# 6. SIDEBAR FILTERS
# ==========================================

st.sidebar.subheader("Apply Filters")

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

regions = sorted(
    df["Region"].dropna().unique()
)

selected_regions = st.sidebar.multiselect(
    "Select Region",
    regions,
    default=regions
)

categories = sorted(
    df["Category"].dropna().unique()
)

selected_categories = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)


# ==========================================
# 7. FILTER DATA
# ==========================================

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:

    start_date, end_date = date_range

else:

    start_date, end_date = min_date, max_date


filtered_df = df[
    (df["Order Date"].dt.date >= start_date) &
    (df["Order Date"].dt.date <= end_date) &
    (df["Region"].isin(selected_regions)) &
    (df["Category"].isin(selected_categories))
].copy()


# ==========================================
# 8. KPI CALCULATIONS
# ==========================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = filtered_df["Order ID"].nunique()

profit_margin = (
    (total_profit / total_sales) * 100
    if total_sales != 0 else 0
)


st.subheader("Key Performance Indicators")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)

c2.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

c3.metric(
    "Total Orders",
    f"{total_orders:,}"
)

c4.metric(
    "Profit Margin",
    f"{profit_margin:.2f}%"
)

st.divider()


if filtered_df.empty:

    st.warning("No records match the selected filters.")
    st.stop()



# ==========================================
# PROFESSIONAL PLOTLY CHART STYLING
# ==========================================

def style_chart(fig):

    fig.update_layout(
        template="plotly_white",

        font=dict(
            family="Arial",
            size=14,
            color="#17243A"
        ),

        title=dict(
            font=dict(
                size=21,
                color="#17365D"
            )
        ),

        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",

        colorway=["#2868C7", "#D9480F", "#0B8A6A", "#7B3FC4", "#B7791F"],

        legend=dict(
            font=dict(
                size=13,
                color="#17243A"
            ),
            bgcolor="#FFFFFF"
        ),

        margin=dict(
            l=65,
            r=35,
            t=75,
            b=65
        ),

        hoverlabel=dict(
            bgcolor="#17365D",
            font=dict(
                color="#FFFFFF",
                size=13
            )
        )
    )

    # X-axis labels and numbers
    fig.update_xaxes(
        color="#17243A",
        tickfont=dict(
            color="#17243A",
            size=13
        ),
        title_font=dict(
            color="#17365D",
            size=15
        ),
        showgrid=False,
        zerolinecolor="#CBD5E1",
        linecolor="#64748B"
    )

    # Y-axis labels and numbers
    fig.update_yaxes(
        color="#17243A",
        tickfont=dict(
            color="#17243A",
            size=13
        ),
        title_font=dict(
            color="#17365D",
            size=15
        ),
        gridcolor="#E2E8F0",
        gridwidth=1,
        zerolinecolor="#94A3B8",
        linecolor="#64748B"
    )

    return fig



# ==========================================
# 9. SALES TREND ANALYSIS
# ==========================================

st.subheader("📈 Sales Trend Analysis")

filtered_df["Month"] = (
    filtered_df["Order Date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_sales = (
    filtered_df
    .groupby("Month", as_index=False)["Sales"]
    .sum()
)

fig1 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend",
    template="plotly_white"
)

fig1.update_traces(
    line_color="#2868C7",
    line_width=3
)

fig1.update_layout(
    font_color="#17243A",
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF"
)

fig1 = style_chart(fig1)

st.plotly_chart(
    fig1,
    use_container_width=True,
    theme=None
)


# ==========================================
# 10. SALES BY CATEGORY
# ==========================================

st.subheader("📦 Sales by Category")

category_sales = (
    filtered_df
    .groupby("Category", as_index=False)["Sales"]
    .sum()
)

fig2 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="Category-wise Sales",
    template="plotly_white"
)

fig2.update_layout(
    font_color="#17243A",
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF"
)

fig2 = style_chart(fig2)

st.plotly_chart(
    fig2,
    use_container_width=True,
    theme=None
)


# ==========================================
# 11. SALES BY CUSTOMER SEGMENT
# ==========================================

st.subheader("👥 Sales by Customer Segment")

segment_sales = (
    filtered_df
    .groupby("Segment", as_index=False)["Sales"]
    .sum()
)

fig3 = px.pie(
    segment_sales,
    names="Segment",
    values="Sales",
    hole=0.45,
    title="Sales Distribution by Segment"
)

fig3.update_layout(
    template="plotly_white",
    font_color="#17243A",
    paper_bgcolor="#FFFFFF"
)

fig3.update_traces(
    textinfo="percent",
    textfont=dict(size=16, color="#FFFFFF"),
    insidetextfont=dict(size=16, color="#FFFFFF")
)

fig3 = style_chart(fig3)

st.plotly_chart(
    fig3,
    use_container_width=True,
    theme=None
)


# ==========================================
# 12. SALES BY REGION
# ==========================================

st.subheader("🌍 Sales by Region")

region_sales = (
    filtered_df
    .groupby("Region", as_index=False)["Sales"]
    .sum()
)

fig4 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    color="Region",
    title="Regional Sales Performance",
    template="plotly_white"
)

fig4.update_layout(
    font_color="#17243A",
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF"
)

fig4 = style_chart(fig4)

st.plotly_chart(
    fig4,
    use_container_width=True,
    theme=None
)


# ==========================================
# 13. PROFIT ANALYSIS
# ==========================================

st.subheader("💰 Profit Analysis")

profit_category = (
    filtered_df
    .groupby("Category", as_index=False)["Profit"]
    .sum()
)

fig5 = px.bar(
    profit_category,
    x="Category",
    y="Profit",
    color="Category",
    title="Profit by Category",
    template="plotly_white"
)

fig5.update_layout(
    font_color="#17243A",
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF"
)

fig5 = style_chart(fig5)

st.plotly_chart(
    fig5,
    use_container_width=True,
    theme=None
)


# ==========================================
# 14. DATA TABLE
# ==========================================

st.subheader("📋 Sales Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


# ==========================================
# 15. DOWNLOAD FILTERED DATA
# ==========================================

csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Sales Data",
    data=csv_data,
    file_name="Filtered_Sales_Data.csv",
    mime="text/csv"
)


# ==========================================
# 16. PROJECT INFORMATION
# ==========================================

st.divider()

st.subheader("About This Project")

st.write("""
The Sales Performance Dashboard is a Python-based
Business Intelligence project designed to analyse sales,
profit, customer segments and regional performance.

It uses Pandas for data processing, Plotly for interactive
visualizations and Streamlit for the dashboard interface.
""")

st.markdown("### Project Developed By")

members = [
    ("Yash Jain", "25SCS1003000621"),
    ("Jahnvi Verma", "25SCS1003005395"),
    ("Tanishq Ahuja", "25SCS1003000590"),
    ("Anirban Bhowmik", "25SCS1003005398"),
    ("Vansh Dhangar", "25SCS1003002263")
]

for name, student_id in members:

    st.write(
        f"- **{name}** — {student_id}"
    )

st.caption(
    "Sales Performance Dashboard | Python Group Project"
)
