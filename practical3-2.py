import csv
from traceback import print_tb
import pandas as pd
with open('/Users/ishanpathak/Desktop/Workshop-foundation-of-data-science/FDS-practical-3/sem5pract3new.csv' , mode='r') as file:
    csvFile=csv.reader(file)
df=pd.read_csv('sem5pract3new.csv')
sum1=df.groupby(['Country']).sum()
print("Sum by the GroupBy: ",sum1)
print("\n")
mean1=df.groupby(['Country']).mean()
print("Mean by the GroupBy: ",mean1)
print("\n")
max1=df.groupby(["Country"]).max()
print("Max by the GroupBy ",max1)
print("\n")

min1=df.groupby(["Country"]).min()
print("Min by the GroupBy",min1)
print("\n")
std1=df.groupby(["Country"]).std()
print("Standard Deviation by the GroupBy",std1)
print("\n")
var1=df.groupby(["Country"]).var()
print("Variance by the GroupBy",var1)
print("\n")
median1=df.groupby(["Country"]).median()
print("Median by the GroupBy",median1)
print("\n")
count1=df.groupby(["Country"]).count()
print("Count by the GroupBy",count1)


