import pandas as pd
df=pd.read_csv("netflix_titles.csv")
missing_values=df.isnull().sum()
new_df=df.fillna(method="bfill").fillna("ffill")
print(df.shape,new_df.info())
print(missing_values[0:5])
print(new_df.head)
print(new_df.shape)
drop_duplicates=new_df.drop_duplicates(subset=["title","release_year"])
print(drop_duplicates.shape)



