import pandas as pd
df_fr=pd.read_csv("fertility_rate.csv.",header=0)
df_le=pd.read_csv("life_expectancy.csv",header=0)

df_fr1 = pd.DataFrame(df_fr, columns = ['Country Name','1966','1976','1986','1996','2006', '2016'])
df_le1 = pd.DataFrame(df_fr, columns = ['Country Name','1966','1976','1986','1996','2006', '2016'])

print(df_fr1)
print(df_le1)
df_fr2=df_fr1.iloc[0:264,0:6]
print(df_fr2)
df_le2=df_le1.iloc[0:264,0:6]
print(df_le2)

df_fr_le=pd.merge(df_fr2,df_le2,left_on='Country Name',right_on='Country Name',how='inner')
print(df_fr_le)
df_fr_le2=df_fr_le.fillna(method="bfill").fillna("ffill")
print(df_fr_le2)



