# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:30:23 2021

@author: budzp
"""
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import matplotlib.pyplot as plt5
from scipy.interpolate import make_interp_spline
count = 0
file = "T.txt"

with open (file) as json_file:
    atmodata = json.load(json_file)
    templist = list()
    for each in atmodata['atmo']:
        templist.append(each)
    pressurelist = templist[::4]
    tempFlist = templist[1::4]
    ALTlist = templist[2::4]
    timeMlist = templist[3::4]    
    templist = list()
    for each in atmodata['orient']:
        templist.append(each)
    orientx = templist[::4]
    orienty = templist[1::4]
    orientz = templist[2::4]
    timeMlist = templist[3::4]  
    templist = list()
    for each in atmodata['magnet']:
        templist.append(each)
    magnetx = templist[::4]
    magnety = templist[1::4]
    magnetz = templist[2::4]
    timeMlist = templist[3::4]  
    templist = list()
    for each in atmodata['linear']:
        templist.append(each)
    linearx = templist[::4]
    lineary = templist[1::4]
    linearz = templist[2::4]
    timeMlist = templist[3::4]  
    templist = list()
    for each in atmodata['accel2']:
        templist.append(each)
    gx = templist[::4]
    gy = templist[1::4]
    gz = templist[2::4]
    timeMlist = templist[3::4] 
    templist = list()
   # print(pressurelist)
   # print(tempFlist)
   # print(ALTlist)
   # print(timeMlist)
        #print((ALTlist[each] * 0.96)+(ALTlist[each] * 0.04))
        #templist.append((ALTlist[each] * 0.56)+(ALTlist[each] * 0.44))
        #ALTlist[each] = (ALTlist[each] * 0.56)+(ALTlist[each] * 0.44)
    #print (templist)    
    
    #print(len(templist))
def getAverage(data):
    return sum(data)  / len(data)
    
print (len(templist))      

def smoothData(data, alpha):
    weight = getAverage(data) * alpha
    smoothed = list()

print (getAverage(ALTlist),"average")

xarray1 = []
yarray1 = []


for each in range(len(ALTlist)):
    xarray1.append(float(ALTlist[each]))
for each in range(len(ALTlist)):
    yarray1.append(float(timeMlist[each]))    


slope = 0

yarray1 = np.array(ALTlist)
xarray1 = np.array(timeMlist)
slope, intercept = np.polyfit(yarray1, xarray1, 1)
xvar = np.linspace(0,110000,len(xarray1))
model_params1 = np.polyfit( xarray1, yarray1, 60)
y_predicted1 = np.polyval( model_params1, xvar )




yavg = getAverage(ALTlist)

plt.plot(timeMlist,gx)
plt.plot(timeMlist,gy)
plt.plot(timeMlist,gz)
#plt.scatter(datax,timeMlist)
plt.xlabel("Time in Milliseconds")
plt.ylabel("Gx")
plt.show()


plt2.plot(timeMlist,linearx)
plt2.plot(timeMlist,lineary)
plt2.plot(timeMlist,linearz)
plt.xlabel("Time in Milliseconds")
plt.ylabel("linearG")
plt2.show()

plt3.plot(timeMlist,magnetx)
#plt3.plot(timeMlist,magnety)
#plt3.plot(timeMlist,magnetz)
plt.xlabel("Time in Milliseconds")
plt.ylabel("magnetx")
plt3.show()


plt4.scatter(xarray1,yarray1,c='red',alpha = .2)
plt4.plot(xvar, y_predicted1, c="black")
#plt4.plot(xarray1,slope*xarray1+intercept)
#plt4.plot(timeMlist,ALTlist)
#plt4.plot(timeMlist,magnety)
#plt4.plot(timeMlist,magnetz)
plt4.xlabel("Time in Milliseconds")
plt4.ylabel("Altitude")
plt4.show()

plt5.plot(timeMlist,orientx)
#plt5.plot(timeMlist,magnety)
#plt5.plot(timeMlist,magnetz)
plt5.xlabel("Time in Milliseconds")
plt5.ylabel("oreintx")
plt5.show()


#-------------------------------------------------------------------------------------------------
