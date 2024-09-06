# app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title and Description
st.title('Coffee Shop Sales Analysis')
st.write('This app performs a sales analysis of a coffee shop dataset.')

# File Uploader
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Check missing values
    missing_values = df.isnull().sum()
    st.write("### Missing Values")
    st.write(missing_values)

    # Data information
    st.write("### Data Information")
    st.write(df.info())

    # Convert transaction_time to timedelta and create new columns
    df['transaction_time'] = df['transaction_time'].astype(str)
    df['transaction_time'] = pd.to_timedelta(df['transaction_time'])
    df['sales'] = df['transaction_qty'] * df['unit_price']
    df['datetime'] = df['transaction_date'] + df['transaction_time']

    st.write("### Data with Sales and Datetime")
    st.dataframe(df.head())

    # Descriptive Statistics
    st.write("### Descriptive Statistics")
    st.write(df.describe())

    # Outliers Detection using Boxplots
    st.write("### Outliers Detection using Boxplots")
    numeric_columns = ['transaction_qty', 'unit_price', 'sales']

    # Plotting outliers
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for i, column in enumerate(numeric_columns):
        sns.boxplot(x=df[column], ax=axes[i])
        axes[i].set_title(f'Boxplot of {column}')
    st.pyplot(fig)

    # Group by store location
    df_location = df.groupby('store_location').agg({
        'sales': 'sum',
        'transaction_id':'count'
    })
    st.write("### Sales by Store Location")
    st.write(df_location)

    # Daily Sales by Location
    daily_sales_by_location = df.groupby(['transaction_date', 'store_location'])['sales'].sum().unstack()

    st.write("### Daily Sales by Location")
    st.line_chart(daily_sales_by_location)

    # Stacked Area Chart for Sales by Location
    st.write("### Stacked Area Chart of Sales by Location")
    fig, ax = plt.subplots(figsize=(14, 8))
    plt.stackplot(daily_sales_by_location.index, daily_sales_by_location.T, labels=daily_sales_by_location.columns)
    plt.title('Daily Sales by Store Location (Stacked Area Chart)')
    plt.xlabel('Date')
    plt.ylabel('Total Sales ($)')
    plt.legend(title='Store Location', loc='upper left')
    plt.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Daily, Weekly, Monthly, Quarterly, and Yearly Sales Analysis
    df['day_of_week'] = df['datetime'].dt.day_name()
    weekly_sales = df.groupby('day_of_week')['sales'].sum().reindex(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']).reset_index()

    st.write("### Weekly Sales")
    st.bar_chart(weekly_sales.set_index('day_of_week'))

    df['month'] = df['datetime'].dt.to_period('M')
    monthly_sales = df.groupby('month')['sales'].sum().reset_index()

    st.write("### Monthly Sales")
    st.line_chart(monthly_sales.set_index('month'))

    df['quarter'] = df['datetime'].dt.to_period('Q')
    quarterly_sales = df.groupby('quarter')['sales'].sum().reset_index()

    st.write("### Quarterly Sales")
    st.write(quarterly_sales)

    df['year'] = df['datetime'].dt.to_period('Y')
    yearly_sales = df.groupby('year')['sales'].sum().reset_index()

    st.write("### Yearly Sales")
    st.write(yearly_sales)
