#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Given: A simple graph with n≤103n≤103 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the sum of the degrees of i's neighbors.
"""

def create_undirected_graph(relations, cardinality):
    graph = {vertex:[] for vertex in range(1,cardinality+1)}
    for relation in relations:
        v1, v2 = relation
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

if __name__ == '__main__':
    with open('rosalind_ddeg.txt') as file:
        number_of_vertices = [int(value) for value in file.readline().split()][0]
        relations = [tuple([int(number) for number in value.split()]) for value in file.readlines()]
    adjacency_list = create_undirected_graph(relations, number_of_vertices)
    result = []
    for neighbors in adjacency_list.values():
        sum_degrees = 0
        for neighbor in neighbors:
               sum_degrees += len(adjacency_list[neighbor])
        result.append(sum_degrees)
    print(' '.join([str(value) for value in result]))
