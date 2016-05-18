#!/usr/bin/env python
import math
from implementation import *
import collections

class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]

class FrontierQueue:
    def __init__(self, start=None):
        self.elements = []
        self.came_from = {}
        self.cost_so_far = {}
        self.id = 1
        if start is not None:
            self.cost_so_far[start] = 1
            start_tup = start, 0
            self.put([start_tup], None)

    def __bool__(self):
        return len(self.elements)>0

    def put(self, items, previous):
        for e, priority in items:
            heapq.heappush(self.elements, (priority, self.id, e))
            self.id += 1
            self.came_from[e] = previous

    def get(self):
        elem = heapq.heappop(self.elements)
        return elem[2]

def heuristic(p1, p2):
    (x1,y1),(x2,y2) = (p1,p2)
    # return math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    return abs(x1-x2) + abs(y1-y2)

def a_star(graph, start, goal):
    def need_to_visit(next, current):
        """Return (node, cost) tuple if need to visit `next`;
        also updates `cost_so_far[next]`."""
        cost_so_far = frontier.cost_so_far
        cost = cost_so_far[current] + graph.cost(current, next)
        if next not in cost_so_far or cost < cost_so_far[next]:
            cost_so_far[next] = cost
            return next, cost + heuristic(next, goal)*10

    def unvisited_neighbors(current):
        """Unvisited (or better path to visited) neighbors."""
        # print("current", current)
        for n in graph.neighbors(current):
            val = need_to_visit(n, current)
            if val:
                yield val
    # frontier keeps track of active nodes on the "frontier" as well as a dictionary of already visited nodes
    frontier = FrontierQueue(start)     # create frontier with a single starting node

    while frontier:
        current = frontier.get()
        if current == goal:
            return frontier
        frontier.put(unvisited_neighbors(current), previous=current)  # add unvisited neighbors to the frontier
    return frontier


def reconstruct_path(came_from, end, current):
    if current != end:
        return [current] + reconstruct_path(came_from, end, came_from[current])
    else:
        return [end]

f_queue = a_star(diagram4, (1, 4), (7, 8))
# draw_grid(diagram4, width=3, point_to=f_queue.came_from, start=(1, 4), goal=(7, 8))
print()
# draw_grid(diagram4, width=3, number=f_queue.cost_so_far, start=(1, 4), goal=(7, 8))
print()
p = reconstruct_path(f_queue.came_from, end=(1, 4), current=(7, 8))
# print("p", list(reversed(p)))
# draw_grid(diagram4, width=3, path=reconstruct_path(fr.came_from, end=(1, 4), current=(7, 8)))
# draw_grid(diagram4, width=3, path=p)
