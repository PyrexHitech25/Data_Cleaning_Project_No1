# Libaries

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Pandas-Settings 

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 2000)

# Import Data

df = pd.read_csv(r'C:\Users\mypath\CSV\messy_sales_data.csv')

# Data Cleaning
    # Renaming Columns
    
df = df.rename(columns={'Customer Name': 'Customer_Name',
                        'Order ID': 'Order_ID'})

    # Converting date column to datetime format
    
df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=True)

    # Replacing missing values

df['Customer_Name'] = df['Customer_Name'].replace({'???': np.nan, 'unknown': np.nan})

df['customer_age']  = df['customer_age'].replace('120', np.nan)

df['Quantity'] = df['Quantity'].replace(-1, 1)

df['Total_Sales'] = df['Total_Sales'].replace({'three hundred ninety nine': 399, '$$$': np.nan, '-49': '49', '99999': np.nan})

df['Total_Sales'] = df['Total_Sales'].replace('\€', '', regex=True).astype(float)

df['Country'] = df['Country'].replace({'DE' : 'Germany', 'Deutschland': 'Germany', 'GER': 'Germany'})

df['Payment_Method'] = df['Payment_Method'].replace('credit card','Credit Card')

df['Price'] = df['Price'].str.replace(',', '.').astype(float)

    # Correcting specific values
    
df.at[17, 'Total_Sales'] = 4999

    # Dropping specific rows

df = df.drop(index=18)

    # Handling missing values

def check_NaN(column):
    num_missing = df[column].isna().sum()
    perc_missing = num_missing / len(df) * 100
    print(f'Column: {column} - Missing Values: {num_missing} ({perc_missing:.2f}%)')

    # Handeling NaN values in 'customer_age' by converting to numeric and filling with median

df['customer_age'] = pd.to_numeric(df['customer_age'], errors='coerce') 
median_age = df['customer_age'].median()
df['customer_age'] = df['customer_age'].fillna(median_age).astype(int)

    # Filling NaN values in 'Customer_Name' and 'Country' with 'Unknown'

df.fillna('Unknown', inplace=True)

# Export Cleaned Data

df.to_csv(r'C:\Users\mypath\Data Analyst\CSV\messy_data_cleaned.csv', index=False)
