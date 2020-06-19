# -*- coding: utf-8 -*-
class RINEXobs():
    """This class will interact with RINEX observation file (*.obs) type and 
    an (*csv) type file created earlier using RINEXnav class. Iputs are path to 
    this files (*obs) and (*csv). It wil return as a final result a cordinates 
    of reciver calculated on each epoch"""
    
    #TODO maybe i should pass an argument for a 
    def __init__(self,ephemerides,rnxfile):
        self.ephemerides = ephemerides
        self.rnxfile = rnxfile
    
    def read_obs_file(self):
        
        global obsDict
        
        import re        
        obsDict = {}
        observations = {}
        with open(self.rnxfile, 'r') as nav:
            for row in nav:
                if 'END OF HEADER' in row:
                    print("############## END OF HEADER ###################\n")
                    break
            for row in nav:
                if "> " in row: # If it find "G" it assings a date name of vaariables
                    
                    obs_date = row[2:29]
                    #observations['obs_date'] = obs_date
                    #print(obs_date)        
                elif "G" in row:
                    sat_num = row[0:3]
                    obsDict['sat_num'] = sat_num
                    
                    w = re.compile("^/s*|\-*\d{8}\.\d{3}")
                    a = w.findall(row)
                    code_obs = a[0:1]
                    code_obs = [float(i) for i in code_obs]
                    obsDict['code_obs'] = code_obs[0]
            observations[obs_date] = obsDict
            print(observations)
                
            #return obsDict    
        
                    
        def find_nearest_epoch(self,obsDict):
            pass
            
            
            
        # INHERETENCE
        
        # TESTING 

wroclaw_observation = RINEXobs('/home/pawel/Master_thesis_Pawel/document.csv','/home/pawel/Master_thesis_Pawel/WROC00POL_R_20193160045_15M_01S_MO (copy).rnx')

wroclaw_observation.read_obs_file()
