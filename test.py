from feature_engineering import create_features

monthly = create_features(
    "data/Forecasting_Briefs_Jobs_Realistic_Dataset.xlsx"
)

print(monthly.head())

print(monthly.columns)
