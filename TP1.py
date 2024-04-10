import csv
import random as rand
import math
import pandas as pd
import matplotlib.pyplot as plt

class SCATTER:
    def CALCUL(self, name ,tpce, effst, tst):
        name += ".csv"
        file2 = open(name,"w")   # "w" MEANS OPEN-FILE FOR WRITING
        file2.write("Longitude,Latitude,EffNST, Pout\n") #HEADER LINE OF OUTPUT CSV-FILE
        #INPUT CSV-FILE
        file1 = open("World-Temp-Irr.csv","r")    # "r" MEANS OPEN-FILE FOR READING ONLY
        linefile1 = csv.reader(file1)      # FUNCTION FOR PROCESSING LINE IN A CSV-FILE

        next(linefile1)                    # ESCAPE THE FIRST LINE OF CSV-FILE : HEADER LINE
        for row in linefile1:              # LOOP TO READ ELEMENTS OF CSV-FILE
            xval = float(row[0])           # 1ST ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            yval = float(row[1])           # 2ND ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            tnst = float(row[2])           # 3TH ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            pin = float(row[3])            # 4TH ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            if (35 <= xval <= 72) and ((-25) <= yval <= 65):
                effnst = (((tnst-tst)*tpce*effst)/100)+effst
                pout=pin*(effnst/100)
                ##PRINTING OUTPUT WITH FORMAT
                file2.write("{0:.4f},{1:.4f},{2:.6f},{3:.6f}\n".format(xval,yval,effnst,pout))
            else:
                effnst = (((tnst-tst)*tpce*effst)/100)+effst
                pout=pin*(effnst/100)
                ##PRINTING OUTPUT WITH FORMAT
                file2.write("{0:.4f},{1:.4f},{2:.6f},{3:.6f}\n".format(xval,yval,effnst,pout))
            #print("{0:.4f},{1:.4f},{2:.6f}".format(xval,yval,ff))
        file1.close() #FILE CLOSE
        file2.close() #FILE CLOSE

OBJ1= SCATTER()
OBJ1.CALCUL("World-Si",(-0.15),20.4,25)
OBJ1.CALCUL("World-Perovskite",(-0.15),20.4,25)
OBJ1.CALCUL("Europe-Si",(-0.15),20.4,25)
OBJ1.CALCUL("Europe-Perovskite",(-0.15),20.4,25)

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
