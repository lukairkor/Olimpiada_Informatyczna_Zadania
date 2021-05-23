#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:48:15 2021

@author: lukas
"""
licz_sloni = 10 # n
mas_slon = [3015, 4728, 4802, 4361, 135, 4444, 4313, 1413, 4581, 546]
kol_startowa = [3, 10, 1, 8, 9, 4, 2, 7, 6, 5]
kol_docelowa = [[4], [9], [5], [3], [1], [6], [10], [7], [8], [2]]
wynik_koncowy = 0

masa_sloni = dict(zip(kol_startowa, mas_slon))
graph = dict(zip(kol_startowa, kol_docelowa))

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
    my_cycles.append(x)
    # print(x)

my_cycles = [x for x in my_cycles if x]
print(my_cycles, "my_cycles\n")


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
        cmc = calkowi_masa_cyklu[i]
        mmwc = min_masa_w_cyklu[i]
        Cl = len(elem)
        print(Cl, "Cl")
        print(cmc, "calk_masa_cykl")
        print(mmwc, "min mas w cyklu")
        metoda1.append(cmc + (abs(Cl) - 2) * mmwc)
        metoda2.append(cmc + mmwc + (abs(Cl) + 1) * min_)
        # w = w + min(metoda1, metoda2)
    
    print(metoda1, "metoda1")
    print(metoda2, "metoda2")
    metoda1 = sum(metoda1)
    metoda2 = sum(metoda2)
    print(metoda1)
    print(metoda2)
    print(w)
    print(metoda1 + metoda2)
    print(metoda1 + metoda1)
    print(metoda2 + metoda2)
    print(w + w)
    # 30518
        
# print(sumaC)        
wyzn_para_cykl()
oblicz_wyniku()


# if __name__ == "__main__":  
#     for i in range(1, licz_sloni+1):
#         x = dfs(visited, graph, i)
#         print(x)
                                                