# -*- coding: utf-8 -*-
class RINEXnav:
    def __init__(self,rnxfile,num_of_row): # moglbym dac tu epochDict jako pusty slownik domyslnie 
        self.rnxfile = rnxfile
        self.num_of_row = num_of_row
        # czy dodac parametr self.line ????
    #def read_line(self):
        #for line in open(self.rnxfile):
            #if self.sat_num in line:
                #line = line.split(" ")
                #while "" in line:
                    #line.remove("")
                #return line
#######################################################################################################    
    def read_navigation_file(self):
        """ 
        This function is created to read RINEX navigation file data section
        it returns a dictionary of dictionaries in form : 
            satellites = epoch{a1:'0.0004e+05',a2:'0.001e+02'...}
        """
        
        # Giving a variable satellites a global scope
        global satellites
        
        # Importing nesssecary modules
        import re
        
        # Creating an empty dictionaries to fill a data strings from file in
        epochDict = {}
        satellites = {}
        
        # Opening a gives file 
        with open(self.rnxfile, 'r') as nav:
            
            # Going into end of header of a file
            for row in nav:
                if 'END OF HEADER' in row:
                    print("############## END OF HEADER ###################\n")
                    break
                
    # Starting iteration of rows with dta
            for wiersz in nav: 
                if "G" in wiersz: # If it find "G" it assings a satellite and date name of vaariables
                    
    # Using an regular expression searching for  pattern of string in iterated row
    
                    d = re.compile("^/s*|\-*\d{1}\.\d{12}D[+|-]\d{2}")
                    a = d.findall(wiersz)
                    
                    # Substituting an "D" string in scientific notation for a "e" 
                    a = [i.replace('D', 'e') for i in a]
                    
                    # Assing from string sliceing
                    sat_num = wiersz[0:3] 
                    date = wiersz[3:23]
    
    # Dodaje numer satelity , datę oraz pięć pierwszych obserwacje do słownika
                    epochDict = {
                    'sat_num':sat_num,
                    'a0':a[0],
                    'a1':a[1],
                    'a2':a[2]
                    }
    
    
    # Adding a variable wich will calculte a numer of iterations
                    index = 0
                    
                else: # If conditional won't find string "G" in row , it means it is in row with only observations
    
    # Using an regular expression searching for  pattern of string in iterated row
                    c = re.compile("/s*|\-*\d{1}\.\d{12}D[+|-]\d{2}")
                    w = c.findall(wiersz)
                    
                    # Substituting an "D" string in scientific notation for a "e" 
                    w = [i.replace('D', 'e') for i in w]
    # Index 0  means that it is in firt line with obserwations 
                    if index == 0:
                        epochDict['aode'] = w[0]
                        epochDict['Crs'] = w[1]
                        epochDict['delta_n'] = w[2]
                        epochDict['M0'] = w[3]
                        index = index + 1
                    elif index == 1:
                        epochDict['Cuc'] = w[0]
                        epochDict['e'] = w[1]
                        epochDict['Cus'] = w[2]
                        epochDict['sqrt_a'] = w[3]
                        index = index + 1
                    elif index == 2:
                        epochDict['toe'] = w[0]
                        epochDict['Cic'] = w[1]
                        epochDict['OMEGA_0'] = w[2]
                        epochDict['Cis'] = w[3]
                        index = index + 1
                    elif index == 3:
                        epochDict['i0'] = w[0]
                        epochDict['Crc'] = w[1]
                        epochDict['omega'] = w[2]
                        epochDict['OMEGA_kropka'] = w[3]
                        index = index + 1
                    elif index == 4:
                        epochDict['i_dot'] = w[0]
                        epochDict['L2_codes'] = w[1]
                        epochDict['GPS_week'] = w[2]
                        epochDict['L2_P_flag'] = w[3]
                        index = index + 1
                    elif index == 5:
                        epochDict['SV_accur'] = w[0]
                        epochDict['SV_health'] = w[1]
                        epochDict['TGD'] = w[2]
                        epochDict['IOGC'] = w[3]
                        index = index + 1
                    elif index == 6:
                        epochDict['spare'] = w[0]
                        index = 0
    
    # Test czy dany słownik ma wystarczająco elementów 
                        #test_count_nav_dict_elements(epochDict
                        satellites[date] = epochDict
        print(satellites)
        return satellites
