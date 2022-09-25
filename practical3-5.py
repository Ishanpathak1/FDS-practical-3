import pandas as pd
data={"Numbers":[10,20,30,40,50,60,70,80,30,20,10,2,3]}
df=pd.DataFrame(data)
df.loc[df["Numbers"]>=40,"Values"]="TRUE"
print(df)