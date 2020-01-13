# -*- coding: utf-8 -*-
class RINEXnav:
    def __init__(self,rnxfile,sat_num): # moglbym dac tu epochDict jako pusty slownik domyslnie 
        self.rnxfile = rnxfile
        self.sat_num = sat_num

    def read_line(self):
        for line in open(self.rnxfile):
            if self.sat_num in line:
                line = line.split(" ")
                while "" in line:
                    line.remove("")
                return line
# CREATE A SUB CLASS FOR VALUES ????


# Rinex 3.11
wroclaw_navigation = RINEXnav('d:\Master_Thesis\Reading_Navigation_File\WROC00POL_R_20193160000_01D_GN.rnx','G01')
# Rinex 2.10 format file 
v_naviagtion = RINEXnav('d:\Master_Thesis\Reading_Navigation_File\V130299I.11n','G01')

# TEST 
print(wroclaw_navigation.read_line())
# Not workinkg for Rinex 2.10 , test of file above
print(v_naviagtion.read_line())