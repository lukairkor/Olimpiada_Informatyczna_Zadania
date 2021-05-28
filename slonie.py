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
            line = [int(x) for x in line.split(',')]
            lines.append(line)
        
    licz_sloni = int(lines[0][0])
    mas_slon = lines[1]
    kol_startowa = lines[2]
    kol_docelowa = [[x] for x in lines[3]]

    # print(licz_sloni)
    # print(mas_slon)
    # print(kol_startowa)
    # print(kol_docelowa)

    masa_sloni = dict(zip(kol_startowa, mas_slon))
    graph = dict(zip(kol_startowa, kol_docelowa))
    
    return licz_sloni, masa_sloni, kol_startowa, kol_docelowa, graph
    

# DFS graph traversing iterational
def dfs_it(graph, start_node, end_node, cyc_with_repeti):
    # print(cyc_with_repeti)
    frontier = []
    frontier.append(start_node)
    explored = set()  
    while frontier:
        current_node = frontier.pop()
        if current_node in explored: continue
        if current_node == end_node: 
            if end_node not in cyc_with_repeti:
                cyc_with_repeti.append(end_node) 
                    
        for neighbor in graph[current_node]:
            frontier.append(neighbor)        
            explored.add(current_node) 
            
    return cyc_with_repeti


#
def creat_cycles_part1(start_node, my_cycles):
    # cyc_with_repeti will contain all cycles with repetition
    cyc_with_repeti = []
    for end_node in range(1, licz_sloni + 1):
        cycl = dfs_it(graph, start_node, end_node, cyc_with_repeti)
        if cycl not in my_cycles:
            my_cycles.append(cycl)
            print(cycl)
    print(cyc_with_repeti)
        
        
#
def creat_cycles_part2(Creat_cycles_part1):
    # list containing our cycles
    my_cycles = []
    # for amount of elephant
    for i in range(1, licz_sloni + 1):
        # return None
        Creat_cycles_part1(i, my_cycles)     
    # removes duplicates cycles in final list of cycles (my_cycles)
    my_cycles.sort()
    my_cycles = list(k for k,_ in itertools.groupby(my_cycles))
    # print("\nCycles: \n", my_cycles)
    return my_cycles


# distribution cycles into 2 element cycles for 
# sum theire mass
def rozklad_na_cykle_proste(my_cycles, masa_sloni):
    print("my_cycles: ", my_cycles)
    print("masa_sloni:", masa_sloni)
    cykle_proste = []
    for i, elem in enumerate(my_cycles, start = 1):
        dl_cyc = len(elem)
        print("i, elem: ", i, elem)
        print("dl_cyc: ", dl_cyc, "\n")
        for i in range(dl_cyc - 1):
            cykle_proste.append([elem[i], elem[i + 1]])
                    
    print("cykle_proste: ", cykle_proste)
    
    return cykle_proste
        


# calculate cycles parameters
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
                 
        # przechodzimy przez elementy cyklow
        for e in elem:
            # print(e, "n -ty slon\n")       
            list_of_mass.append(masa_sloni.get(e))
                
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

     
# count  finall reuslt
def oblicz_wyniku():   
    calkowi_masa_cyklu, min_masa_w_cyklu, min_ = wyzn_para_cykl()
    w = []
    for i, elem in enumerate(my_cycles, start = 1):        
        print("Numer cyklu: ", i)
        cmc = calkowi_masa_cyklu[i]
        mmwc = min_masa_w_cyklu[i]
        dl_cyc = len(elem)
        
        print("Dlugos_cyckl: ", dl_cyc)
        print("Calk_masa_cykl: ", cmc)
        print("Min masa w cyklu: ", mmwc)
        print("Globalne minimum: ", min_)  
                
        metoda1 = cmc + (dl_cyc  - 2) * mmwc
        metoda2 = cmc + mmwc + (dl_cyc + 1) * min_

        print("Metoda1 w cyklu: ", metoda1)
        print("Metoda2 w cyklu: ", metoda2, "\n")
       
        licz3 = min(metoda1, metoda2)
        w.append(licz3)

    wynik = sum(w)
    
    print("Wynik: ", wynik)
    # 30518 7038
    # 11200 
        

# algorithm  start
if __name__ == "__main__":      
    start = time.time() # starting time
    
    licz_sloni, masa_sloni, kol_startowa, kol_docelowa, graph = import_date()    
    my_cycles = creat_cycles_part2(creat_cycles_part1)
    print("my_cycles", my_cycles)
    # rozklad_na_cykle_proste(my_cycles, masa_sloni)
    # print(sumaC)        
    # wyzn_para_cykl()
    # oblicz_wyniku()
       
    end = time.time() # end time   
    print(f"Runtime of the program is {end - start}") # total time taken

                                                