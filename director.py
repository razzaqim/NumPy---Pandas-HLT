import pandas as pd 

movies_data = pd.read_csv("Movie-Data.csv", index_col ="Director")
print(movies_data.loc[["Ridley Scott", "Tom Ford"]]) 