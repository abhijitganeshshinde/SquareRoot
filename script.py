import csv
import subprocess

def read_csvfile():
    csvFile = 'restult.csv'

    with open(csvFile,'r') as file:
        readCSV = csv.DictReader(file)
        for row in readCSV:
            
            if row['status'] != 'passed':
                return False
    return True



result = read_csvfile()

if result:
    print("Test Case Pass")
    subprocess.run(['git','checkout','deployment'])
    subprocess.run(['git','merge','test'])
    subprocess.run(['git','push','origin','deployment'])
else:
    print("Test Case Fail")