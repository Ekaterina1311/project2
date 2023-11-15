 #print("Hello")
import pandas as pd
pd.options.display.max_rows = 1
df = pd.read_csv('data.csv')
strr = df.to_string()
print(strr)
print(df.info())


df1 = pd.read_csv('2.csv')
strr = df1.to_string()
print(strr)


