#Bu program, bir JFET veya kanal ayarlamalı MOSFET için dc öngerilimli hesaplarını ve Şekil 10.23'teki gibi bir devre için ac yükselteç hesaplamaları yapar.

# SERHAT İSMAİL ZUNLUOĞLU  20370031062

# -*- coding: utf-8 -*-
"""
Created on Fri May 20 12:55:54 2022

@author: Serhat
"""

# *********************************************
# *********************************************
# FET ac yükselteç hesapları için modül
# *********************************************

import math

print("Bu program, bir JFET veya kanal ayarlamalı MOSFET için dc öngerilimli hesaplarını ve ")
print("Şekil 10.23'teki gibi bir devre için ac yükselteç hesaplamaları yapar.\n")

print("Aşağıdaki devre bilgilerini girin:\n")

R1=float(input("RG1 (açık devre ise IE30 kullanın) = "))
R2=float(input("RG2 = "))
RS=float(input("Toplam kaynak direnci, RS = "))
RD=float(input("RD = "))

DD=float(input("Besleme gerilimi, VDD = "))

print("Aşağıdaki eleman bilgilerini girin: ")
SS = float(input("akaç-kaynak doyma akımı,IDSS = "))
VP = float(input("geçit-kaynak kısıma gerilimi, VP = "))

# Şimdi ön gerilim hesaplarını yapalım
# FET dc öngerilim hesaplamaları için modül
GG = (R2 / (R1 + R2)) * DD
A = SS * RS / (VP * VP)
B = 1-(2 * SS * RS / VP)
C = (SS * RS) - GG
D = (B * B) - (4 * A * C)

if D < 0:
    print("Çözüm yok!!!")

V1=(-B+math.sqrt(D))/(2*A)
V2=(-B-math.sqrt(D))/(2*A)

if abs(V1) > abs(VP):
    GS = V2

if abs(V2) > abs(VP):
    GS = V1

ID=SS*(1-((GS/VP)*(GS/VP)))
VS=ID*RS
VG=GG
VD=DD-ID*RD
DS=VD-VS


# Şimdi ön gerilim hesaplarını yapalım

print("Kutuplama akımı,ID= ",str(ID*1000),"mA")
print("öngerilimleri:")
print("VGS= ",str(GS),"Volt")
print("VD= ",str(VD),"Volt")
print("VS= ",str(VS),"Volt")
print("VDS= ",str(DS),"Volt")

print("Şimdi de ac yükselteç verilerini alalım: ")

RL = float(input("Yük direnci(yok ise IE30 alın), RL= "))
VA = float(input("Kaynak gerilim, Vs= "))
RA = float(input("Kaynak direnci, Rs= "))
S1 = float(input("Köprülenmemiş kaynak direnci, RS1= "))


GO=2*SS/abs(VP)
GM=GO*(1-GS/VP)
RM=1/GM
AV=-RD/(RM+S1)
RI=R1*R2/(R1+R2)
RO=RD
VI=RI*VA/(RA+RI)
VL=AV*VI*(RL/(RO+RL))
# Module to do Fet amplifier ac calculations
# Şimdi FET ac hesaplamarını Yapalım

print(f'Yükseltecin gerilim kazancı, Av= {AV:.6f}') # f fonksiyon kullanımı ile basamaktan sonra 6 rakam yazıldı
print(f'Yük üzerindeki çıkış gerilimi:{VL*1000:.5f} ',"mV") # f fonksiyon kullanımı ile basamaktan sonra 5 rakam yazıldı

print(f"Yükselteç katının giriş direnci, Ri= {RI/1000:.3f}","kiloohm") # f fonksiyon kullanımı ile basamaktan sonra 3 rakam yazıldı
print("Yükselteç katı çıkış direnci, Ro= ",str(RO/1000),"kiloohm")

