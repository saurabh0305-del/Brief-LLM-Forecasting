import pandas as pd
import numpy as np

def load_data(path):

    df = pd.read_excel(path)

    df["Brief Requested Date"] = pd.to_datetime(
        df["Brief Requested Date"]
    )

    return df

def prepare_monthly(df):

    monthly = (
        df.groupby(
            [
                pd.Grouper(
                    key="Brief Requested Date",
                    freq="MS"
                ),
                "Region"
            ]
        )
        .agg(
            Revenue=("Revenue (USD)", "sum"),
            Briefs=("Brief ID", "nunique"),
            Jobs=("Job ID", "count"),
            AvgJobPrice=("Job Price (USD)", "mean"),
            AvgBriefValue=("Brief Value (USD)", "mean"),
            Customers=("Customer Name", "nunique")
        )
        .reset_index()
    )

    return monthly

monthly["Year"]=...

monthly["Month"]=...

monthly["Quarter"]=...

monthly["MonthSin"]=...

monthly["MonthCos"]=...

def add_time_features(monthly):

for lag in [1,2,3,6]:

def add_lag_features(monthly):

def add_rolling_features(monthly):

def add_rolling_features(monthly):

monthly=pd.get_dummies(...)

def encode_region(monthly):

def create_features(path):

    df = load_data(path)

    monthly = prepare_monthly(df)

    monthly = add_time_features(monthly)

    monthly = add_lag_features(monthly)

    monthly = add_rolling_features(monthly)

    monthly = add_growth_features(monthly)

    monthly = monthly.dropna()

    monthly = encode_region(monthly)

    return monthly
