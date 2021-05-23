#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:48:15 2021

@author: lukas
"""
import re 

# lines = []  
# with open('zadanie_B/slo1.in', 'r') as f:
#     for line in f:
#         line = line.strip()
#         line = re.sub("\s+", ", ", line.strip())
#         line =[int(x) for x in line.split(',')]
#         lines.append(line)


# licz_sloni = int(lines[0][0])
# mas_slon = lines[1]
# kol_startowa = lines[2]
# kol_docelowa = [[x] for x in lines[3]]

# print(licz_sloni)
# print(mas_slon)
# print(kol_startowa)
# print(kol_docelowa)

licz_sloni = 6
mas_slon = [2400, 2000, 1200, 2400, 1600, 4000]
kol_startowa = [1, 4, 5, 3, 6, 2]
kol_docelowa = [[5], [3], [2], [4], [6], [1]]

masa_sloni = dict(zip(kol_startowa, mas_slon))
graph = dict(zip(kol_startowa, kol_docelowa))
# print(graph)
visited = set() # Set to keep track of visited nodes.
my_cycles = []


#
def dfs(visited, graph, node, p):
    if node not in visited:
        # print(node)
        p.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, p)
    return p


for i in range(1, licz_sloni + 1):  
    p = []      
    x = dfs(visited, graph, i, p)
    # x = dfs_it(graph, i)
    my_cycles.append(x)
    # print(x)

my_cycles = [x for x in my_cycles if x]
print("\nCycles: \n", my_cycles)


# wyznaczanie param cykli
def wyzn_para_cykl():
    calkowi_masa_cyklu = {}
    min_masa_w_cyklu = {}
    
    minn = float('inf')
    min_ = 0
                
    # przechodzimy przez cykle w liscie
    for i, elem in enumerate(my_cycles, start = 1):
        # print(i, elem, "numer i cykl\n")
        sumaC, minC = 0, minn
        list_of_mass = []
        
        # przechodzimy przez elementy cyklow
        for e in elem:
            # print(e, "n -ty slon\n")
  
            list_of_mass.append(masa_sloni.get(e))
                
            sumaC = sum(list_of_mass)
            minC = min(list_of_mass)
            
            # print(list_of_mass, "list_of_mass")
            print("Min masa w cyklu: ",minC)
            print("Suma mas cyklu: ", sumaC)       
            calkowi_masa_cyklu[i] = sumaC
            min_masa_w_cyklu[i] = minC

        min_ = min(min_masa_w_cyklu, key=min_masa_w_cyklu.get)
        min_ = min_masa_w_cyklu[min_]
        
    print("\nMin masa globalnie: ", min_)   
    print("Suma mas w cyklach:", calkowi_masa_cyklu)
    print("Najlzejszy slon w cyklu:", min_masa_w_cyklu)
    print("----------------------------------------------------\n")
        
    return calkowi_masa_cyklu, min_masa_w_cyklu, min_

        
# Obliczenie wyniku
def oblicz_wyniku():   
    calkowi_masa_cyklu, min_masa_w_cyklu, min_ = wyzn_para_cykl()
    w = 0
    metoda1 = []
    metoda2 = []
    
    #
    for i, elem in enumerate(my_cycles, start = 1):
        print("Numer cyklu: ", i)
        cmc = calkowi_masa_cyklu[i]
        mmwc = min_masa_w_cyklu[i]
        dlugos_cyckl = len(elem)
        
        print("Dlugos_cyckl: ", dlugos_cyckl)
        print("Calk_masa_cykl:", cmc)
        print("Min masa w cyklu", mmwc, "\n")
        
        # if abs(dlugos_cyckl) >= 0:
            
        metoda11 = cmc + (abs(dlugos_cyckl - 1) ) * mmwc
        metoda22 = cmc + mmwc + (abs(dlugos_cyckl + 1)) * min_
            
        metoda1.append(metoda11)
        metoda2.append(metoda22)
        
        print("Metoda1 w cyklu: ", metoda11)
        print("Metoda2 w cyklu: ", metoda22)
       
        licz1 = min(metoda1)
        licz2 = min(metoda2)
        licz3 = min(licz1, licz2)
        
        print(licz1, "licz1")        
        print(licz2, "licz2")    
        print(licz3, "licz3\n")
        # w = w + licz3
    
    print("Metoda1: ", metoda1)
    print("Metoda2: ", metoda2)
    
    liss = []
    for i in range(3):
        met1 = metoda1[i]
        met2 = metoda2[i]
        max_ = max(met1, met2)
        min_ = min(met1, met2)
        w = max_ - min_
        liss.append(w)
    
    
    
    # metoda1 = sum(metoda1)
    # metoda2 = sum(metoda2)
    
    # max_ = max(metoda1, metoda2)
    # min_ = min(metoda1, metoda2)
    
    # w = max_ - min_
    
    print(metoda1)
    print(metoda2)
    print("w:", sum(liss))
    # 30518
    # 11200
        
# print(sumaC)        
# wyzn_para_cykl()
# oblicz_wyniku()



# if __name__ == "__main__":  
#     for i in range(1, licz_sloni+1):
#         x = dfs(visited, graph, i)
#         print(x)
                                                