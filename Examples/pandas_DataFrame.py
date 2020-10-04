import pandas as pd

pd.options.display.max_columns = 6

 # Must have the full pointer to the file you want to use.
df = pd.read_csv('/Users/michael/Machine_Learning/sololearn-machine-learning/Examples/titanic.csv')

#print(df.head())
print(df.describe())