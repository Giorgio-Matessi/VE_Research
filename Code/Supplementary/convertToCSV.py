import csv
import os

"""
Created on Fri July, 22 2022 11:14:35
Convert Data Files to CSV files
@author: Giorgio-Matessi

"""

inputDirPath = input("Path of Directory: ") 
outputDirPath = input("Output Directory: ")

if not os.path.isdir(outputDirPath):
    print("Directory does not exist. Creating Directory.")
    os.mkdir(outputDirPath)


for filename in os.listdir(inputDirPath):
   with open(os.path.join(inputDirPath, filename), 'r') as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=' ')

        name = outputDirPath + '/' + os.path.basename(filename) + ".csv"

        print(name)
        
        with open(name, 'w', newline='') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')
        
            for line in csv_reader:
                print(line)
                csv_writer.writerow(line)
print("Done.")
