# -*- coding: utf-8 -*-
"""atividade_01_em.ipynb

**a) Definir um motor elétrico apropriado que deverá alimentar o redutor de
velocidade;**

**b) Fazer croqui (à mão livre) do sistema de transmissão de potência por meio de engrenagens de dentes retos mostrando o trem de engrenagem proposto;**

**c) Relações de transmissão de todo o trem de engrenagens;**
"""

from numpy import sqrt, sin, cos, tan, radians, pi, sqrt, interp
import pandas as pd

Pe = 30000                      #W
ωp = (1180*2*pi)/60                #rpm  escolhido no motor elétrico (entrada) - rad/s
Ps = 29400                      #W  
ωc = (72*2*pi)/60                  #rpm (saída) -> rad/s
print("ωp", ωp, "ωc", ωc)

mg1 = (ωp/ωc)
print(mg1)
mg2 = sqrt(mg1)
print(mg2)

Tent = Ps/ωp  #torque entrada
Tsai = Ps/ωc
print("torque entrada", Tent,"torque saída", Tsai)

"""**d) Principais dimensões geométricas do par de engrenagens que fornece o
torque de saída;**
"""

k = 1
Np = 21 #adotar o número de dentes do pinhão

for k in range(1, 10):
  Nc = mg2*Np
  print("pinhão", Np, "coroa", Nc)
  Np+=1
  k=+1

Nc = 85 #mais exato escolhido
Np = 21

m = 3  #adotado
pd = 1/m
theta = 20   
print(pd)

a = m                           #adendo
b = 0.25*m                      #dedendo
pc = pi*m                       #passo circular
pb = pc*cos(radians(theta))     #passo de base
F = 12*m                        #largura da face 6 a 16*m  

print("a =", a, "b =", b, "pc =", pc, "pb =", pb, "pd =", pd, "F =", F)

"""*pinhão*"""

dpp = m*Np               #diâmetro primitivo
dep = dpp + a*2          #diametro externo A = adendo, dp = diam. prim.
drp = dpp - 2*b          #diametro raiz D = dedendo, dr = diam. raiz
Vp = (pi*ωp/30)*(dpp/2)  #velocidade linear
print("Diâmetro primitivo do pinhão =", dpp, "Diâmetro externo do pinhão =", dep, "Diâmetro raiz do pinhão =", drp, "Velocidade linear do pinhão", Vp)

"""*coroa*"""

dpc = m*Nc               #diâmetro primitivo
dec = dpc + a*2          #diametro externo A = adendo, dp = diam. prim.
drc = dpc - 2*b          #diametro raiz D = dedendo, dr = diam. raiz
dbc = dpc*cos(radians(theta))
Vc = (pi*ωc/30)*(dpc/2)  #velocidade linear
print(dbc, "Diâmetro primitivo da coroa =", dpc, "Diâmetro externo da coroa =", dec, "Diâmetro raiz da coroa =", drc, "Velocidade linear da coroa", Vc)
dbc

C = dpc/2 + dpp/2
print("Distância entre centros =", C)

Z = sqrt(((dpp/2)+(a))**2 - ((dpp/2)*cos(radians(theta)))**2) + sqrt(((dpc/2)+(a))**2 - ((dpc/2)*cos(radians(theta)))**2) - C*sin(radians(theta))
print("Comprimento de ação =", Z)

mp = Z/pb
print(mp)

"""**e) Cálculo das tensões de fadiga de flexão e desgaste superficial nas 1,5 engrenagens do item d;**

*pinhão 1*
"""

Tp1 = Tent             #torque
Wtp1 = Tp1/(dpp/2)     #carga transmitida
Wrp1 = Wtp1*tan(radians(theta))
Wp1 = Wtp1/cos(radians(theta))
print ("Torque =", Tp1, "Carga Tangencial =", Wtp1, "Carga Radial =", Wrp1, "Carga Resultante =", Wp1)

"""*coroa 1*"""

Tc1 = Tp1*mg2            #torque
Wtc1 = Tc1/(dpc/2) #carga transmitida
Wrc1 = Wtc1*tan(radians(theta))
Wc1 = Wtc1/cos(radians(theta))
print ("Torque =", Tc1, "Carga Tangencial =", Wtc1, "Carga Radial =", Wrc1, "Carga Resultante =", Wc1)

