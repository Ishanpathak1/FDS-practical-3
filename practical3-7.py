import pandas as pd
data={"Numbers":[1,2,3,4,5,6,7,8,1,10,1,12,13,14,1,16,17,18,1,20,21]}
df=pd.DataFrame(data)
df.loc[df["Numbers"]==1,"Numbers"]=100
print(df)