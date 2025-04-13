# Importing the pandas library, which is used for data analysis and manipulation
import pandas as pd

# Reading data from a JSON file named "sample_Data.json" and loading it into a DataFrame
df = pd.read_json("sample_Data.json")

# Printing a message to explain what’s coming next
print("Displaying the info of data set")

# Displaying summary information about the DataFrame
# This includes the number of entries (rows), column names, data types, and memory usage
print(df.info())
