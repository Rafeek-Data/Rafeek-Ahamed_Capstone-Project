* **Prepared By: Rafeek Ahamed**
* **Project Title: Singapore HDB Resale Market Analysis to Improve Sales Performance**

<p align="center">
<img width="1264" height="843" alt="image" src="https://github.com/user-attachments/assets/4f3f5c5c-af16-42f1-8f9c-74d46b66ce0d" />
</p>


<h1 align="center">Singapore HDB Resale Market Analysis to Improve Sales Performance

This repository contains a transactional dataset of HDB resale flat sales in Singapore from January 2000 to January 2024. It has about 628,000 records across five CSV files. Each record gives the sale month, town, flat type, block and street, storey range, floor area, flat model, lease start year and resale price.

The data is a good resource for exploratory data analysis (EDA), price trend analysis, regional market comparison, and property price prediction with models such as Linear Regression and Random Forest. It also suits data cleaning practice, because the files have a missing header in one copy, remaining lease in different formats, duplicate rows and extreme outliers. A final use is flagging flats that sold below their predicted market value.

<img width="970" height="602" alt="image" src="https://github.com/user-attachments/assets/b2dc6990-c772-44cb-a2f0-ec25c5ebb187" />



5 Project Objectives

1. Analyse Historical Property Price Trends
>> The median resale price rose from about S$239,000 in 2000 to S$550,000 in 2023, up 130%. The rise was uneven. Prices fell from a 2013 peak of S$455,000 to S$400,000 in 2019. They then rebounded 38% by 2023.


2. Identify Key Factors Affecting Property Prices
>> Location, flat type and size, and storey all matter. Queenstown, Central Area and Bukit Merah cost about 55% more per sqm than Jurong West, Woodlands and Choa Chu Kang. Flats on storey 20 or higher cost about 61% more per sqm than storeys 1–5, though part of that gap is location. In my quick Random Forest, floor area was the strongest factor, followed by storey, flat type and remaining lease. Remaining lease has no clear link to price on its own, because location and flat model hide it.


3. Develop a Property Price Prediction Model
>> I trained both models on 2012–2021 sales and tested them on 2022 onward. Random Forest was clearly better, with an R² of 0.75 and an average error of about S$65,000 (roughly 11%). Linear Regression reached only 0.43 and about S$112,000. Both runs were quick and untuned, so improve them before you report final accuracy.


4. Identify Potentially Undervalued Properties
>> About 0.9% of the 2022+ test sales (493 flats) sold more than 10% below the model’s prediction. They cluster in Bukit Merah, Jurong West, Jurong East and Geylang. Treat these as candidates for a closer look, not proven bargains, because the data has no flat condition, renovation or MRT distance.


5. Provide Data Driven Recommendations
>> 1. Buyers: compare a 4-room flat in a cheaper town against a 3-room in a better one, and weigh the storey premium against size.
>> 2. Investors: stress-test for flat price periods like 2014–2019, and don’t judge value by remaining lease alone.
>> 3. Agents: price by town, flat type and storey instead of using island-wide medians.
>>
>>    
## 📋 Dataset Overview

* **File Name:** `hdb_resale_clean.csv`
* **Time Horizon:** 2000 – 2017
* **Target Category:** Resales flats
* **Key Entities:** Products, Sales Team, Regional Markets, Revenue Metrics

  Link to Jupyter Notebook in Google Colab:
https://colab.research.google.com/drive/1Xb8K_tEherJ-0tqqgWMoK7jebAOUNs_I#scrollTo=QGMKX71DsLUe
   
## 🗂️ Data Dictionary

The dataset consists of the following 10 features:

|S.No | Feature | Type | Description | Example | Unique Values |
| :--- | :--- | :--- | :--- | :--- | :--- |
|1| **Month** | Text, date (YYYY-MM) | Month the resale was recorded. Approval date in 2000–Feb 2012, registration date from Mar 2012. | `2017-01` | 289 |
|2| **Town** | Categorical | HDB town where the flat is located. | `ANG MO KIO` | 26|
|3| **Flat_Type** | Categorical | Number of rooms: 1 ROOM, 2 ROOM, 3 ROOM, 4 ROOM, 5 ROOM, EXECUTIVE or MULTI-GENERATION. | `2 ROOM` | 7|
|4| **Block** | Text | Block number. It is text because some values have letters, such as 123A. | `406` | 2,700|
|5| **Street_Name** | Text | Street address of the block. |  `ANG MO KIO AVE 10` | 573|
|6| **Story_range** | Categorical | Band of floors the flat is on. The band width differs between periods. |10 TO 12|25|
|7| **floor_area_sqm** | Numeric (float) | Size of the flat in square metres. | `44.0` |192|
|8| **flat_model** | Categorical | HDB design type, such as Improved, New Generation, DBSS or Premium Apartment. | `Improved` |21|
|9| **lease_commence_date** | Numeric (year) | Year the 99-year lease started. | `1979` |56|
|10| **resale_price** | Numeric (float), target | Sale price in Singapore dollars. | `232000.0` | 8,034|

## 🔍 Data Quality & Cleaning Notes

* **Different date bases:** the 2000–Feb 2012 files use approval date, and the files from Mar 2012 use registration date, so small timing differences exist at the join.
* **Partial final year:** 2024 contains January only (411 sales), so compare only full years.
* **Nominal prices:** prices are not adjusted for inflation.
* **Approximate lease:** remaining lease is accurate to the year, not the month.
* **Duplicates:** two real sales of identical flats at the same price in the same month would also have been removed, but this is rare.
  
Summary of changes
|Stage | Rows | 
| :--- | :--- | 
|Stage|	Rows|
|Raw (5 files combined)|	628,591|
|Duplicates removed|	−1,134|
|Invalid records removed|	−15|
|Clean dataset|	627,442|

## 🛠️ Usage Example (Python & Pandas)

Get started analyzing this dataset quickly using Python:

```import pandas as pd

BASE = "https://raw.githubusercontent.com/Rafeek-Data/Rafeek-Ahamed_Capstone-Project/refs/heads/main/"
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
    # some copies of the 2nd file have no header row, so check the first row
    if pd.read_csv(url, nrows=1).columns[0] == "month":
        return pd.read_csv(url)
    return pd.read_csv(url, header=None, names=COLS)

df = pd.concat([load(BASE + f) for f in files], ignore_index=True)
print(df.shape)
df.head()
