import pandas as pd

df = pd.DataFrame ({'Courses': ["Spark", "PySpark", "Python", "pandas", "Java"],
                    'Fee': [20000, 25000, 30000, 24000, 40000],
                    'Duration': ['30day', '40days', '60days', '55days', '50days']})

df1 = pd.DataFrame ({'Courses': ["Java", "PySpark", "Python", "pandas", "Hyperion"],
                     'Fee': [20000, 25000, 30000, 24000, 40000],
                     'Percentage': ['10%', '20%', '25%', '20%', '10%']})

print (df)
print()
print (df1)
print()


# Use pandas.merge() to on multiple columns
df2 = pd.merge (df, df1, how='left', left_on=['Courses', 'Fee'], right_on=['Courses', 'Fee'])
print (df2)



