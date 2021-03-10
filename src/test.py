import pandas as pd
import time

# save filepath to variable for easier access
data_path = '../data/train.csv'
# read the data and store data in DataFrame titled digit_data
digit_data = pd.read_csv(data_path)
# print a summary of the data in digit_data
print(digit_data.describe())
# print a list of columns in digit_data
print(digit_data.columns)

# prediction target - select the column we want to predict
y = digit_data.label