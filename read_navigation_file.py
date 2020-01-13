# -*- coding: utf-8 -*-
def read_navigation_file(nav_file):
    global epochDict
    import re

    epochDict = {}

    with open(nav_file, 'r') as nav:
        for row in nav:
            if 'END OF HEADER' in row:

# Sprawdzam czy skrypt dotarł do konca headera
                print("############## END OF HEADER ###################\n")
                break
            
# Zaczynam itreowac sekcje z obserwacjami
        for wiersz in nav: 
            if "G" in wiersz: # Jezeli znajdzie G to przydziela zmienna nazwie satelity oraz dacie

# Za pomocą wyrażenia regulatnego wyszukuje obserwacje w wierszu , który zawiera
# datę oraz numer satelity
                d = re.compile("^/s*|\-*\d{1}\.\d{12}D[+|-]\d{2}")
                a = d.findall(wiersz)
                sat_num = wiersz[0:3]
                date = wiersz[3:23]

# Dodaje numer satelity , datę oraz pięć pierwszych obserwacje do słownika
                epochDict = {
                'sat_num':sat_num,
                'date':date,
                'data':{
                'a0':a[0],
                'a1':a[1],
                'a2':a[2]
                }}


# Dodaje zmienną wskazująca numer iteracji
                index = 0
            else:

# Jeżeli nie znajdę stringa "G" w linijce znaczy , że jestem w linijce z obserwacjami
                c = re.compile("/s*|\-*\d{1}\.\d{12}D[+|-]\d{2}")
                w = c.findall(wiersz)

# Index 0 oznacza ,że jestem w pierwszej linijce z obserwacjami 
                if index == 0:
                    epochDict['data']['aode'] = w[0]
                    epochDict['data']['Crs'] = w[1]
                    epochDict['data']['delta_n'] = w[2]
                    epochDict['data']['M0'] = w[3]
                    index = index + 1
                elif index == 1:
                    epochDict['data']['Cuc'] = w[0]
                    epochDict['data']['e'] = w[1]
                    epochDict['data']['Cus'] = w[2]
                    epochDict['data']['sqrt_a'] = w[3]
                    index = index + 1
                elif index == 2:
                    epochDict['data']['toe'] = w[0]
                    epochDict['data']['Cic'] = w[1]
                    epochDict['data']['OMEGA_0'] = w[2]
                    epochDict['data']['Cis'] = w[3]
                    index = index + 1
                elif index == 3:
                    epochDict['data']['i0'] = w[0]
                    epochDict['data']['Crc'] = w[1]
                    epochDict['data']['omega'] = w[2]
                    epochDict['data']['OMEGA_kropka'] = w[3]
                    index = index + 1
                elif index == 4:
                    epochDict['data']['i_dot'] = w[0]
                    epochDict['data']['L2_codes'] = w[1]
                    epochDict['data']['GPS_week'] = w[2]
                    epochDict['data']['L2_P_flag'] = w[3]
                    index = index + 1
                elif index == 5:
                    epochDict['data']['SV_accur'] = w[0]
                    epochDict['data']['SV_health'] = w[1]
                    epochDict['data']['TGD'] = w[2]
                    epochDict['data']['IOGC'] = w[3]
                    index = index + 1
                elif index == 6:
                    epochDict['data']['spare'] = w[0]
                    index = 0

# Test czy dany słownik ma wystarczająco elementów 
                    #test_count_nav_dict_elements(epochDict
    print(epochDict)
    return epochDict

read_navigation_file("d:\Master_Thesis\Reading_Navigation_File\WROC00POL_R_20193160000_01D_GN.rnx")
