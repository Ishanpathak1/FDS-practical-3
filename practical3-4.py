import pandas as pd
data={"products":["Harrier","Punch","Altroz","Tiago"],"price":[2500000,530000,690000,7000000]}
df=pd.DataFrame(data)
print(df)
df.to_csv("/Users/ishanpathak/Desktop/Workshop-foundation-of-data-science/FDS-practical-3/sem5pract3new.csv",index=False)