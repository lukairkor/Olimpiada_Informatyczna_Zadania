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
    with open('zadanie_B/slo1.in', 'r') as f:
        for line in f:
            line = line.strip()
            line = re.sub("\s+", ", ", line.strip())
            line = [int(x) for x in line.split(',')]
            lines.append(line)
        
    licz_sloni = int(lines[0][0])
    mas_slon = lines[1]
    kol_startowa = lines[2]
    kol_docelowa = [[x] for x in lines[3]]

    # print(licz_sloni)
    print(mas_slon)
    # print("kol_startowa", kol_startowa)
    # print("kol_docelowa", kol_docelowa)

    # masa_sloni = dict(zip(kol_startowa, mas_slon))
    graph = dict(zip(kol_startowa, kol_docelowa))
    
    return licz_sloni, mas_slon, kol_startowa, kol_docelowa, graph
    

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



# distribution cycles into 2 element cycles for 
# sum theire mass
def rozklad_na_cykle_proste(my_cycles, masa_sloni):
    # print("my_cycles: ", my_cycles)
    # print("masa_sloni:", masa_sloni)
    cykle_proste = []
    for i, elem in enumerate(my_cycles, start = 1):
        dl_cyc = len(elem)
        # print("i, elem: ", i, elem)
        # print("dl_cyc: ", dl_cyc, "\n")
        for i in range(dl_cyc - 1):
            cykle_proste.append([elem[i], elem[i + 1]])
                    
    print("cykle_proste: ", cykle_proste, "\n\n")
    
    return cykle_proste
        


# calculate cycles parameters
def wyzn_para_cykl(cykle_proste, masa_sloni, kol_startowa):
    print(masa_sloni, "masa_sloni\n")
    mass_in_cycles = []
    min_by_cycle = []
    min_mass_global = 0
    # przechodzimy przez cykle w liscie
    for i, elem in enumerate(cykle_proste, start = 1):
        print("numer i cykl ", i, elem)
        # przechodzimy przez elementy cyklow
        x = masa_sloni[elem[0]-1]
        y = masa_sloni[elem[1]-1]
        mass_in_cycles.append(x + y)
                       
        min_mass_in_cycle = min(x, y)
        min_by_cycle.append(min_mass_in_cycle)
        
        min_mass_global = min(min_by_cycle)
                   
    print("\nMin masa globalnie: ", min_mass_global)   
    print("Suma mas w cyklach:", mass_in_cycles)
    print("Najlzejszy slon w cyklu:", min_by_cycle)
    print("----------------------------------------------------\n")
    
    # print(sum(mass_in_cycles))
    return mass_in_cycles, min_by_cycle, min_mass_global

     
# count  finall reuslt
def oblicz_wyniku(mass_in_cycles, min_by_cycle, min_mass_global, cykle_proste, my_cycles):   
    
    w = []
    for i, elem in enumerate(cykle_proste, start = 0):        
        print("Numer cyklu: ", i)
        cmc = mass_in_cycles[i]
        mmwc = min_by_cycle[i]
        dl_cyc = len(elem)
        
        print("Dlugos_cyckl: ", dl_cyc)
        print("Calk_masa_cykl: ", cmc)
        print("Min masa w cyklu: ", mmwc)
        print("Globalne minimum: ", min_mass_global)  
                
        metoda1 = cmc + (dl_cyc  - 2) * mmwc
        metoda2 = cmc + mmwc + (dl_cyc + 1) * min_mass_global

        print("Metoda1 w cyklu: ", metoda1)
        print("Metoda2 w cyklu: ", metoda2)
       
        licz3 = min(metoda1, metoda2)
        print("licz3: ", licz3, "\n")
        w.append(licz3)

    wynik = sum(w)
    
    print("Wynik: ", wynik)
    # 30518 
    # 11200 
        

# algorithm  start
if __name__ == "__main__":      
    start = time.time() # starting time
    
    licz_sloni, masa_sloni, kol_startowa, kol_docelowa, graph = import_date()   
    
    my_cycles = get_cycles()
    # print("my_cycles: ", my_cycles)
    cykle_proste = rozklad_na_cykle_proste(my_cycles, masa_sloni)
    
    mass_in_cycles, min_by_cycle, min_mass_global = wyzn_para_cykl(cykle_proste, masa_sloni, kol_startowa)
    
    oblicz_wyniku(mass_in_cycles, min_by_cycle, min_mass_global, cykle_proste, my_cycles)
       
    end = time.time() # end time   
    print(f"Runtime of the program is {end - start}") # total time taken

                                                