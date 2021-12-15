import csv
import pandas as pd
import plotly.express as px
import math

with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
def mean(file_data)
    totalMarks=0
    totalEntries=len(file_data)

    for marks in file_data:
        totalMarks=totalMarks+float(marks[1])

mean=totalMarks/totalEntries
print("Mean = "+str(mean))

squaredList=[]
for number in file_data:
    a=int(number)-mean(file_data)
    a=a**2
    squaredList.append(a)


sum=0
for i in squaredList:
    sum=sum+i
result=sum/(len(file_data)-1)
std=math.sqrt(result)
print(std)