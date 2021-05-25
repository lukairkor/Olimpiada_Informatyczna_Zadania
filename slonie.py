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
            line =[int(x) for x in line.split(',')]
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
    

# DFS graph traversing
def dfs_it(graph, start_node, end_node, p):
    # print(p)
    frontier = []
    frontier.append(start_node)
    explored = set()  
    while frontier:
        current_node = frontier.pop()
        if current_node in explored: continue
        if current_node == end_node: 
            if end_node not in p:
                p.append(end_node) 
                    
        for neighbor in graph[current_node]:
            frontier.append(neighbor)        
            explored.add(current_node) 
    return p


#
def Creat_cycles_part1(j):
    p = []
    for i in range(1, licz_sloni + 1):
        # print(my_cycles)
        # for j in range(1, licz_sloni + 1):
        cycl = dfs_it(graph, j, i, p)
        my_cycles.append(cycl)
        
        
#
def Creat_cycles_part2(Creat_cycles_part1, my_cycles):  
    for i in range(1, licz_sloni + 1):
        Creat_cycles_part1(i)
       
    my_cycles.sort()
    my_cycles = list(k for k,_ in itertools.groupby(my_cycles))
    print("\nCycles: \n", my_cycles)
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
    # 30518 7038
    # 11200 
        

# Programm start
if __name__ == "__main__":      
    start = time.time() # starting time
    
    my_cycles = []

    licz_sloni, masa_sloni, kol_startowa, kol_docelowa, graph = import_date()    
    my_cycles = Creat_cycles_part2(Creat_cycles_part1, my_cycles)
    # print(sumaC)        
    wyzn_para_cykl()
    oblicz_wyniku()
       
    end = time.time() # end time   
    print(f"Runtime of the program is {end - start}") # total time taken

                                                