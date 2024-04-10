import csv
import random as rand
import math
import pandas as pd
import matplotlib.pyplot as plt

class SCATTER:
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
    def INPUTGRID(self):
        dx=0.10
        dy=0.10
        ngrid=200
        xmin=-10.00
        ymin=-10.00
        
        file = open("XYINPUT.csv","w")  # OPENING CSV-FILE FOR WRITING
        file.write("XVAL,YVAL\n")       # HEADER-LINE OF CSV-FILE
        
        ##LOOP OVER X,Y TO CREATE GRIDS
        for ix in range(0,ngrid+1):
            for iy in range(0,ngrid+1):
                xval=xmin+dx*ix
                yval=ymin+dy*iy
                file.write("{0:.6f},{1:.6f}\n".format(xval,yval)) #WRITING IN CSV FILE
        file.close() #FILE CLOSE
        
    

df = pd.read_csv("World-Temp-Irr.csv")
for col in df.columns:
    print(col)
    
#PRINTING HEAD
print(df.head())

#PRINTING TAIL
print(df.tail())

#PRINTING MAXIMUM IN EACH COLUMN
print(df.max())

#PRINTING MINIMUM IN EACH COLUMN
print(df.min())

# 4 colonnes : Latitude (max : 83.58333, min : -89.916667), Longitude (max : 179.916667, min : -179.91667), Avg. Temperature ( $^0$C ) (max : 30.755500, min : -54.6876), Annual Solar Irradiance ( kWh/m$^2$ ) (max : 2362.5723, min : 60.2334)

df.plot(x='Longitude', y='Latitude', c="Avg. Temperature ( $^0$C )",kind="scatter",colormap="coolwarm", 
        xlim=(df["Longitude"].min(),df["Longitude"].max()), ylim=(df["Latitude"].min,df["Latitude"].max()),
        grid=("on"))
plt.show()
