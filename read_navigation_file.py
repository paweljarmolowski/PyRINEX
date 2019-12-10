# -*- coding: utf-8 -*-
def read_navigation_file(nav_file):
    global epochDict
    import re
    #nav_file = r"d:\Master_Thesis\Reading_Navigation_File\WROC00POL_R_20193160000_01D_GN.rnx"
    with open(nav_file, 'r') as nav:
        for row in nav:
            if 'END OF HEADER' in row:
# Sprawdzam czy skrypt dotarł do konca headera                
                print("#################################")
                break
# Zaczynam itreowac sekcje z obserwacjami             
        for wiersz in nav:
# Jezeli znajdzie G to przydziela zmienna nazwie satelity oraz datcie
            if "G" in wiersz:
# Za pomocą wyrażenia regulatnego wyszukuje obserwacje w wierszu , który zawiera
# datę oraz numer satelity
                d = re.compile("^/s*|\-*\d{1}\.\d{12}D[+|-]\d{2}")
                a = d.findall(wiersz)
                            
                sat_num = wiersz[0:3]
                date = wiersz[3:23]
# Dodaje numer satelity , datę oraz trzy pierwsze obserwacje do słownika
                epochDict = {'epoch':{
                'sat_num':sat_num,
                'date':date,
                'a0':a[0],
                'a1':a[1],
                'a2':a[2]
                }
                }
                #print(epochDict)
# Dodaje zmienną wskazująca numer iteracji
                index = 0
            else:
# Jeżeli nie znajdę stringa "G" w linijce znaczy , że jestem w linijce z obserwacjami
                c = re.compile("/s*|\-*\d{1}\.\d{12}D[+|-]\d{2}")
                w = c.findall(wiersz)
# Index 0 oznacza ,że jestem w pierwszej linijce z obserwacjami 
                if index == 0:
                    epochDict['epoch']['aode'] = w[0]
                    epochDict['epoch']['Crs'] = w[1]
                    epochDict['epoch']['delta_n'] = w[2]
                    epochDict['epoch']['M0'] = w[3]
                    index = index + 1
                elif index == 1:
                    epochDict['epoch']['Cuc'] = w[0]
                    epochDict['epoch']['e'] = w[1]
                    epochDict['epoch']['Cus'] = w[2]
                    epochDict['epoch']['sqrt_a'] = w[3]
                    index = index + 1
                elif index == 2:
                    epochDict['epoch']['toe'] = w[0]
                    epochDict['epoch']['Cic'] = w[1]
                    epochDict['epoch']['OMEGA_0'] = w[2]
                    epochDict['epoch']['Cis'] = w[3]
                    index = index + 1
                elif index == 3:
                    epochDict['epoch']['i0'] = w[0]
                    epochDict['epoch']['Crc'] = w[1]
                    epochDict['epoch']['omega'] = w[2]
                    epochDict['epoch']['OMEGA_kropka'] = w[3]
                    index = index + 1
                elif index == 4:
                    epochDict['epoch']['i_dot'] = w[0]
                    epochDict['epoch']['L2_codes'] = w[1]
                    epochDict['epoch']['GPS_week'] = w[2]
                    epochDict['epoch']['L2_P_flag'] = w[3]
                    index = index + 1
                elif index == 5:
                    epochDict['epoch']['SV_accur'] = w[0]
                    epochDict['epoch']['SV_health'] = w[1]
                    epochDict['epoch']['TGD'] = w[2]
                    epochDict['epoch']['IOGC'] = w[3]
                    index = index + 1
                elif index == 6:
                    epochDict['epoch']['spare'] = w[0]
                    index = 0
                    print(epochDict)
# Tutaj zwaraca mi niestety tylko słownik dla pierwszej epoki
    return epochDict
                
                