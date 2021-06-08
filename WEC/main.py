import pandas as pd
import math
import csv

firestation1lat = 40.0137071
firestation1long = -75.3961213
firestation2lat = 40.0251013
firestation2long = -75.4490013
hospital1lat =  40.0514920
hospital1long = -75.3965480
hospital2lat = 40.0329254
hospital2long = -75.2750179
totalTimeF1=0
totalTimeF2=0
totalTimeH1=0
totalTimeH2=0

series1 = pd.read_csv('WEC.csv')
with open('WEC.csv') as csvDataFile:
    data=list(csv.reader(csvDataFile))
    csvReader = csv.reader(csvDataFile)
for x in range(0,135):
    if data[x][4] == 'EMS:':
        print("Time call was placed: " + str(data[x][6]))
        print("Type of emergency: " + str(data[x][5]))
        print("District: " + str(data[x][7]))
        distanceE1 = math.sqrt( ((hospital1lat-float(data[x][0]))**2)+((hospital1long-float(data[x][1]))**2) )*111
        distanceE2= math.sqrt( ((hospital2lat-float(data[x][0]))**2)+((hospital2long-float(data[x][1]))**2) )*111
        if distanceE1 > distanceE2:
            print("Distance to Hospital (Hospital 1): "+ str(distanceE1)+ " km")
            time = 7+4+2*distanceE1
            print("Time to complete (in mins): " + str(time)+"\n\n")
            totalTimeH1= totalTimeH1+time
        else:
            print("Distance to Hospital (Hospital 2) "+ str(distanceE2) + " km")
            time = 7+4+2*distanceE2
            print("Time to complete (in mins): " + str(time)+"\n\n")
            totalTimeH2= totalTimeH2+time


    elif data[x][4] == 'Fire:':
        print("Time call was placed: " + str(data[x][6]))
        print("Type of emergency: " + str(data[x][5]))
        print("District: " + str(data[x][7]))
        distanceF1 = math.sqrt( ((firestation1lat-float(data[x][0]))**2)+((firestation1long-float(data[x][1]))**2) )*111
        distanceF2= math.sqrt( ((firestation2lat-float(data[x][0]))**2)+((firestation2long-float(data[x][1]))**2) )*111
        if distanceF1 > distanceF2:
            print("Distance to Firestation (Firestation 1): "+ str(distanceF1)+ " km")
            time = 10+30+2*distanceF1/0.833
            print("Time to complete (in mins): " + str(time)+"\n\n")
            totalTimeF1= totalTimeF1+time
        else:
            print("Distance to Firestation (Firestation 2): "+ str(distanceF2)+ " km")
            time = 10+30+2*distanceF2/0.833
            print("Time to complete (in mins): " + str(time)+"\n\n")
            totalTimeF2= totalTimeF2+time

    elif data[x][4] == 'Traffic:':
        print("Time call was placed: " + str(data[x][6]))
        print("Type of emergency: " + str(data[x][5]))
        print("District: " + str(data[x][7]))
        distanceT1 = math.sqrt( ((hospital1lat-float(data[x][0]))**2)+((hospital1long-float(data[x][1]))**2) )*111
        distanceT2= math.sqrt( ((hospital2lat-float(data[x][0]))**2)+((hospital2long-float(data[x][1]))**2) )*111
        if distanceT1 > distanceT2:
            print("Distance to Hospital (Hospital 1): "+ str(distanceT1)+ " km")
            time = 7+4+2*distanceT1
            print("Time to complete (in mins): " + str(time)+"\n\n")
            totalTimeH1= totalTimeH1+time
        else:
            print("Distance to Hospital (Hospital 2): "+ str(distanceT2)+ " km")
            time = 7+4+2*distanceT2
            print("Time to complete (in mins): " + str(time)+"\n\n")
            totalTimeH2= totalTimeH2+time

print("Total time from start (Hospital 1): " + str(totalTimeH1))
print("Total time from start (Hospital 2): " + str(totalTimeH2))
print("Total time from start (Firestation 1):" + str(totalTimeF1))
print("Total time from start (Firestation 2): " + str(totalTimeF2))