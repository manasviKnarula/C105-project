import csv
import math 

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data=file_data[0]

def mean(data):
    total_marks = 0
    total_entries = len(data)

    for marks in data:
        total_marks += float(marks)

    mean = int(total_marks / total_entries)

    return mean


squared_list=[]

for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)

sum = 0

for i in squared_list:
    sum+=i
result = sum/(len(data)-1)

sd = math.sqrt(result)
print(sd)