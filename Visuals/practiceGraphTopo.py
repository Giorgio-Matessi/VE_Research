"""
Created on Fri July, 22 2022 12:55:33

Practice Graphing Topgraphy 

@author: Giorgio-Matessi

Notes:
    - No espcially useful data
    - Just for practice 

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv 

topo1 = pd.read_csv("C:\\Users\\giorg\\Desktop\\Computer Science\\Research\\VE_Research\\Data\\CASE100_P_CSV\\c01.topo_s_00096.dat.csv", usecols = ['xCor','verticalDisplacement','rateDisplace','ignore'])
topo2 = pd.read_csv("C:\\Users\\giorg\\Desktop\\Computer Science\\Research\\VE_Research\\Data\\CASE100_P_CSV\\c01.topo_s_00102.dat.csv", usecols = ['xCor','verticalDisplacement','rateDisplace','ignore'])
topo3 = pd.read_csv("C:\\Users\\giorg\\Desktop\\Computer Science\\Research\\VE_Research\\Data\\CASE100_P_CSV\\c01.topo_s_00318.dat.csv", usecols = ['xCor','verticalDisplacement','rateDisplace','ignore'])

xCor1 = topo1['xCor']
verticalDisplacement1 = topo1['verticalDisplacement']
rateDisplace1 = topo1['rateDisplace']

xCor2 = topo2['xCor']
verticalDisplacement2 = topo2['verticalDisplacement']
rateDisplace2 = topo2['rateDisplace']

xCor3 = topo3['xCor']
verticalDisplacement3 = topo3['verticalDisplacement']
rateDisplace3 = topo3['rateDisplace']

plt.plot(xCor1,100 - verticalDisplacement1,
        xCor2,100-verticalDisplacement2,'r',
        xCor3,100-verticalDisplacement3,'b')
plt.show()




