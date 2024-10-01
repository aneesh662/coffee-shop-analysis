
# Coffee Shop Sales Analysis
This project is focused on analyzing the sales data of a coffee shop using Python's Pandas, NumPy, Matplotlib, and Seaborn libraries. The dataset contains various details of transactions, including the transaction date, time, store location, product details, and sales amounts. The aim is to perform an exploratory data analysis (EDA), handle missing data, perform data cleaning, and generate visualizations to uncover key insights about sales trends across different store locations and time periods.

# Project Structure

# Data
The dataset (Coffee Shop Sales.xlsx) includes the following columns:
•	transaction_id: Unique ID for each transaction.
•	transaction_date: Date of the transaction.
•	transaction_time: Time when the transaction occurred.
•	transaction_qty: Quantity of products sold.
•	store_id: ID of the store where the transaction occurred.
•	store_location: Name of the store's location.
•	product_id: ID of the product sold.
•	unit_price: Price per unit of the product.
•	product_category: Category of the product (e.g., Coffee, Tea, etc.).
•	product_type: Type of the product within the category.
•	product_detail: Detailed product description.

# Data Analysis Process
1.	Data Loading: The dataset is loaded into a Pandas DataFrame for analysis.
df = pd.read_excel("Coffee Shop Sales.xlsx")

2.	Missing Values: Checked for any missing data.
missing_values = df.isnull().sum()

3.	Data Cleaning:
o	Converted transaction_time to a proper time format using pd.to_timedelta().
o	Calculated total sales by multiplying transaction_qty with unit_price.
o	Created a new datetime column by combining transaction_date and transaction_time.

4.	Descriptive Statistics: A summary of key statistics like mean, min, max, etc., for numerical columns using .describe().
df.describe()

5.	Outlier Detection: Identified outliers using the Interquartile Range (IQR) method and visualized them using boxplots.
sns.boxplot(x=df[column])

6.	Data Aggregation:
o	Grouped the data by store_location to analyze total sales and number of transactions.
o	Calculated daily sales across different store locations.

7.	Visualizations:
o	Boxplot: Visualized outliers for transaction_qty, unit_price, and sales.
o	Line Plot: Showed daily sales trends by store location.
o	Stacked Area Chart: Visualized cumulative daily sales across different locations.

8.	Time-Based Analysis:
o	Grouped sales data by day of the week, month, quarter, and year.
o	Created visualizations to explore how sales vary by these time periods.

# Visualizations
•	Daily Sales by Store Location: Shows how daily sales fluctuate across different store locations.
•	Weekly, Monthly, Quarterly Sales: Analyzes how sales change over different time frames to uncover trends.

# Libraries Used
•	Pandas: For data manipulation and analysis.
•	NumPy: For numerical operations.
•	Matplotlib: For generating plots.
•	Seaborn: For creating advanced visualizations.


