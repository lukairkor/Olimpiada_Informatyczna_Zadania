#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:48:15 2021

@author: lukas
"""
import re 
import itertools
import time

# importuje dane z plikow i zmienia ich format
def import_date():
    lines = []  
    with open('zadanie_B/slo0.in', 'r') as f:
        for line in f:
            line = line.strip()
            line = re.sub("\s+", ", ", line.strip())
            line =[int(x) for x in line.split(',')]
            lines.append(line)
        
    licz_sloni = int(lines[0][0])
    masa_sloni = lines[1]
    kol_startowa = lines[2]
    kol_docelowa = [[x] for x in lines[3]]

    # print(licz_sloni)
    # print(mas_slon)
    # print(kol_startowa)
    # print(kol_docelowa)

    # masa_sloni = dict(zip(kol_startowa, mas_slon))
    graph = dict(zip(kol_startowa, kol_docelowa))
    
    return licz_sloni, masa_sloni, kol_startowa, kol_docelowa, graph
    

# DFS graph traversing iterational
def dfs(graph, start_vertex):
    visited = set()
    traversal = []
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            stack.extend(reversed(graph[vertex]))   # add vertex in the same order as visited
    return traversal


def getList(graph):
    list = []
    for key in graph.keys():
        list.append(key)
          
    return list
      

#
def get_cycles():
    my_cycles = []
    xx = getList(graph)
    for i, elem in enumerate(xx, start = 1):
        x_flat = [val for sublist in my_cycles for val in sublist]
        if elem not in x_flat:
            my_cycles.append(dfs(graph, elem))    

    # print(my_cycles)
    return my_cycles


# wyznaczanie param cykli
def wyzn_para_cykl():
    calkowi_masa_cyklu = {}
    min_masa_w_cyklu = {}
    
    minn = float('inf')
    min_ = 0
                
    # przechodzimy przez cykle w liscie
    for i, elem in enumerate(my_cycles, start = 1):
        print(i, elem, "numer i cykl\n")
        sumaC, minC = 0, minn
        list_of_mass = []
                    
        [list_of_mass.append(masa_sloni[i-1]) for i in elem]

        # # przechodzimy przez elementy cyklow
        # for e in elem:
        #     print(e, "n -ty slon\n")       
        #     list_of_mass.append(masa_sloni[e-1])
                
        sumaC = sum(list_of_mass)
        minC = min(list_of_mass)
            
        print(list_of_mass, "list_of_mass")
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
    w = []
    for i, elem in enumerate(my_cycles, start = 1):   
        print("Numer cyklu: ", i)
        cmc = calkowi_masa_cyklu[i]
        mmwc = min_masa_w_cyklu[i]
        dlugos_cyckl = len(elem)
        
        print("Dlugos_cyckl: ", dlugos_cyckl)
        print("Calk_masa_cykl: ", cmc)
        print("Min masa w cyklu ", mmwc)    
        
        metoda1 = cmc + (abs(dlugos_cyckl)  - 2) * mmwc
        metoda2 = cmc + mmwc + (abs(dlugos_cyckl) + 1) * min_

        print("Metoda1 w cyklu: ", metoda1)
        print("Metoda2 w cyklu: ", metoda2, "\n")
       
        licz3 = min(metoda1, metoda2)
        w.append(licz3)

    wynik = sum(w)
    
    print("Wynik: ", wynik)
    # 30518 
    # 11200 
        

# Programm start
if __name__ == "__main__":      
    start = time.time() # starting time

    licz_sloni, masa_sloni, kol_startowa, kol_docelowa, graph = import_date()    
    
    my_cycles = get_cycles()

    wyzn_para_cykl()
    
    oblicz_wyniku()
       
    end = time.time() # end time   
    print(f"Runtime of the program is {end - start}") # total time taken

                                                