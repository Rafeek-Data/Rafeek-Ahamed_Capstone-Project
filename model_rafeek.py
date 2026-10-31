import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Safe check: Recreate the variables if the kernel was restarted and they are missing
if 'model' not in globals() or 'X' not in globals() or 'sample_df' not in globals():
    print("Variables not found in memory. Reconstructing data and retraining model...")
    
    # 1. Load clean dataset if it isn't in memory
    if 'clean' not in globals():
        import os
        if os.path.exists("hdb_resale_clean.csv"):
            clean = pd.read_csv("hdb_resale_clean.csv")
        else:
            # Fallback load and tidy
            BASE = "https://raw.githubusercontent.com/Rafeek-Data/Rafeek-Ahamed_Capstone-Project/refs/heads/main/"
            FILES = ["resale-flat-prices-based-on-approval-date-2000-feb-2012_1.csv",
                     "resale-flat-prices-based-on-approval-date-2000-feb-2012_2.csv",
                     "resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv",
                     "resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv",
                     "resale-flat-prices-based-on-registration-date-from-Jan-2017-onwards.csv"]
            COLS = ["month", "town", "flat_type", "block", "street_name", "storey_range",
                    "floor_area_sqm", "flat_model", "lease_commence_date", "resale_price"]
            def load(url):
                head = pd.read_csv(url, nrows=1)
                d = pd.read_csv(url) if head.columns[0] == "month" else pd.read_csv(url, header=None, names=COLS)
                return d[COLS]
            clean = pd.concat([load(BASE + f) for f in FILES], ignore_index=True).drop_duplicates()
            clean["month"] = pd.to_datetime(clean["month"], format="%Y-%m")
            clean["year"] = clean["month"].dt.year
            for c in ["town", "flat_type", "flat_model"]:
                clean[c] = clean[c].astype(str).str.strip().str.upper()
            clean["flat_type"] = clean["flat_type"].str.replace("MULTI GENERATION", "MULTI-GENERATION")
            st = clean["storey_range"].str.extract(r"(\d+)\s*TO\s*(\d+)").astype(float)
            clean["storey_mid"] = (st[0] + st[1]) / 2
            clean["price_per_sqm"] = clean["resale_price"] / clean["floor_area_sqm"]
            clean["remaining_lease_yrs"] = 99 - (clean["year"] - clean["lease_commence_date"])
            clean = clean[clean["remaining_lease_yrs"].between(0, 99)].reset_index(drop=True)

    # 2. Sample and prepare features
    sample_df = clean.sample(50000, random_state=42).copy()
    X = pd.DataFrame({
        'floor_area_sqm': sample_df['floor_area_sqm'].astype(float),
        'storey_mid': sample_df['storey_mid'].fillna(sample_df['storey_mid'].median()).astype(float),
        'remaining_lease_yrs': sample_df['remaining_lease_yrs'].astype(float),
        'year': sample_df['year'].astype(float)
    })
    X = pd.concat([X, pd.get_dummies(sample_df[['town', 'flat_type']], drop_first=True)], axis=1)
    y = sample_df['resale_price'].astype(float)

    # 3. Fit Random Forest model
    model = RandomForestRegressor(n_estimators=50, max_depth=12, random_state=42, n_jobs=-1)
    model.fit(X, y)

# Save model and its training information
model_bundle = {
    "model": model,
    "feature_columns": X.columns.tolist(),
    "towns": sorted(sample_df["town"].dropna().unique().tolist()),
    "flat_types": sorted(sample_df["flat_type"].dropna().unique().tolist()),
    "storey_median": sample_df["storey_mid"].median()
}

# Export model
joblib.dump(model_bundle, "hdb_resale_model.pkl")

print("HDB Resale Model exported successfully to 'hdb_resale_model.pkl'!")
