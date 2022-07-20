#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
In an undirected graph, the degree d(u) of a vertex u is the number of neighbors 
u has, or equivalently, the number of edges incident upon it.

Given: A simple graph with n≤103 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the degree of vertex i.
"""

def create_undirected_graph(relations, cardinality):
    graph = {vertex:[] for vertex in range(1,cardinality+1)}
    for relation in relations:
        v1, v2 = relation
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

if __name__ == '__main__':
    with open('rosalind_deg.txt') as file:
        number_of_vertices = [int(value) for value in file.readline().split()][0]
        relations = [tuple([int(number) for number in value.split()]) for value in file.readlines()]
    adjacency_list = create_undirected_graph(relations, number_of_vertices)
    print(' '.join([str(len(value)) for value in adjacency_list.values()]))
