#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 03:14:30 2021

@author: lukas
"""
import re 
lines = []  
with open('zadanie_B/slo5.in', 'r') as f:
    for line in f:
        line = line.strip()
        line = re.sub("\s+", ", ", line.strip())
        line =[int(x) for x in line.split(',')]
        lines.append(line)


licz_sloni = int(lines[0][0])
mas_slon = lines[1]
kol_startowa = lines[2]
kol_docelowa = [[x] for x in lines[3]]

print(licz_sloni)
print(mas_slon)
print(kol_startowa)
print(kol_docelowa)

# licz_sloni = 6
# mas_slon = [2400, 2000, 1200, 2400, 1600, 4000]
# kol_startowa = [1, 4, 5, 3, 6, 2]
# kol_docelowa = [[5], [3], [2], [4], [6], [1]]

masa_sloni = dict(zip(kol_startowa, mas_slon))
graph = dict(zip(kol_startowa, kol_docelowa))