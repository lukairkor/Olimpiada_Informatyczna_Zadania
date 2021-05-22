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
# graph ={
        # 1 : [5],
        # 4 : [3],
        # 5 : [2],
        # 3 : [4],
        # 6 : [2],
        # 2 : [1]  
        # }

# print(graph)

visited = set() # Set to keep track of visited nodes.
my_cycles = []

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
    sumaC = [] # suma mas sloni nalezacych do cyklu C
    minC = [] # masa najlzejszego slonia na cyklu C
    min_ = [] # masa najlzejszego slonia w ogole
    calkowi_masa_cyklu = {}
    min_masa_w_sycklu = {}
    
    minn = float('inf')
    min_ = minn
    for i, elem in enumerate(my_cycles, start = 1):
        print(i, elem)
        sumaC, minC = 0, minn
        for e in elem:
            # print(e, "\n")
            mas_slon_x =  masa_sloni.get(e)
            sumaC = sumaC + mas_slon_x
            if mas_slon_x < minC:
                minC =  mas_slon_x
                calkowi_masa_cyklu[i] = sumaC
                min_masa_w_sycklu[i] = minC

         
        print(sumaC, "suma mas cyklu")
        print(minC, "najlzejszy slon w cyklu")
        print(calkowi_masa_cyklu, "calkowi_masa_cyklu\n")
        print(min_masa_w_sycklu, "min_masa_w_sycklu\n")

        # print(list(opis_cykli.items())[0])
        
        min_ = min(min_masa_w_sycklu, key=min_masa_w_sycklu.get)
        min_ = min_masa_w_sycklu[min_]
        print(min_, "min masa ogolnie")   
        
        return calkowi_masa_cyklu, min_masa_w_sycklu, min_
        
# Obliczenie wyniku
def oblicz_wyniku():   
    calkowi_masa_cyklu, min_masa_w_sycklu, min_ = wyzn_para_cykl()
    w = 0
    # for i, elem in enumerate(my_cycles, start = 1):
    
    cmc = calkowi_masa_cyklu[1]
    mmwc = min_masa_w_sycklu[1]
    # min_
    
    metoda1 = cmc + (3 - 2) * mmwc
    metoda2 = cmc + mmwc + (3 + 1) * min_
    w = w + min(metoda1, metoda2)

    print(metoda1)
    print(metoda2)
    print(w)
    print(metoda1 + metoda2)
    print(metoda1 + metoda1)
    print(metoda2 + metoda2)
    print(w + w)
    #30518
        
# print(sumaC)        
wyzn_para_cykl()
oblicz_wyniku()


# if __name__ == "__main__":  
#     for i in range(1, licz_sloni+1):
#         x = dfs(visited, graph, i)
#         print(x)
