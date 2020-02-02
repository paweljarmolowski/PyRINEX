# -*- coding: utf-8 -*-
""" 
This function is created to read RINEX navigation file data section
it returns a dictionary of dictionaries in form : 
    satellites = epoch{a1:'0.0004e+05',a2:'0.001e+02'...}
"""
def read_navigation_file(nav_file):
    # Giving a variable satellites a global scope
    global satellites
    
    # Importing nesssecary modules
    import re
    
    # Creating an empty dictionaries to fill a data strings from file in
    epochDict = {}
    satellites = {}
    
    # Opening a gives file 
    with open(nav_file, 'r') as nav:
        
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

# Running a funtion on some file from Wroclaw Station
read_navigation_file("d:\Master_Thesis\Reading_Navigation_File\WROC00POL_R_20193160000_01D_GN.rnx")
