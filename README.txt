<!-- ═══════════════════════════════════════════════════════ -->
<!--                    HERO SECTION                       -->
<!-- ═══════════════════════════════════════════════════════ -->

<div align="center">

# 📊 SALES PERFORMANCE DASHBOARD

### Turning Raw Sales Data Into Meaningful Business Insights.

A powerful, interactive business intelligence dashboard built with Python, Streamlit, Pandas and Plotly.

<br/>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />

<br/><br/>

**Explore. Analyze. Visualize. Decide.**

[Features](#-what-makes-it-special) • [Installation](#-get-started) • [Analytics](#-inside-the-dashboard) • [Team](#-the-people-behind-the-project)

</div>

---

## ⚡ The Idea

Raw sales data is just numbers until you know what those numbers mean.

The **Sales Performance Dashboard** transforms ordinary CSV datasets into an interactive analytical experience. It helps users understand revenue patterns, identify profitable categories, compare regional performance and monitor essential business metrics — all through a single interface.

Whether you're exploring sample data or uploading your own sales records, the dashboard makes data analysis accessible and intuitive.

---

## ✨ What Makes It Special?

<table>
<tr>
<td width="50%">

### 📈 KPI Intelligence

Monitor essential business metrics:

- Total Sales
- Total Profit
- Total Orders
- Profit Margin

</td>
<td width="50%">

### 📊 Interactive Analytics

Explore five dynamic visualizations powered by Plotly.

- Monthly Sales Trends
- Category Performance
- Customer Segments
- Regional Analysis
- Category-wise Profit

</td>
</tr>
<tr>
<td width="50%">

### 🔍 Smart Filtering

Take control of your analysis with:

- Date Range Selection
- Regional Filters
- Category Filters
- Dynamic Data Updates

</td>
<td width="50%">

### 📁 Flexible Data Handling

Work with your own data:

- CSV Upload
- Automatic Data Cleaning
- Column Validation
- Filtered CSV Export

</td>
</tr>
</table>

---

## 📸 Inside the Dashboard

### 01 — Business Overview
Monitor your business performance through four key indicators.

### 02 — Monthly Sales Analysis
Identify revenue trends and changes over time.

### 03 — Category & Segment Analysis
Understand which product categories and customer segments contribute to sales.

### 04 — Regional Performance
Compare business performance across different regions.

### 05 — Profitability Analysis
Discover which categories generate the highest profit.

<!-- Add your actual dashboard screenshots below -->

<div align="center">

*Dashboard screenshots coming soon.*

</div>

---

## 📊 Demo Analytics

The application includes a built-in synthetic dataset containing 100 sample orders.

<div align="center">

| METRIC | DEMO VALUE |
|:---:|:---:|
| 💰 Total Sales | **$143,150** |
| 📈 Total Profit | **$27,350** |
| 📦 Total Orders | **100** |
| 🎯 Profit Margin | **19.11%** |

</div>

### 🔎 Interesting Discoveries

- 🥇 Furniture leads in total sales.
- 💹 Technology generates the highest profit.
- 🌍 Central is the highest-performing region.
- 📅 June 2022 records the highest monthly sales.

> These values are generated from synthetic demonstration data. Actual results depend on the uploaded dataset.

---

## 🛠️ Technology Behind the Project

| Technology | Role |
|:---|:---|
| Python 3 | Application logic |
| Streamlit | Interactive dashboard interface |
| Pandas | Data cleaning and manipulation |
| Plotly Express | Interactive charts |
| Custom CSS | UI styling and light theme |

---

## 🚀 Get Started

Ready to explore your sales data? Follow these steps.

### 1. Clone the Repository

```bash
git clone https://github.com/anirban-bhowmik-coder/Sales-Performance-Dashboard.git
```

### 2. Enter the Project Directory

```bash
cd Sales-Performance-Dashboard
```

### 3. Install Dependencies

```bash
pip install streamlit pandas plotly
```

### 4. Check the Project Structure

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

<details>
<summary><b>🎨 Important: Streamlit Theme Configuration</b></summary>

Keep the `.streamlit` directory in the same location as your Python application.

The `config.toml` file forces the light theme, ensuring consistent styling and a readable data table.

Do not remove this folder if you want to preserve the intended interface appearance.

</details>

### 5. Launch the Dashboard

```bash
streamlit run Sales_Performance_Dashboard.py
```

That's it! Your dashboard will open in your browser.

---

## 📂 Dataset Format

Your uploaded CSV should contain these required columns:

| Column | Purpose |
|:---|:---|
| `Order ID` | Unique order identification |
| `Order Date` | Transaction date |
| `Sales` | Revenue generated |
| `Profit` | Profit earned |
| `Category` | Product classification |
| `Region` | Geographical region |
| `Segment` | Customer segment |

The application performs header normalization, date parsing, numeric conversion and missing-value handling.

---

## 🧠 Under the Hood

The dashboard follows a simple five-stage analytical pipeline:

<div align="center">

**01. INPUT**  
Upload CSV or use demo data

⬇️

**02. CLEAN**  
Normalize, validate and prepare data

⬇️

**03. FILTER**  
Apply date, region and category filters

⬇️

**04. ANALYZE**  
Calculate KPIs and aggregate results

⬇️

**05. VISUALIZE**  
Display charts, tables and exportable records

</div>

---

## 🔮 What's Next?

The project can be extended with:

- [ ] Machine Learning-based sales forecasting.
- [ ] Year-over-year performance comparisons.
- [ ] Customizable dataset column mapping.
- [ ] Advanced business intelligence metrics.
- [ ] User authentication and saved sessions.

---

## 👥 The People Behind the Project

**A collaborative group project in Business Intelligence and Sales Analytics.**

| Contributor | Enrolment ID |
|:---|:---|
| Yash Jain | 25SCS1003000621 |
| Jahnvi Verma | 25SCS1003005395 |
| Tanishq Ahuja | 25SCS1003000590 |
| **Anirban Bhowmik** | **25SCS1003005398** |
| Vansh Dhangar | 25SCS1003002263 |

---

<div align="center">

## ⭐ If you find this project interesting, give it a star!

**Built with Python. Powered by Data. Driven by Insights.**

<br/>

<img src="https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python" />
<img src="https://img.shields.io/badge/Powered%20by-Streamlit-FF4B4B?style=flat-square&logo=streamlit" />

</div>