#######################################################################################################    
    def to_pandas_DataFrame(self,satellites):
        """
        This function will export data taken from RNX file as 
        an dictionary into simple pandas DataFame object with 
        epoch of satellite observation as an index value
        To test , it prints first 20 rows and DataFrame size.
        It returns DataFrame named epochFrame.
        """
        import pandas as pd
        global epochFrame
        global how_many_rows
        epochFrame = pd.DataFrame.from_dict(satellites,orient='index',dtype='float64')
        print('Number of columns in epochFrame:',len(epochFrame.index))
        print('Number of rows in epochFrame:',len(epochFrame.index))
        print(epochFrame.head(100))
        return epochFrame
#######################################################################################################    
    def calculatin_sat_XYZ(self,epochFrame):
        import math
        import numpy as np
        import pandas as pd
        global XYZ
        global XYZ_Frame
        
        GM = 398600500000000
        omega_e = 0.00007292115
        dt = 900
        c = 299792458
        
        XYZ_Frame = epochFrame.iloc[self.num_of_row,:]
        print(XYZ_Frame.tail())
        
        a = XYZ_Frame['sqrt_a']**2
        print("Major half-axis parameter a:{}".format(a))
        
        n = math.sqrt((GM)/(a**3))+XYZ_Frame['delta_n']
        print("Average speed of the satellite in rad/s n:{}".format(n))
        
        
        #algorithm of satelite coordinates
        M = XYZ_Frame['M0']+n*dt
        print("Mean anomaly in rad M:{}".format(M))
        
        
        E = M + XYZ_Frame['e'] * math.sin(M)
        print("Eccentric anomaly in rad E:{}".format(E))
        
        e = XYZ_Frame['e']
        
        for i in range(1,10): 
            E = M+e*math.sin(E)
            print("{} step of iteration. E is equal to: {} \n".format(i,E))
    
        
        #calculations of satellite clock error
        dt_rel = ((-2) * math.sqrt(GM) * XYZ_Frame['e'] * XYZ_Frame['sqrt_a'] * math.sin(E)) / c**2
        dtz = XYZ_Frame['a0'] + XYZ_Frame['a1'] * dt + (XYZ_Frame['a2']**2) * dt+dt_rel
        print('Relativistic_correction_of_clock:{}'.format(dt_rel))
        print('Second_correction_of_clock:{}'.format(dtz))
        
        #algorithm of satelite coordinates
        
        Vs = math.sqrt((1 - XYZ_Frame['e']**2)) * math.sin(E)
        Vc = math.cos(E) - XYZ_Frame['e']
        Ve = 1 - XYZ_Frame['e'] * math.cos(E)
        # sprawdzic czy dodac pi czy odjac pi ?
        
        V1 = math.atan(Vs/Vc)
        if V1<0.0:
            V = V1 + math.pi
        else:
            V = V1
        
        fi = V + XYZ_Frame['omega']
        print(fi)
        
        Cuc = XYZ_Frame['Cuc']
        Cus = XYZ_Frame['Cus']
        Cuc_Cus = np.array([Cuc, Cus])
        print("Here is matric Cuc_Cus{}".format(Cuc_Cus))
        cos2fi = math.cos(2*fi)
        sin2fi = math.sin(2*fi)
        cos2fi_sin2fi = np.array([[cos2fi],[sin2fi]])
        print(cos2fi_sin2fi)
        
        u=  fi + np.matmul(Cuc_Cus, cos2fi_sin2fi)
        print("The u arameter {}".format(u))
        
        Crc = XYZ_Frame['Crc'] 
        Crs = XYZ_Frame['Crs']
        Crc_Crs = np.array([Crc, Crs])
        r = a * Ve + np.matmul(Crc_Crs, cos2fi_sin2fi)
        print("The r parameter {}".format(r))
        
        
        x_prim =  r * math.cos(u)
        y_prim = r * math.sin(u)
        
        Cic = XYZ_Frame['Cic'] 
        Cis = XYZ_Frame['Cis']
        Cic_Cis = np.array([Cic, Cis])
        
        inklinacja = XYZ_Frame['i0']+XYZ_Frame['i_dot']*dt+np.matmul(Cic_Cis, cos2fi_sin2fi)
        print("Inclination parameter {}".format(inklinacja))
        
        OMEGA = XYZ_Frame['OMEGA_0'] + XYZ_Frame['OMEGA_kropka'] * dt - omega_e * dt # Here add some t_oe parameter 
        print("Omega prametr value {}".format(OMEGA))
        
        X=(x_prim * math.cos(OMEGA) - y_prim * math.sin(OMEGA) * math.cos(inklinacja)) / 1000
        Y=(x_prim * math.sin(OMEGA) + y_prim * math.cos(inklinacja) * math.cos(OMEGA)) / 1000
        Z=(y_prim * math.sin(inklinacja)) / 1000
        
        print("Tropoentric coordinates of satellites X:{} Y:{} Z:{}:".format(X,Y,Z))
        XYZ = [X, Y, Z]
        XYZ_convert = [str(X), str(Y), str(Z)]
        str_XYZ = ','.join(XYZ_convert)
        # to CSV file export
        with open('document.csv','a') as fd:
            fd.write(XYZ_Frame.name + ',' + str(XYZ_Frame['sat_num']) + ',' + str_XYZ + '\n')
            # TODO dodac epoke do csv
        print(XYZ)
        return XYZ
