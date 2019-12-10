import numpy as np 
import math 

GM = 398600500000000
omega_e = 0.00007292115
a = (sqrt_a)**2
n = sqrt((GM)/(a^3))+delta_n
dt = 900
#algorithm of satelite coordinates
M = M0+n*dt
E = []
Ek = M+e*sin(M)
##############################################
#for i in range(1,10): 
#   E(i+1) = M+e*sin(E(i))
#    if E(i+1)-E(i) < 0.00000000001:
#        break
#Ek=E(end)
###############################################
#calculations of satellite clock error
dt_rel = ((-2)*sqrt(GM)*e*sqrt_a*sin(Ek))/c^2
dtz = a0+a1*dt+(a2^2)*dt+dt_rel

#algorithm of satelite coordinates
Vs = sqrt(1-e^2)*sin(Ek)
Vc = cos(Ek)-e
Ve = 1-e*cos(Ek)
# sprawdzic czy dodac pi czy odjac pi ?

V1 = atan(Vs/Vc)
if V1<0:
    V=V1+pi()
else:
    V=V1

fi=V+omega
#############################################################
Cuc_Cus = np.arrray(Cuc,Cus)
cos2fi_sin2fi = np.array(cos(2*fi) , sin(2*fi))
u=fi+Cuc_Cus*cos2fi_sin2fi
Crc_Crs = np.array(Crc, Crs)
r=a*Ve+Crc_Crs*cos2fi_sin2fi
#############################################################

x_prim =  r*cos(u)
y_prim = r*sin(u)

#############################################################
Cic_Cis = matrix(Cic, Cis)
inklinacja = i0+i_kropka*dt+Cic_Cis*cos2fi_sin2fi
#############################################################

OMEGA = OMEGA_0+OMEGA_kropka*dt-omega_e*(toe+dt)

X=(x_prim*cos(OMEGA)-y_prim*sin(OMEGA)*cos(inklinacja))/1000
Y=(x_prim*sin(OMEGA)+y_prim*cos(inklinacja)*cos(OMEGA))/1000
Z=(y_prim*sin(inklinacja))/1000
