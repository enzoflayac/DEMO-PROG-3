# Fichier codé par FLAYAC ENZO groupe TP3
# dernière modification 12 Avril 2024
import csv
import pandas as pd
import matplotlib.pyplot as plt

class SCATTER:
    def __init__(self,name, tpce, effst, tst):
        self.name = name
        self.tpce = tpce
        self.effst = effst
        self.tst = tst
        
    def CALCUL(self, xval, yval, tnst, pin, file2):
        effnst = (((tnst-self.tst)*self.tpce*self.effst)/100)+self.effst # YIELD CALCULATION FOR NON-STANDARD CONDITIONS
        pout=pin*(effnst/100) # CALCULATION OF DEVICE OUTPUT POWER
        ##PRINTING OUTPUT WITH FORMAT 
        file2.write("{0:.4f},{1:.4f},{2:.6f},{3:.6f}\n".format(xval,yval,effnst,pout))
    def OUTPOUT(self):
        self.name += ".csv" # ADD EXTENSION .CSV TO THE NAME
        file2 = open(self.name,"w")   # "w" MEANS OPEN-FILE FOR WRITING
        file2.write("Latitude,Longitude,EffNST,Pout\n") #HEADER LINE OF OUTPUT CSV-FILE
        #INPUT CSV-FILE
        file1 = open("World-Temp-Irr.csv","r")    # "r" MEANS OPEN-FILE FOR READING ONLY
        linefile1 = csv.reader(file1)      # FUNCTION FOR PROCESSING LINE IN A CSV-FILE
        europe_or_not=self.name.split('-')
        next(linefile1)                    # ESCAPE THE FIRST LINE OF CSV-FILE : HEADER LINE
        for row in linefile1:              # LOOP TO READ ELEMENTS OF CSV-FILE
            xval = float(row[0])           # 1ST ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            yval = float(row[1])           # 2ND ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            tnst = float(row[2])           # 3TH ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            pin = float(row[3])            # 4TH ELEMENT OF ROW, USE "float()" FOR PROPER CONVERSION
            if europe_or_not[0] == 'Europe': # CONDITION TO CHECK IF IT'S IN EUROPE
                if (35 <= xval <= 72) and ((-25) <= yval <= 65): 
                    self.CALCUL(xval,yval,tnst,pin,file2)
            else: # IF NOT IN EUROPE
                self.CALCUL(xval,yval,tnst,pin,file2)
        file1.close() #FILE CLOSE
        file2.close() #FILE CLOSE
    
#SETTING OBJECT
OBJ1= SCATTER("World-Si",(-0.15),20.4,25)
#INPUT FILE => "World-Temp-Irr.csv"
#OUTPUT FILE: Latitude,Longitude, EffNST, Pout
#FILE => "World-Si.csv"
OBJ1.OUTPOUT() 

#SETTING OBJECT
OBJ2 = SCATTER("World-Perovskite",(-0.15),20.4,25)
#INPUT FILE => "World-Temp-Irr.csv"
#OUTPUT FILE: Latitude,Longitude, EffNST, Pout
#FILE => "World-Perovskite.csv"
OBJ2.OUTPOUT()


#SETTING OBJECT
OBJ3 = SCATTER("Europe-Si",(-0.11),17.9,25)
#INPUT FILE => "World-Temp-Irr.csv"
#OUTPUT FILE: Latitude,Longitude, EffNST, Pout
#FILE => "Europe-Si.csv"
OBJ3.OUTPOUT()

#SETTING OBJECT
OBJ4 = SCATTER("Europe-Perovskite",(-0.11),17.9,25)
#INPUT FILE => "World-Temp-Irr.csv"
#OUTPUT FILE: Latitude,Longitude, EffNST, Pout
#FILE => "Europe-Perovskite.csv"
OBJ4.OUTPOUT()

def plot_printing(name):
    df = pd.read_csv(name) 
    print("\nColumns : \n")
    for col in df.columns: # LOOP TO READ ELEMENTS OF CSV-FILE
        print(col)
        
    #PRINTING HEAD
    print(f"\n{name} head :\n",df.head())

    #PRINTING TAIL
    print("\ntail :\n",df.tail())

    #PRINTING MAXIMUM IN EACH COLUMN
    print("\nmax :\n",df.max())

    #PRINTING MINIMUM IN EACH COLUMN
    print("\nmin :\n",df.min())
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

    # FIND THE MAXIMUM and MINIMUM Pout INDEX
    max_index_pout = df['Pout'].idxmax()
    max_index_effnst = df['EffNST'].idxmax()
    min_index_pout = df['Pout'].idxmin()
    min_index_effnst = df['EffNST'].idxmin()
    # RETRIEVE LONGITUDE AND LATITUDE VALUES CORRESPONDING TO MAXIMUM and MINIMUM POUT
    max_longitude_pout = df.loc[max_index_pout, 'Longitude']
    max_latitude_pout = df.loc[max_index_pout, 'Latitude']
    
    min_longitude_pout = df.loc[min_index_pout, 'Longitude']
    min_latitude_pout = df.loc[min_index_pout, 'Latitude']
    # RETRIEVE LONGITUDE AND LATITUDE VALUES CORRESPONDING TO THE MAXIMUM OF EFFNST
    max_longitude_effnst = df.loc[max_index_effnst, 'Longitude']
    max_latitude_effnst = df.loc[max_index_effnst, 'Latitude']
    min_longitude_effnst = df.loc[min_index_effnst, 'Longitude']
    min_latitude_effnst = df.loc[min_index_effnst, 'Latitude']
    print("\nPour", name,":\n")
    print(f"Pour le Pout maximum la longitude est : {max_longitude_pout} et la latitude : {max_latitude_pout}.")
    print(f"Pour le EffNST maximum la longitude est : {max_longitude_effnst} et la latitude : {max_latitude_effnst}.")
    print(f"\nPour le Pout minimun la longitude est : {min_longitude_pout} et la latitude : {min_latitude_pout}.")
    print(f"Pour le EffNST minimum la longitude est : {min_longitude_effnst} et la latitude : {min_latitude_effnst}.")
    


print_max("World-Si.csv")#PRINT THE MAX OF POUT AND EFFNST WITH THE FILE NAME
print_max("World-Perovskite.csv")#PRINT THE MAX OF POUT AND EFFNST WITH THE FILE NAME
print_max("Europe-Si.csv")#PRINT THE MAX OF POUT AND EFFNST WITH THE FILE NAME
print_max("Europe-Perovskite.csv")#PRINT THE MAX OF POUT AND EFFNST WITH THE FILE NAME
plot_printing("Europe-Si.csv") #PRINT THE PLOT WITH THE FILE NAME

#Je trouve que l'endroit où est le maximum Pout en Europe est à Chypre.
#Je trouve que l'endroit où est le minimum Pout en Europe est en Norvège à l'île Jan Mayen.
#Je trouve que l'endroit où est le maximum d'efficience en Europe est au Groenland.
#Je trouve que l'endroit où est le minimum d'efficience en Europe est en Irak.