"""*pinhão 2*"""

Tp2 = Tc1             #torque
Wtp2 = Tp1/(dpp/2) #carga transmitida
Wrp2 = Wtp2*tan(radians(theta))
Wp2 = Wtp2/cos(radians(theta))
print ("Torque =", Tp2, "Carga Tangencial =", Wtp2, "Carga Radial =", Wrp2, "Carga Resultante =", Wp2)

"""*coroa 2*"""

Tc2 = Tp1*mg1            #torque
Wtc2 = Tc2/(dpc/2)      #carga transmitida
Wrc2 = Wtc2*tan(radians(theta))
Wc2 = Wtc2/cos(radians(theta))
print ("Torque =", Tc2, "Carga Tangencial =", Wtc2, "Carga Radial =", Wrc2, "Carga Resultante =", Wc2)

Wm1 = Wtp1/2
Wm2 = Wtp2/2

print("Forças Alternadas no par 1 =", Wm1, "Forças Alternadas no par 2", Wm2)

Wtotal = Wtp1/cos(radians(theta))
print(Wtotal)

Jc = 0.42 #fator geométrico de resistência a flexão
Jp = 0.33 #fator geométrico de resistência a flexão

Ka = 1.25                             #motor elétrico
Km = 1.6
Ks = 1
Kb = 1
Kl = 1                            #1 p/ pinhão ou coroa e 1,42 para intermediária
Vt = (dpp/2000)*ωp*(dpp/dpc)
print("Vt =", Vt, "m/s")
Qv = 7       #assumindo indice de qualidade 7
Bx = ((12-Qv)**(2/3))/4
Ax = 50 + (56*(1-Bx))
Kv = ( Ax / (Ax + sqrt(200*Vt)))**(Bx)
Ax, Bx, Kv

σbc = ((Wtc1*Ka*Km*Ks*Kb*Kl)/(F*Jc*Kv*m))*10**3 #tensão de flexão
print("σbc", σbc)
σbp = ((Wtp1*Ka*Km*Ks*Kb*Kl)/(F*Jp*Kv*m))*10**3 #tensão de flexão
print("σbp", σbp)

rpp = dpp/2

rhop = sqrt((rpp + m)**2 - ((rpp)*cos(radians(theta)))**2)  - (pi*m)*cos(radians(theta))

rhoc = (C*sin(radians(theta))) - rhop

I = (cos(radians(theta)))/(((1/rhop)+(1/rhoc))*dpp)       #fator geométrico da superfície
print(rhop, rhoc, I)

Ca = Ka
Cv = Kv
Cm = Km
Cs = Ks
Cf = 1

vp = 0.28
Ep = 200*10**6
vc = 0.28
Ec = 200*10**6

Cp = sqrt(1/(pi*(((1-(vp)**2)/Ep)+(((1-(vc)**2)/Ec)))))
print(Cp)

σcp = Cp*sqrt((Wtp1*Ca*Cm*Cs*Cf)/((F)*I*(dpp)*Cv))     #resistência a crateração AGMA
print(σcp)

Tamb = 20
Temp = (9*Tamb)/5 + 32

N = ωp*60*16*5*52*20
print(N)

Kl = 1.3558*N**(-0.0178)
print("Kl", Kl)

if Temp>250:
  Kt = (460+Tamb)/620
else:
  Kt = 1
print(Kt)
Kr = 0.85

Sfci = 450
print("KL", Kl, "Sfci", Sfci, "Kt", Kt, "Kr", Kr)
Syi = (Kl*Sfci)/(Kt*Kr)         #desgaste superficial
print(Syi)

Cl = 1
A = 0 #considerando a mesma dureza da coroa e pinhao
Ch = 1
Ct = Kt
Cr = Kr

Sy = (Cl*Ch*Syi)/(Ct*Cr)         #resistência a fadiga a flexão
print(Sy)

coefsc = Sy/σbc
print(coefsc)

coefsp = Sy/σbp
print(coefsp)
