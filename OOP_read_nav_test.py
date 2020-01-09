class RINEXnav:
    def __init__(self,epochtime,line):
        self.epochtime = epochtime
        self.line = line
    @classmethod
    def reading_line(cls,rnxfile):
        with open(rnxfile,"r") as rnxfile:
            for line in rnxfile:
                print(rnxfile.readline(5))
                return line
            
RINEXnav.reading_line('D:\Master_Thesis\Reading_Navigation_File\WROC00POL_R_20193160000_01D_GN.rnx')
