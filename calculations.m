% speed of light
c = 299792458;
% load of navigation file 
load nav_file_07.txt
% caculation from variables loaded 
a0= nav_file_07(1,2);
a1=nav_file_07(1,3);
a2=nav_file_07(1,4);
aode = nav_file_07(2,1);
Crs = nav_file_07(2,2);
delta_n = nav_file_07(2,3);
M0 = nav_file_07(2,4);
Cuc = nav_file_07(3,1);
e = nav_file_07(3,2);
Cus = nav_file_07(3,3);
pierwiastek_z_a = nav_file_07(3,4);
toe = nav_file_07(4,1);
Cic = nav_file_07(4,2);
OMEGA_0 = nav_file_07(4,3);
Cis = nav_file_07(4,4);
i0 = nav_file_07(5,1);
Crc = nav_file_07(5,2);
omega = nav_file_07(5,3);
OMEGA_kropka = nav_file_07(5,4);
i_kropka = nav_file_07(6,1);
cod12 = nav_file_07(6,2);
GPS_week = nav_file_07(6,3);
GM = 398600500000000;
omega_e=0.00007292115;
a =(pierwiastek_z_a)^2;
n = sqrt((GM)/(a^3))+delta_n;
dt=900;
%algorithm of satelite coordinates
M = M0+n*dt;
E= [];
E(1) = M+e*sin(M);
for i=1:10 
    E(i+1)=M+e*sin(E(i));
    if E(i+1)-E(i)<0.00000000001
        break
    end
end
Ek=E(end);

%calculations of satellite clock error
dt_rel = (-2*sqrt(GM)*e*pierwiastek_z_a*sin(Ek))/c^2;
dtz = a0+a1*dt+(a2^2)*dt+dt_rel;

%algorithm of satelite coordinates
Vs=sqrt(1-e^2)*sin(Ek);
Vc=cos(Ek)-e;
Ve=1-e*cos(Ek);
% sprawdzic czy dodac pi czy odjac pi ?

V1=atan(Vs/Vc);
if V1<0
    V=V1+pi();
else
    V=V1;
end
fi=V+omega;
u=fi+[Cuc Cus]*[cos(2*fi);sin(2*fi)];
r=a*Ve+[Crc Crs]*[cos(2*fi);sin(2*fi)];
x_prim =  r*cos(u);
y_prim = r*sin(u);
inklinacja = i0+i_kropka*dt+[Cic Cis]*[cos(2*fi);sin(2*fi)];
OMEGA = OMEGA_0+OMEGA_kropka*dt-omega_e*(toe+dt);
format long g
X=(x_prim*cos(OMEGA)-y_prim*sin(OMEGA)*cos(inklinacja))/1000;
Y=(x_prim*sin(OMEGA)+y_prim*cos(inklinacja)*cos(OMEGA))/1000;
Z=(y_prim*sin(inklinacja))/1000;
