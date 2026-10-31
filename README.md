# Singapore HDB Resale Market Analysis to Improve Sales Performance

* **Prepared By:** Rafeek Ahamed
* **Project Title:** Singapore HDB Resale Market Analysis to Improve Sales Performance
* **Google Colab Notebook:** [View Jupyter Notebook](https://colab.research.google.com/drive/1Xb8K_tEherJ-0tqqgWMoK7jebAOUNs_I#scrollTo=QGMKX71DsLUe)
* **Streamlit:** [https://noxious-corpse-5v5r6jvpwpjvcvx95-8501.app.github.dev/](https://rafeek-ahamedcapstone-project-007.streamlit.app/)

---

<p align="center">
<img width="1264" height="843" alt="Singapore HDB Resale Market Overview" src="https://github.com/user-attachments/assets/4f3f5c5c-af16-42f1-8f9c-74d46b66ce0d" />
</p>

## 📌 Project Overview

This repository contains a transactional dataset of HDB resale flat sales in Singapore from January 2000 to January 2024. It features approximately **628,000 records** across five CSV files. Each record provides details on the sale month, town, flat type, block and street, storey range, floor area, flat model, lease start year, and resale price.

The data is an excellent resource for:
* **Exploratory Data Analysis (EDA)** and price trend evaluations.
* **Regional market comparisons** and property price predictions using models such as Linear Regression and Random Forest.
* **Data cleaning practice**, addressing challenges such as missing headers, mismatched remaining lease formats, duplicate rows, and extreme outliers.
* **Identifying undervalued opportunities**, specifically flagging flats sold below their predicted market value.

<p align="center">
<img width="1247" height="678" alt="image" src="https://github.com/user-attachments/assets/1b49b0d0-576e-4854-be3a-d716ff1e7e0f" />


</p>

---

## 🎯 Project Objectives & Key Findings

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/fceaa91c-815f-4541-ab43-dd1b95dcb003" />



### 1. Analyse Historical Property Price Trends
* **Finding:** The median resale price rose from about S$239,000 in 2000 to S$550,000 in 2023, up **130%**. Prices fell from a 2013 peak of S$455,000 to S$400,000 in 2019, before rebounding by **38% through 2023**.

### 2. Identify Key Factors Affecting Property Prices
* **Finding:** Location, flat type, size, and storey play major roles. Prime locations like Queenstown, Central Area, and Bukit Merah cost about **55% more per sqm** than Jurong West, Woodlands, and Choa Chu Kang.
* Flats on storey 20 or higher cost about **61% more per sqm** than storeys 1–5.
* In a Random Forest model, **floor area** was the strongest factor, followed by storey, flat type, and remaining lease.

### 3. Develop a Property Price Prediction Model
* **Finding:** Models were trained on 2012–2021 data and tested on 2022 onward. 
* **Random Forest** outperformed Linear Regression with an **$R^2$ of 0.75** and an average error of about **S$65,000 (~11%)**. 
* **Linear Regression** reached an $R^2$ of 0.43 with an average error of **S$112,000**.

### 4. Identify Potentially Undervalued Properties
* **Finding:** About **0.9%** of the 2022+ test sales (493 flats) sold more than 10% below the model’s prediction. These cluster in **Bukit Merah, Jurong West, Jurong East, and Geylang**.

### 5. Provide Data-Driven Recommendations
* **Buyers:** Compare a 4-room flat in a cheaper town against a 3-room in a better one, and weigh the storey premium against size.
* **Investors:** Stress-test for flat price periods like 2014–2019, and do not judge value by remaining lease alone.
* **Agents:** Price by town, flat type, and storey instead of using island-wide medians.

---

## 📋 Dataset Overview

* **File Name:** `hdb_resale_clean.csv`
* **Time Horizon:** 2000 – 2024
* **Target Category:** Resale flats
* **Key Entities:** Products, Sales Team, Regional Markets, Revenue Metrics

---

## 🗂️ Data Dictionary

The dataset consists of the following 10 features:

| S.No | Feature | Type | Description | Example | Unique Values |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Month** | Text, date (YYYY-MM) | Month the resale was recorded. Approval date in 2000–Feb 2012, registration date from Mar 2012. | `2017-01` | 289 |
| 2 | **Town** | Categorical | HDB town where the flat is located. | `ANG MO KIO` | 26 |
| 3 | **Flat_Type** | Categorical | Number of rooms: 1 ROOM, 2 ROOM, 3 ROOM, 4 ROOM, 5 ROOM, EXECUTIVE or MULTI-GENERATION. | `2 ROOM` | 7 |
| 4 | **Block** | Text | Block number (stored as text for letters like 123A). | `406` | 2,700 |
| 5 | **Street_Name** | Text | Street address of the block. | `ANG MO KIO AVE 10` | 573 |
| 6 | **Story_range** | Categorical | Band of floors the flat is on. | `10 TO 12` | 25 |
| 7 | **floor_area_sqm** | Numeric (float) | Size of the flat in square metres. | `44.0` | 192 |
| 8 | **flat_model** | Categorical | HDB design type (e.g., Improved, New Generation, DBSS, Premium Apartment). | `Improved` | 21 |
| 9 | **lease_commence_date** | Numeric (year) | Year the 99-year lease started. | `1979` | 56 |
| 10 | **resale_price** | Numeric (float), target | Sale price in Singapore dollars. | `232000.0` | 8,034 |

---

## 🔍 Data Quality & Cleaning Notes

* **Different date bases:** 2000–Feb 2012 files use approval date; Mar 2012 onward uses registration date.
* **Partial final year:** 2024 contains January only (411 sales).
* **Nominal prices:** Prices are not adjusted for inflation.
* **Approximate lease:** Remaining lease is accurate to the year, not the month.

### Summary of Changes

| Stage | Rows |
| :--- | :--- |
| **Raw (5 files combined)** | 628,591 |
| **Duplicates removed** | −1,134 |
| **Invalid records removed** | −15 |
| **Clean dataset** | **627,442** |

---

## 🛠️ Usage Example (Python & Pandas)

Get started analyzing this dataset quickly using Python:

```python
import pandas as pd

BASE = "[https://raw.githubusercontent.com/Rafeek-Data/Rafeek-Ahamed_Capstone-Project/refs/heads/main/](https://raw.githubusercontent.com/Rafeek-Data/Rafeek-Ahamed_Capstone-Project/refs/heads/main/)"
COLS = ["month", "town", "flat_type", "block", "street_name", "storey_range",
        "floor_area_sqm", "flat_model", "lease_commence_date", "resale_price"]

files = [
    "resale-flat-prices-based-on-approval-date-2000-feb-2012_1.csv",
    "resale-flat-prices-based-on-approval-date-2000-feb-2012_2.csv",
    "resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv",
    "resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv",
    "resale-flat-prices-based-on-registration-date-from-Jan-2017-onwards.csv",
]

def load(url):
    # Some copies of the 2nd file have no header row, so check the first row
    if pd.read_csv(url, nrows=1).columns[0] == "month":
        return pd.read_csv(url)
    return pd.read_csv(url, header=None, names=COLS)

df = pd.concat([load(BASE + f) for f in files], ignore_index=True)
print(df.shape)
df.head()
