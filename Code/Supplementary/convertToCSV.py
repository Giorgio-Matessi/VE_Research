import csv
import os

from numpy import number

"""
Created on Fri July, 22 2022 11:14:35
Convert Data Files to CSV files
@author: Giorgio-Matessi

Notes:
    - Windows 10+ only

"""



inputDirPath = input("Path of Input Directory: ")

if '\\' in inputDirPath or '\"' in inputDirPath:
    inputDirPath.replace('\\','/')
    inputDirPath.replace('\"','')
    

if not os.path.isdir(inputDirPath):
    print("Directory does not exist.")
    exit()   
    

outputDirPath = input("Output Directory: ")
if '\\' in outputDirPath or '\"' in outputDirPath:
    outputDirPath.replace('\\','/')
    outputDirPath.replace('\"','')
    outputDirPath.replace('\"','')


# Checks for output folder existance 
if not os.path.isdir(outputDirPath):
    print("Directory does not exist. Creating Directory.")
    input("Press Enter to continue...")
    os.mkdir(outputDirPath)


for filename in os.listdir(inputDirPath): #Runs through all files in a directory
    with open(os.path.join(inputDirPath, filename), 'r') as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter=' ') # Reads file 

        name = outputDirPath + '/' + os.path.basename(filename) + ".csv" # Stores name of file

        with open(name, 'w', newline='') as new_file: 
            new_file.write("First,Second,Third,Fourth\n")
            csv_writer = csv.writer(new_file, delimiter=',') # Rewrites file to have a comma delimiter 
            
            for line in csv_reader:
                csv_writer.writerow(line)

    print(os.path.basename(filename))

print("Done.")
