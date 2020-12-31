import csv

"""import pandas 

# reading the CSV file 
csvFile = pandas.read_csv('Giants.csv') 

# displaying the contents of the CSV file 
print(csvFile) 
"""

with  open('university_records.csv',mode='r') as csvFile:
    csv_reader = csv.reader(csvFile)
    for row in csv_reader:
        if row == []:
            pass
        else:
            print(row)
