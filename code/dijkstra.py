#!/usr/bin/env python
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
            print("e,priority", e,priority)
            # self.elements.append(e)
            heapq.heappush(self.elements, (priority, self.id, e))
            self.id += 1
            self.came_from[e] = previous

    def get(self):
        elem = heapq.heappop(self.elements)
        print(elem)
        return elem[2]


def dijkstra(graph, start, goal):
    def need_to_visit(next, current):
        """Return (node, cost) tuple if need to visit `next`;
        also updates `cost_so_far[next]`."""
        cost_so_far = frontier.cost_so_far
        cost = cost_so_far[current] + graph.cost(current, next)
        if next not in cost_so_far or cost < cost_so_far[next]:
            cost_so_far[next] = cost
            return next, cost

    def unvisited_neighbors(current):
        """Unvisited (or better path to visited) neighbors."""
        print("current", current)
        for n in graph.neighbors(current):
            val = need_to_visit(n, current)
            if val:
                yield val
    # frontier keeps track of active nodes on the "frontier" as well as a dictionary of already visited nodes
    frontier = FrontierQueue(start)     # create frontier with a single starting node

    while frontier:
        current = frontier.get()
        frontier.put(unvisited_neighbors(current), previous=current)  # add unvisited neighbors to the frontier
    return frontier

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def reconstruct_path(came_from, end, current, path=None):
    path = path or [current]
    if current == end:
        return reversed(path + [end])
    else:
        return reconstruct_path(came_from, end, came_from[current], path + [current])

def reconstruct_path(came_from, end, current):
    if current != end:
        return [current] + reconstruct_path(came_from, end, came_from[current])
    else:
        return [end]

fr = dijkstra(diagram4, (1, 4), (7, 8))
draw_grid(diagram4, width=3, point_to=fr.came_from, start=(1, 4), goal=(7, 8))
print()
draw_grid(diagram4, width=3, number=fr.cost_so_far, start=(1, 4), goal=(7, 8))
print()
p = reconstruct_path(fr.came_from, end=(1, 4), current=(7, 8))
print("p", list(reversed(p)))
# draw_grid(diagram4, width=3, path=reconstruct_path(fr.came_from, end=(1, 4), current=(7, 8)))
draw_grid(diagram4, width=3, path=p)