############################################################################################################        
    def plot_sat_XYZ(self,XYZ):
            
        """Function to plot 3D satellite position """
        from matplotlib import pyplot as plt
        import numpy as np
        # Earth radius
        RAD = 6371
        # Creating a chart
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Make data
        plt.title('Topocentric Coordinates of satellite')
        ax.set_xlabel('X(km)')
        ax.set_ylabel('Y(km)')       
        ax.set_zlabel('Z(km)')
        
        # Earth as a sphere
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = RAD * np.outer(np.cos(u), np.sin(v))
        y = RAD * np.outer(np.sin(u), np.sin(v))
        z = RAD * np.outer(np.ones(np.size(u)), np.cos(v))
        
        # Satellite position
        X = (RAD + XYZ[0]) + (500 * np.outer(np.cos(u), np.sin(v)))
        Y = (RAD + XYZ[1]) + (500 * np.outer(np.sin(u), np.sin(v)))
        Z = (RAD + XYZ[2]) + (500 * np.outer(np.ones(np.size(u)), np.cos(v)))


        # Plot the surfaces
        ax.plot_surface(x, y, z)
        ax.plot_surface(X, Y, Z)
        plt.show()

############################################################################################################   
    
    
    
# Rinex 3.11
wroclaw_navigation = RINEXnav('d:\Master_Thesis\Reading_Navigation_File\WROC00POL_R_20193160000_01D_GN.rnx',1)

# TEST

# Testing method --> read_navigation_file(self)
#wroclaw_navigation.read_navigation_file()

# Testing method --> to_pandas_DataFrame(satellites)
#wroclaw_navigation.to_pandas_DataFrame(satellites) 

# Testing method --> calculatin_sat_XYZ(epochFrame)6
#wroclaw_navigation.calculatin_sat_XYZ(epochFrame)

# Testing calculation for 10 first satellites
for first_ten in range(1,37):
    wroclaw_navigation = RINEXnav('d:\Master_Thesis\Reading_Navigation_File\WROC00POL_R_20193160000_01D_GN.rnx',first_ten)
    wroclaw_navigation.read_navigation_file()
    wroclaw_navigation.to_pandas_DataFrame(satellites)
    wroclaw_navigation.calculatin_sat_XYZ(epochFrame)
# Testing method --> plot_sat_XYZ()
#wroclaw_navigation.plot_sat_XYZ(XYZ)