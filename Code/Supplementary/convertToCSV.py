import pandas as pd
import numpy as np
import matplotlib as mt
import csv


# path = input("Path: ")
# path = path.replace('\\','/')
# print(path)

with open('C:\\Users\\giorg\\Desktop\\Computer Science\\Research\\VE_Research\\Code\\CitcomVE\\Data\\CASE100_P\\c02.topo_s_00438.dat', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    newFileName = input("Enter New File Name: ")

    with open("newFile.csv", 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')
        
        for line in csv_reader:
            csv_writer.writerow(line)
