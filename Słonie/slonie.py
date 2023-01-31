#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:48:15 2021
Example from test files.
INPUT slo1.in:
    elephant numb:         10
    elephant mass:         3015 4728 4802 4361 135 4444 4313 1413 4581 546
    elephant start order:  3 10 1 8 9 4 2 7 6 5
    elephant finall order: 4 9 5 3 1 6 10 7 8 2
OUTPUT slo1.out:
    final value of effort to replace elephants order in optimal way: 30518
@author: lukas
"""
import re
import time
import itertools


def import_date():
    """
    Import data and prepare them for further use.
    Import:
        file .in
    Returns:
        eleph_numb: 10
        eleph_mass: [3015, 4728, 4802, 4361, 135, 4444, 4313, 1413, 4581, 546]
        start_order: [3, 10, 1, 8, 9, 4, 2, 7, 6, 5]
        final_order: [[4], [9], [5], [3], [1], [6], [10], [7], [8], [2]]
        graph_1: {3: [4], 10: [9], 1: [5], 8: [3], 9: [1], 4: [6], 2: [10], 7: [7], 6: [8], 5: [2]}
    """
    # file_ = input()
    lines = []
    with open('zadanie_B/slo4.in', 'r', encoding='UTF-8') as file:
        # with open(str(file_), 'r') as file:
        for line in file:
            line = line.strip()
            line = re.sub(r"\s+", ", ", line.strip())
            line = [int(x) for x in line.split(',')]
            lines.append(line)

    eleph_numb = int(lines[0][0])
    eleph_mass = lines[1]
    start_order = lines[2]
    final_order = [[x] for x in lines[3]]

    # combine start_order with final_order
    graph_1 = dict(zip(start_order, final_order))

    return eleph_numb, eleph_mass, start_order, final_order, graph_1


def dfs(graph_1, start_vertex):
    """DFS graph traversing iterational"""
    visited = set()
    traversal = []
    stack = [start_vertex]
    while stack:  # not empty
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            # add vertex in the same order as visited
            stack.extend(reversed(graph_1[vertex]))
    return traversal


def get_cycles():
    """Use dfs() and getlist() to create cycles list of list"""
    my_cycles = []

    for _, elem in enumerate(start_order_1, start=1):
        # flattening cycle list from [[],[]..] to [..] to prevent
        # faster than  [val for sublist in my_cycles for val in sublist]
        my_cycles_flatted = list(itertools.chain(*my_cycles))
        if elem not in my_cycles_flatted:
            my_cycles.append(dfs(graph, elem))

    return my_cycles


def cycles_param_calculate():
    """
    Calculate cycles parameters
    [[3, 4, 6, 8]]
    """
    # construct cycles using DFS algorithm
    my_cycles = get_cycles()

    total_cycl_mass = {}
    minima_cycl_mass = {}
    min_global = 0

    for i, elem in enumerate(my_cycles, start=1):
        # print(i, elem, "numer i cykl\n")
        suma_c = 0
        list_of_mass = []

        # [list_of_mass.append(eleph_mass_1[i-1]) for i in elem]
        list_of_mass = list(map(lambda i: eleph_mass_1[i-1], elem))

        suma_c = sum(list_of_mass)
        min_c = min(list_of_mass)

        total_cycl_mass[i] = suma_c
        minima_cycl_mass[i] = min_c

        min_global = min(minima_cycl_mass, key=minima_cycl_mass.get)
        min_global = minima_cycl_mass[min_global]

    return total_cycl_mass, minima_cycl_mass, min_global, my_cycles


def counting_result_main():
    """Count  finall result"""
    total_cycl_mass, minima_cycl_mass, min_global, my_cycles = cycles_param_calculate()
    result = []
    for i, elem in enumerate(my_cycles, start=1):
        cmc = total_cycl_mass[i]
        mmwc = minima_cycl_mass[i]
        cycl_lenght = len(elem)

        method_1 = cmc + (abs(cycl_lenght) - 2) * mmwc
        method_2 = cmc + mmwc + (abs(cycl_lenght) + 1) * min_global

        smalle_method_value = min(method_1, method_2)
        result.append(smalle_method_value)

    result = sum(result)
    print(result)


if __name__ == "__main__":
    start = time.time()  # starting time
    eleph_numb_1, eleph_mass_1, start_order_1, final_order_1, graph = import_date()
    counting_result_main()

    end = time.time()  # end time
    print(f"Runtime of the program is {end - start}")  # total time taken
