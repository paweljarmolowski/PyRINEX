def calculatin_sat_XYZ(epochFrame,num_of_row)
    import math
    import numpy as np
    
    GM = 398600500000000
    omega_e = 0.00007292115
    dt = 900
    c = 299792458
    
    XYZ_Frame = epochFrame.iloc[num_of_row,:]
    #print(XYZ_Frame.tail())
    
    a = XYZ_Frame['sqrt_a']**2
    print(a)
    
    n = math.sqrt((GM)/(a**3))+XYZ_Frame['delta_n']
    print(n)
    
    
    #algorithm of satelite coordinates
    M = XYZ_Frame['M0']+n*dt
    print(M)
    
    
    E = M + XYZ_Frame['e'] * math.sin(M)
    print(E)
    #for i in range(1,20):
    #    E_list = list(M + XYZ_Frame['e'] * math.sin(E[i-1]
    #    print(E[i])
    #    if E[i+1]-E[i]<0.00000000001:
    #        break
    
    #Ek=E[:-1]
    
    #E = []
    #error = 0.000001
    
    ##############################################
    #for i in range(1,10): 
    #    Ek = M+e*sin(Ek)
    #    E = E.append(Ek)
    #    if Ek[-1] - E [-2] <  error:
    #        break
    
    #    if E(i+1)-E(i) < 0.00000000001:
    #        break
    #Ek=E(end)
    
    #calculations of satellite clock error
    dt_rel = ((-2)*math.sqrt(GM)*XYZ_Frame['e']*XYZ_Frame['sqrt_a']*math.sin(E))/c**2
    dtz = XYZ_Frame['a0'] + XYZ_Frame['a1'] * dt + (XYZ_Frame['a2']**2) * dt+dt_rel
    print('Relativistic_correction_of_clock:{}'.format(dt_rel))
    print('Second_correction_of_clock:{}'.format(dtz))
    
    #algorithm of satelite coordinates
    
    Vs = math.sqrt((1-XYZ_Frame['e']**2))*math.sin(E)
    Vc = math.cos(E)-XYZ_Frame['e']
    Ve = 1-XYZ_Frame['e']*math.cos(E)
    # sprawdzic czy dodac pi czy odjac pi ?
    
    V1 = math.atan(Vs/Vc)
    if V1<0.0:
        V=V1+math.pi
    else:
        V=V1
    
    fi=V+XYZ_Frame['omega']
    print(fi)
    
    #all_values = np.array(XYZ_Frame.values.tolist())
    
    #print(all_values)
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
    r=a*Ve+np.matmul(Crc_Crs, cos2fi_sin2fi)
    print("The r parameter {}".format(r))
    
    
    x_prim =  r*math.cos(u)
    y_prim = r*math.sin(u)
    
    Cic = XYZ_Frame['Cic'] 
    Cis =XYZ_Frame['Cis']
    Cic_Cis = np.array([Cic, Cis])
    
    inklinacja = XYZ_Frame['i0']+XYZ_Frame['i_dot']*dt+np.matmul(Cic_Cis, cos2fi_sin2fi)
    print("Inclination parameter {}".format(inklinacja))
    
    OMEGA = XYZ_Frame['OMEGA_0'] + XYZ_Frame['OMEGA_kropka'] * dt -omega_e * dt # HEre add some t_oe parameter 
    print("Omega prametr value {}".format(OMEGA))
    
    X=(x_prim*math.cos(OMEGA)-y_prim*math.sin(OMEGA)*math.cos(inklinacja))/1000
    Y=(x_prim*math.sin(OMEGA)+y_prim*math.cos(inklinacja)*math.cos(OMEGA))/1000
    Z=(y_prim*math.sin(inklinacja))/1000
    
    print(X,Y,Z)
    return 
