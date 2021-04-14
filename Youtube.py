import pandas as pd

canadian_youtube=pd.read_csv("CAvideos.csv")

british_youtube=pd.read_csv("GBvideos.csv")

concat_data=pd.concat([canadian_youtube,british_youtube],axis=1)
join_data=canadian_youtube.join(british_youtube,lsuffix="_CAN",rsuffix="_UK")

print(canadian_youtube.shape,british_youtube.shape,concat_data.shape,join_data.shape)
print(join_data.info())



