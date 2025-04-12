# importing pandas with alias name as pd
import pandas as pd 

# Reading data from an Excel file named "Coca Cola Co.xlsx" into a DataFrame
df = pd.read_excel("Coca Cola Co.xlsx")
# Printing the contents of the Excel DataFrame
print(df)
# Reading data from a CSV file named "sales_data_sample.csv" with Latin-1 encoding or you can use UTF - 8 if it doesn't work for you
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# Printing the contents of the csv DataFrame
print(df)
# Reading data from a JSON file named "sample_Data.json" into a DataFrame
df = pd.read_json("sample_Data.json")
# Printing the contents of the json DataFrame
print(df)