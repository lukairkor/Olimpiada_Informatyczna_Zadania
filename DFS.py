#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:58:59 2021

@author: lukas
"""

import itertools
import time

# starting time
start = time.time()
# program body starts

licz_sloni = 6
mas_slon = [2400, 2000, 1200, 2400, 1600, 4000]
kol_startowa = [1, 4, 5, 3, 6, 2]
kol_docelowa = [[5], [3], [2], [4], [6], [1]]

masa_sloni = dict(zip(kol_startowa, mas_slon))
graph = dict(zip(kol_startowa, kol_docelowa))
# print(graph)
visited = set() # Set to keep track of visited nodes.
my_cycles = []


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


def aaa(j):
    p = []
    for i in range(1, licz_sloni + 1):
        cycl = dfs_it(graph, j, i, p)
        my_cycles.append(cycl)
        
for i in range(1, 7):
    aaa(i)

    
my_cycles.sort()
my_cycles = list(k for k,_ in itertools.groupby(my_cycles))
    
# print("\nCycles: \n", my_cycles)

# end time
end = time.time()
# total time taken
print(f"Runtime of the program is {end - start}")
