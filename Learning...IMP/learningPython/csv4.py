import csv

rows = [ ['Nikhil', 'COE', '2', '9.0'],  
         ['Sanchit', 'COE', '2', '9.1'],  
         ['Aditya', 'IT', '2', '9.3'],  
         ['Sagar', 'SE', '1', '9.5'],  
         ['Prateek', 'MCE', '3', '7.8'],  
         ['Sahil', 'EP', '2', '9.1']] 

fields = ['Name', 'Branch', 'Year', 'CGPA']  
with open('csv4.csv',mode="w") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(fields)
    csv_writer.writerows(rows)