class RINEXnav:
    def __init__(self,epochtime,line):
        self.epochtime = epochtime
        self.line = line
    @classmethod
    def reading_line(cls,rnxfile):
        with open(rnxfile,"r") as rnxfile:
            for line in rnxfile:
                line = line.split(' ')
                for i in line:
                    while "" in line:
                        line.remove(i)
                return line
            
