from itertools import permutations
import sys

def calculate_shortest_path(graph):
    shortest_path = ()
    lowest_cost = sys.maxsize
    vertices = list(graph.vertices)
    g = graph.graph
    all_visit_orders = permutations(vertices)
    for visit_order in all_visit_orders:
        cost = 0
        for i in range(len(visit_order) - 1):
            src_city = visit_order[i]
            dest_city = visit_order[i + 1]
            cost += g[src_city][dest_city]
        if cost < lowest_cost:
            lowest_cost = cost
            shortest_path = visit_order
    return lowest_cost, shortest_path



