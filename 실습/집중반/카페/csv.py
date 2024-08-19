import csv
f=open('구구단.csv','r')
reader=csv.reader(f)

for row in reader:
    print(row)