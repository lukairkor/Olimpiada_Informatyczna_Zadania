#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 18:10:00 2021

@author: lukas
"""
import re 
import itertools
import time
from collections import OrderedDict

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

     
licz_sloni, masa_sloni, kol_startowa, kol_docelowa, graph = import_date()



# # print(graph)

def getList(graph):
    list = []
    for key in graph.keys():
        list.append(key)
          
    return list
      
# # Driver program
# print(getList(graph))
xx = getList(graph)


my_cycles = []
for elem in range(1 , licz_sloni + 1):
    x_flat = [val for sublist in my_cycles for val in sublist]
    if elem not in x_flat:
        my_cycles.append(dfs(graph, elem))

my_cycles = []
for i, elem in enumerate(xx, start = 1):
    x_flat = [val for sublist in my_cycles for val in sublist]
    if elem not in x_flat:
        my_cycles.append(dfs(graph, elem))        

print(my_cycles)


       