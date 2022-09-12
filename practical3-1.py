import csv
import pandas as pd

with open('/Users/ishanpathak/Desktop/Workshop-foundation-of-data-science/FDS-practical-3/sem5pract3new.csv' , mode='r') as file:
    csvFile=csv.reader(file)
df=pd.read_csv('sem5pract3new.csv')
mean1=df['Salary'].mean()
print("Mean of the salary is : ",mean1)
print("\n")
median1=df['Salary'].median()
print("Median of the salary is : " ,median1)
print("\n")
mode1=df['Salary'].mode()
print("Mode of the Salary is: ",mode1)
print("\n")
sum1=df['Salary'].sum()
print("Sum of the Salary is : ",sum1)
print("\n")
std1=df['Salary'].std()
print("Standard deviation of the salary is : ",std1)
print("\n")
var1=df['Salary'].var()
print("Variance of the salary is : ",var1)
print("\n")
