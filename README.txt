# 📊 Sales Performance Dashboard
### Transforming Raw Sales Data into Actionable Business Insights

An interactive **Sales Analytics & Business Intelligence Dashboard** built with Python, Streamlit, Pandas, and Plotly. Upload sales datasets, monitor key performance indicators, explore interactive visualizations, and uncover meaningful business insights through a clean and intuitive interface.

---

## ✨ Overview

The Sales Performance Dashboard simplifies sales data analysis by converting raw CSV files into meaningful visual insights.

Whether you're analyzing revenue trends, comparing regional performance, or identifying profitable product categories, this dashboard provides an interactive environment to explore your business data.

**No manual calculations. No complicated spreadsheets. Just actionable insights.**

## 🚀 Key Features

| Feature | Description |
|---|---|
| 📁 CSV Upload | Upload your own sales dataset. |
| 📈 KPI Monitoring | Track total sales, profit, orders, and profit margin. |
| 📊 Interactive Charts | Explore five interactive Plotly visualizations. |
| 🔍 Dynamic Filters | Filter records by date, region, and category. |
| 🧹 Data Cleaning | Automatically handles headers, dates, currency values, and missing data. |
| 📋 Data Explorer | View filtered sales records in an interactive table. |
| 📥 CSV Export | Download filtered datasets for further analysis. |
| 💡 Demo Mode | Explore the dashboard using built-in sample data. |
| 🎨 Custom UI | Clean interface with consistent styling and a light theme. |

## 📊 Dashboard Visualizations

The dashboard provides five visual perspectives:

1. **Monthly Sales Trend** – Understand revenue patterns over time.
2. **Category-wise Sales** – Compare sales across product categories.
3. **Sales by Segment** – Analyze customer segment contributions.
4. **Regional Sales Performance** – Compare sales across geographical regions.
5. **Profit by Category** – Identify the most profitable product categories.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Data processing and analysis |
| Plotly Express | Interactive data visualizations |
| Custom CSS | Interface styling and presentation |

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/anirban-bhowmik-coder/Sales-Performance-Dashboard.git
```

### 2. Navigate to the Project Directory

```bash
cd Sales-Performance-Dashboard
```

### 3. Install Dependencies

```bash
pip install streamlit pandas plotly
```

### 4. Verify Project Structure

Make sure your project files are arranged as follows:

```text
Sales-Performance-Dashboard/
│
├── .streamlit/
│   └── config.toml
│
├── Sales_Performance_Dashboard.py
├── Stock_Market_Practice_Dataset.csv
└── README.md
```

> **Important:** Keep the `.streamlit` folder in the same directory as the Python application. Its `config.toml` configuration forces the light theme, ensuring that the dashboard and data table remain readable.

### 5. Run the Dashboard

```bash
streamlit run Sales_Performance_Dashboard.py
```

The application will open automatically in your default browser.

## 📂 Dataset Requirements

To upload a custom dataset, provide a CSV file containing these seven required columns:

| Column | Description |
|---|---|
| Order ID | Unique order identifier |
| Order Date | Date of the transaction |
| Sales | Revenue generated |
| Profit | Profit earned |
| Category | Product category |
| Region | Sales region |
| Segment | Customer segment |

The application automatically normalizes column headers, parses dates, converts numeric values, and handles missing records.

## 📌 Sample Dashboard Insights

The built-in demo dataset contains 100 synthetic orders.

| KPI | Demo Result |
|---|---:|
| Total Sales | $143,150 |
| Total Profit | $27,350 |
| Total Orders | 100 |
| Profit Margin | 19.11% |

**Key Observations:**
- Furniture generates the highest sales revenue.
- Technology delivers the highest profit.
- Central is the leading sales region.
- June 2022 records the highest monthly sales.

*Note: These results are based on synthetic demonstration data, not actual business transactions.*

## 🔮 Future Enhancements

- Sales forecasting using Machine Learning.
- Year-over-year and month-over-month comparisons.
- Configurable dataset column mapping.
- User authentication and saved sessions.
- Advanced business intelligence metrics.

## 👥 Project Contributors

**Group Project – Business Intelligence and Sales Analytics**

| Contributor | Enrolment ID |
|---|---|
| Yash Jain | 25SCS1003000621 |
| Jahnvi Verma | 25SCS1003005395 |
| Tanishq Ahuja | 25SCS1003000590 |
| Anirban Bhowmik | 25SCS1003005398 |
| Vansh Dhangar | 25SCS1003002263 |

## 🎯 Project Objective

To demonstrate how Python-based data analytics and visualization tools can transform raw datasets into interactive business intelligence solutions, supporting better decision-making through data-driven insights.

---

<div align="center">

### ⭐ If you find this project interesting, consider giving it a star!

**Built with ❤️ using Python & Streamlit**

</div>
