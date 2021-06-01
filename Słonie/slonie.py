#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:48:15 2021

@author: lukas
"""
import re 
import time

# import data and adjust tham
def import_date():
    # file_ = input()
    lines = []  
    with open('zadanie_B/slo5.in', 'r') as f:
    # with open(str(file_), 'r') as f:
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
    
    # combine elephant start order with theire final order  
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


# get keys from graph (start order)
def get_list(graph):
    list_ = []
    [list_.append(key) for key in graph.keys()]    
          
    return list_


# use dfs() and getlist() to create cycles list of list
def get_cycles():
    my_cycles = []
    # for appropriate elephant order
    start_elep_order = get_list(graph)
    for i, elem in enumerate(start_elep_order, start = 1):
        # flattening cycle list from [[],[]..] to [..] to prevent
        # sending value from cycle we have in my_cycles
        x_flat = [val for sublist in my_cycles for val in sublist]
        if elem not in x_flat:
            my_cycles.append(dfs(graph, elem))    

    # print(my_cycles)
    return my_cycles


# calculate cycles parameters
def cycles_param_calculate():
    # construct cycles using DFS algorithm
    my_cycles = get_cycles()
    
    calkowi_masa_cyklu = {}
    min_masa_w_cyklu = {}   
    min_global = 0
                
    # przechodzimy przez cykle w liscie
    for i, elem in enumerate(my_cycles, start = 1):
        # print(i, elem, "numer i cykl\n")
        sumaC = 0
        list_of_mass = []
                    
        [list_of_mass.append(masa_sloni[i-1]) for i in elem]
                
        sumaC = sum(list_of_mass)
        minC = min(list_of_mass)
            
        # print(list_of_mass, "list_of_mass")
        # print("Min masa w cyklu: ",minC)
        # print("Suma mas cyklu: ", sumaC)       
        calkowi_masa_cyklu[i] = sumaC
        min_masa_w_cyklu[i] = minC

        min_global = min(min_masa_w_cyklu, key=min_masa_w_cyklu.get)
        min_global = min_masa_w_cyklu[min_global]
        
    # print("\nMin masa globalnie: ", min_global)   
    # print("Suma mas w cyklach:", calkowi_masa_cyklu)
    # print("Najlzejszy slon w cyklu:", min_masa_w_cyklu)
    # print("----------------------------------------------------\n")
        
    return calkowi_masa_cyklu, min_masa_w_cyklu, min_global, my_cycles

     
# count  finall result
def counting_result():   
    calkowi_masa_cyklu, min_masa_w_cyklu, min_global, my_cycles = cycles_param_calculate()
    result = []
    for i, elem in enumerate(my_cycles, start = 1):   
        # print("Numer cyklu: ", i)
        cmc = calkowi_masa_cyklu[i]
        mmwc = min_masa_w_cyklu[i]
        dlugos_cyckl = len(elem)
        
        # print("Dlugos_cyckl: ", dlugos_cyckl)
        # print("Calk_masa_cykl: ", cmc)
        # print("Min masa w cyklu ", mmwc)    
        
        method1 = cmc + (abs(dlugos_cyckl)  - 2) * mmwc
        method2 = cmc + mmwc + (abs(dlugos_cyckl) + 1) * min_global

        # print("Metoda1 w cyklu: ", method1)
        # print("Metoda2 w cyklu: ", method2, "\n")
       
        smalle_metod_value = min(method1, method2)
        result.append(smalle_metod_value)

    result = sum(result)
    
    print(result)
    # 30518 
    # 11200 
        

# algorithm  start
if __name__ == "__main__":      
    # start = time.time() # starting time
    # provides imput date
    licz_sloni, masa_sloni, kol_startowa, kol_docelowa, graph = import_date()    
    # final calculation
    counting_result()
       
    # end = time.time() # end time   
    # print(f"Runtime of the program is {end - start}") # total time taken

                                                