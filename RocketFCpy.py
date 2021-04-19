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
file = "rocketlaunch.txt"

with open (file) as json_file:
    atmodata = json.load(json_file)
    templist = list()
    for each in atmodata['atmo']:
        templist.append(each)
    pressurelist = templist[::4]
    tempFlist = templist[1::4]
    humidList = templist[2::4]
    ALTlist = templist[3::4]    
    templist = list()
    for each in atmodata['orient']:
        templist.append(each)
    orientx = templist[::3]
    orienty = templist[1::3]
    orientz = templist[2::3]  
    templist = list()
    for each in atmodata['magnet']:
        templist.append(each)
    heading = templist
    templist = list()
    for each in atmodata['accel2']:
        templist.append(each)
    gx = templist[::4]
    gy = templist[1::4]
    gz = templist[2::4]
    timeMlist = templist[3::4] 
    templist = list()
    
xarray1 = []
npaltarray = []

#for x in range(len(ALTlist)):
#    if ALTlist[x] < -200:
#        ALTlist[x] = 0
for each in range(len(ALTlist)):
    xarray1.append(float(ALTlist[each]))
for each in range(len(ALTlist)):
    npaltarray.append(float(timeMlist[each]))    

nums = []
for number in gx:
    nums.append(number/9.81)
    
gx = nums    
nums = []

for number in gy:
    nums.append(number/9.81)
    
gy = nums    
nums = []

for number in gz:
    nums.append(number/9.81)
    
gz = nums    
nums = []


def removeDataPost(arr, rem):
    arr = arr[:rem]
   # print(len(arr))
    return arr

def removeDataPre(arr, rem):
    arr = arr[rem:]
    return arr



    
def getMaxG(accel):
    maax = 0.0
    temp = 0.0
    for x in range(len(accel)):
    
        if accel[x] > maax:
            temp = accel[x]
        maax = temp
    return maax
    
def getApogee(alt):
    mx = 0.0
    temp = 0.0
    for x in range(len(alt)):
    
        if alt[x] > mx:
            temp = alt[x]
        mx = temp
    return mx
def getAvgHumidity(humarr):
    divider = len(humarr)
    total = 0.0
    for x in range(len(humarr)):
        total += humarr[x]
        
    return total/divider    
        
def getTempF(temparr):
    mx = 0.0
    temp = temparr[0]
    mn = 0.0
    
    for x in range(len(temparr)):
    
        if temparr[x] < mn:
            temp = temparr[x]
        mn = temp
    
    
    for x in range(len(temparr)):
    
        if temparr[x] > mx:
            temp = temparr[x]
        mx = temp
    return mx,"max temp", mn, "min temp"
    







time1000 = removeDataPost(timeMlist,700)
time1000 = removeDataPre(time1000, 550)
gx1000 = removeDataPost(gx, 700)
gx1000 = removeDataPre(gx1000, 550)
gy1000 = removeDataPost(gy, 700)
gy1000 = removeDataPre(gy1000, 550)
gz1000 = removeDataPost(gz, 700)
gz1000 = removeDataPre(gz1000, 550)

Alt1000 = removeDataPost(ALTlist, 700)
Alt1000 = removeDataPre(Alt1000, 550)

#y =  time1000[-1]
#npaltarray = np.array(ALTlist)
#xarray1 = np.array(time1000)
#slope, intercept = np.polyfit(npaltarray, xarray1, 1)
#xvar = np.linspace(0,y,len(xarray1))
#model_params1 = np.polyfit( xarray1, npaltarray, 5)
#y_predicted1 = np.polyval( model_params1, xvar )
#
#
#


print(getMaxG(gz),"Gz")
print(getMaxG(gx),"Gx")
print(getMaxG(gy),"Gy")
print(getApogee(ALTlist), "feet")
print(getAvgHumidity(humidList), "% Average Humidity")
print(getTempF(tempFlist))

plt.scatter(time1000,gx1000, c='blue',alpha = .8)
plt.plot(time1000,gx1000, c='blue',alpha = .8)
plt.plot(time1000,gy1000, c='red',alpha = .8)
plt.plot(time1000,gz1000, c='green',alpha = .8)
#plt.plot(timeMlist,gy, c= 'brown',alpha = .8)
#plt.plot(timeMlist,gz, c= 'red',alpha = .8)
plt.xlabel("Time in Milliseconds")
plt.ylabel("G")
plt.show()
#

plt2.plot(timeMlist,heading)
plt2.xlabel("Time in Milliseconds")
plt2.ylabel("Heading")
plt2.show()
#
##plt3.plot(timeMlist,pressurelist)
#plt3.plot(timeMlist,tempFlist)
#plt3.plot(timeMlist,humidList)
#plt3.xlabel("Time in Milliseconds")
#plt3.ylabel("atmo")
#plt3.show()



plt4.plot(time1000,Alt1000, c="red")
plt4.title("Altitude over Time")
plt4.xlabel("Time in Milliseconds")
plt4.ylabel("Altitude Ft.")
plt4.show()

plt5.plot(timeMlist,orientx)
plt5.plot(timeMlist,orienty)
plt5.plot(timeMlist,orientz)
plt5.xlabel("Time in Milliseconds")
plt5.ylabel("Oreintx")
plt5.show()


#-------------------------------------------------------------------------------------------------
