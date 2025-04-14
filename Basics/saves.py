# Importing the pandas library, which helps us work with data
import pandas as pd

# Reading data from a CSV file named "sales_data_sample.csv"
# Using "latin1" encoding to properly handle any special characters
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# Saving the data we just read into a new Excel file called "sales_data.xlsx"
# Setting index=False so that row numbers don't get saved as an extra column
df.to_excel("sales_data.xlsx", index=False)

# Creating a small dictionary with some sample student information
# Each key is a column (Name, Age, City) and values are lists of data
data = {
    "Name": ["Sam", "Adi", "Ninja", "Arsh"],
    "Age": ["21", "18", "22", "20"],
    "City": ["Bramp", "Edmin", "Oak", "Calg"]
}

# Converting the dictionary into a pandas DataFrame (like a table)
df = pd.DataFrame(data)

# Printing the DataFrame to see the student data
print(df)

# Saving this new student DataFrame into an Excel file called "student_info.xlsx"
df.to_excel("student_info.xlsx", index=False)
