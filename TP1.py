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
        
    def TESTOUTPUT(self):
        #OUTPUT CSV-FILE
        file2 = open("XYOUTPUT.csv","w")   # "w" MEANS OPEN-FILE FOR WRITING
        file2.write("XVAL,YVAL,AVG TEMPERATURE, ASR\n") #HEADER LINE OF OUTPUT CSV-FILE
        
        #INPUT CSV-FILE
        file1 = open("XYINPUT.csv","r")    # "r" MEANS OPEN-FILE FOR READING ONLY
        linefile1 = csv.reader(file1)      # FUNCTION FOR PROCESSING LINE IN A CSV-FILE

        next(linefile1)                    # ESCAPE THE FIRST LINE OF CSV-FILE : HEADER LINE
        for row in linefile1:              # LOOP TO READ ELEMENTS OF CSV-FILE
            xval = float(row[0])           # 1ST ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            yval = float(row[1])           # 2ND ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            
            if ((xval*yval) > 0.00 ):
                f1 = self.alpha*rand.uniform(0.0,1.0) 
                f2 = self.beta*rand.uniform(-1.0,0.0)
                ff=f1+f2                       # 3RD ELEMENT, FILLING WITH RANDOM NUMBER
            else:
                f1 = self.beta*rand.uniform(0.0,1.0) 
                f2 = self.alpha*rand.uniform(-1.0,0.0)
                ff=f1+f2                       # 3RD ELEMENT, FILLING WITH RANDOM NUMBER
            
            ##PRINTING OUTPUT WITH FORMAT
            file2.write("{0:.4f},{1:.4f},{2:.6f}\n".format(xval,yval,ff))
            #print("{0:.4f},{1:.4f},{2:.6f}".format(xval,yval,ff))
        file1.close() #FILE CLOSE
        file2.close() #FILE CLOSE

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
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

df.plot(ax=ax1, x='Longitude', y='Latitude', c="Avg. Temperature ( $^0$C )", kind="scatter", 
        colormap="coolwarm", title='Avg. Temperature ( $^0$C )',
        xlim=(df["Longitude"].min(), df["Longitude"].max()), ylim=(df["Latitude"].min(), df["Latitude"].max()),s=(5.5), grid=("on"))

df.plot(ax=ax2, x='Longitude', y='Latitude', c="Annual Solar Irradiance ( kWh/m$^2$ )", kind="scatter", 
        colormap="coolwarm", title='Annual Solar Irradiance ( kWh/m$^2$ )',
        xlim=(df["Longitude"].min(), df["Longitude"].max()), ylim=(df["Latitude"].min(), df["Latitude"].max()),s=(5.5), grid=("on"))

plt.show()
