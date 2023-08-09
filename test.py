import pandas as pd

# Create a sample dataframe
data = {'Column1': [1, 2, 'N/A', 4, 5],
        'Column2': ['N/A', 'A', 'B', 'C', 'N/A']}
df = pd.DataFrame(data)

# Replace 'N/A' with NaN

# Alternatively, you can read the data while loading the dataframe
# df = pd.read_csv('your_data.csv', na_values=['N/A'])

print(df)
