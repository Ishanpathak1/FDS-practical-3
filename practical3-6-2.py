import pandas as pd
data={"Cars":["Harrier","Polo","Spark","Supra","Benz","Audi","BMW","Harrier","Punch","XL6","Harrier"]}
df=pd.DataFrame(data)
df["Values"]=df["Cars"].apply(lambda x:"MATCH" if x=="Harrier" else "MISMATCH")
print(df)
df1=pd.DataFrame(data)
df1.loc[df1["Cars"]=="Harrier","Values"]="TRUE"
print(df1)