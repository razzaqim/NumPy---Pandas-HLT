import pandas as pd 

movies_data = pd.read_csv("Movie-Data.csv", index_col ="Year")
print(movies_data.loc[[2014]])
