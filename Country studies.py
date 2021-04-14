import pandas as pd

df_fr=pd.read_csv("fertility_ratev2.csv",header=0)
df_cp=pd.read_csv("country_ratev2.csv",header=0)

df_cp1=df_fr2=df_fr1.fillna(method="bfill").fillna("ffill")
print(df_fr2)
df_le2=df_le1.fillna(method="bfill").fillna("ffill")
print(df_fr2.isna().any(axis=1))
print(df_le2.isna().any(axis=1))
print(df_fr2.shape)
print(df_le2.shape)

df_fr1 = pd.DataFrame(df_fr, columns = ['Country Name','1976','1986','1996','2006', '2016'])
df_le1 = pd.DataFrame(df_fr, columns = ['Country Name','1976','1986','1996','2006', '2016'])

print(df_fr1)
print(df_le1)

print(df_fr1.shape)
print(df_le1.shape)
