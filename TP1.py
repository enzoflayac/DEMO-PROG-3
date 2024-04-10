import csv
import random as rand
import math
import pandas as pd
import matplotlib.pyplot as plt

class SCATTER:
    def CALCUL(self, name ,tpce, effst, tst):
        name += ".csv" # ADD EXTENSION .CSV TO THE NAME
        file2 = open(name,"w")   # "w" MEANS OPEN-FILE FOR WRITING
        file2.write("Latitude,Longitude,EffNST,Pout\n") #HEADER LINE OF OUTPUT CSV-FILE
        #INPUT CSV-FILE
        file1 = open("World-Temp-Irr.csv","r")    # "r" MEANS OPEN-FILE FOR READING ONLY
        linefile1 = csv.reader(file1)      # FUNCTION FOR PROCESSING LINE IN A CSV-FILE

        next(linefile1)                    # ESCAPE THE FIRST LINE OF CSV-FILE : HEADER LINE
        for row in linefile1:              # LOOP TO READ ELEMENTS OF CSV-FILE
            xval = float(row[0])           # 1ST ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            yval = float(row[1])           # 2ND ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            tnst = float(row[2])           # 3TH ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            pin = float(row[3])            # 4TH ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            if (35 <= xval <= 72) and ((-25) <= yval <= 65): # CONDITION TO CHECK IF IT'S IN EUROPE
                effnst = (((tnst-tst)*tpce*effst)/100)+effst # YIELD CALCULATION FOR NON-STANDARD CONDITIONS
                pout=pin*(effnst/100) # CALCULATION OF DEVICE OUTPUT POWER
                ##PRINTING OUTPUT WITH FORMAT 
                file2.write("{0:.4f},{1:.4f},{2:.6f},{3:.6f}\n".format(xval,yval,effnst,pout))
            elif (xval < 35 and xval > 72) and (yval < (-25) and yval > 65): # CONDITION TO CHECK IF IT'S NOT IN EUROPE
                effnst = (((tnst-tst)*tpce*effst)/100)+effst # YIELD CALCULATION FOR NON-STANDARD CONDITIONS
                pout=pin*(effnst/100) #CALCULATION OF DEVICE OUTPUT POWER
                ##PRINTING OUTPUT WITH FORMAT
                file2.write("{0:.4f},{1:.4f},{2:.6f},{3:.6f}\n".format(xval,yval,effnst,pout))
            #print("{0:.4f},{1:.4f},{2:.6f},{3:.6f}".format(xval,yval,effnst,pout))
        file1.close() #FILE CLOSE
        file2.close() #FILE CLOSE
#SETTING OBJECT
OBJ1= SCATTER()
#INPUT FILE => "World-Temp-Irr.csv"
#OUTPUT FILE: Latitude,Longitude, EffNST, Pout
#FILE => "World-Si.csv"
OBJ1.CALCUL("World-Si",(-0.15),20.4,25) 

#INPUT FILE => "World-Temp-Irr.csv"
#OUTPUT FILE: Latitude,Longitude, EffNST, Pout
#FILE => "World-Perovskite.csv"
OBJ1.CALCUL("World-Perovskite",(-0.15),20.4,25)

#INPUT FILE => "World-Temp-Irr.csv"
#OUTPUT FILE: Latitude,Longitude, EffNST, Pout
#FILE => "Europe-Si.csv"
OBJ1.CALCUL("Europe-Si",(-0.11),17.9,25)

#INPUT FILE => "World-Temp-Irr.csv"
#OUTPUT FILE: Latitude,Longitude, EffNST, Pout
#FILE => "Europe-Perovskite.csv"
OBJ1.CALCUL("Europe-Perovskite",(-0.11),17.9,25)

def plot_printing(name):
    df = pd.read_csv(name) 
    for col in df.columns: # LOOP TO READ ELEMENTS OF CSV-FILE
        print(col)
        
    #PRINTING HEAD
    print("head :\n",df.head())

    #PRINTING TAIL
    print("tail :\n",df.tail())

    #PRINTING MAXIMUM IN EACH COLUMN
    print("max :\n",df.max())

    #PRINTING MINIMUM IN EACH COLUMN
    print("min :\n",df.min())
    file1 = open(name,"r")    # "r" MEANS OPEN-FILE FOR READING ONLY
    linefile1 = csv.reader(file1) # READING OF FILE1
    first_row = next(linefile1) 
    namec1 = first_row[2] # RECUPERATION OF NAMES IN THE FIRST LINE OF THE FILE
    namec2 = first_row[3]
    # 4 colonnes : Latitude (max : 83.58333, min : -89.916667), Longitude (max : 179.916667, min : -179.91667), Avg. Temperature ( $^0$C ) (max : 30.755500, min : -54.6876), Annual Solar Irradiance ( kWh/m$^2$ ) (max : 2362.5723, min : 60.2334)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) #DEFINITION OF TWO PLOTS
    
    #x,y,c => x-axis, y-axis, z-axis
    #colormap       => Colour Scheme for contour plot
    #xlim, ylim     => Set minimum,maximum values in x-axis and y-axis
    #s => Size of the shape
    #grid => Set grid on plot
    #figsize => Set size of the figure

    df.plot(ax=ax1, x='Longitude', y='Latitude', c=namec1, kind="scatter", 
            colormap="coolwarm", title=namec1,
            xlim=(df["Longitude"].min(), df["Longitude"].max()), ylim=(df["Latitude"].min(), df["Latitude"].max()),s=(5.5), grid=("on"))

    df.plot(ax=ax2, x='Longitude', y='Latitude', c=namec2, kind="scatter", 
            colormap="coolwarm", title=namec2,
            xlim=(df["Longitude"].min(), df["Longitude"].max()), ylim=(df["Latitude"].min(), df["Latitude"].max()),s=(5.5), grid=("on"))

    plt.show()
    




def print_max(name):
    # LOAD DATA
    df = pd.read_csv(name)

    # FIND THE MAXIMUM Pout INDEX
    max_index_pout = df['Pout'].idxmax()
    max_index_effnst = df['EffNST'].idxmax()
    # RETRIEVE LONGITUDE AND LATITUDE VALUES CORRESPONDING TO MAXIMUM POUT
    max_longitude_pout = df.loc[max_index_pout, 'Longitude']
    max_latitude_pout = df.loc[max_index_pout, 'Latitude']
    # RETRIEVE LONGITUDE AND LATITUDE VALUES CORRESPONDING TO THE MAXIMUM OF EFFNST
    max_longitude_effnst = df.loc[max_index_effnst, 'Longitude']
    max_latitude_effnst = df.loc[max_index_effnst, 'Latitude']
    print("\nPour", name,":\n")
    print(f"Pour le Pout maximum la longitude est : {max_longitude_pout} et la latitude : {max_latitude_pout}.")
    print(f"Pour le EffNST maximum la longitude est : {max_longitude_effnst} et la latitude : {max_latitude_effnst}.")

print_max("World-Si.csv")#PRINT THE MAX OF POUT AND EFFNST WITH THE FILE NAME
print_max("World-Perovskite.csv")#PRINT THE MAX OF POUT AND EFFNST WITH THE FILE NAME
print_max("Europe-Si.csv")#PRINT THE MAX OF POUT AND EFFNST WITH THE FILE NAME
print_max("Europe-Perovskite.csv")#PRINT THE MAX OF POUT AND EFFNST WITH THE FILE NAME
plot_printing("World-Si.csv") #PRINT THE PLOT WITH THE FILE NAME





