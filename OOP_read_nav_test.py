class RINEXnav:
    def __init__(self,rnxfile,sat_num): # mog³bym daæ tu epochDict jako pusty s³ownik domyœlnie 
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
        
test_method = RINEXnav('d:\Master_Thesis\Reading_Navigation_File\WROC00POL_R_20193160000_01D_GN.rnx','G01')

# TEST 

print(test_method.read_line())
