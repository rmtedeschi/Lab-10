import json 
import csv

#Create Empty list
sales_data = []
#Create empty Dictionary
tempd = {}
#Open sales data file
with open("SalesJan2009(1).csv", "r") as inFile:
    csvReader = csv.reader(inFile)
    #loop to put each line of data into the temperary dictionary and then append it to list
    for line in csvReader:
        tempd = line
        sales_data.append(tempd)

#create output file
f = open("transaction_data.json", "x")
f.close()

#open file and write output data
with open("transaction_data.json", 'w', encoding='utf-8') as jsonf:
    jsonString = json.dumps(sales_data, indent=4)
    jsonf.write(jsonString)
        





