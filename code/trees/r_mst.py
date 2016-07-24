#!/usr/bin/env python3

"""Random minimum spanning tree."""

from implementation import *
from random import shuffle, randint

import heapq

class Location:
    def __init__(self):
        self.doors = []
        self.rooms = False
        self.corridor = None

    def __str__(self):
        if self.rooms:
            return '#'
        elif self.corridor==1:
            return '-'  # horizontal
        elif self.corridor==2:
            return '|'  # vertical
        else:
            return ' '

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

class SquareGrid:
    passable = lambda x,y:True

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.weights = {}
        self.grid = [[Location() for _ in range(self.width)] for _ in range(self.height)]

    def __setitem__(self, loc, val):
        self.grid[loc[1]][loc[0]] = val

    def __getitem__(self, loc):
        return self.grid[loc[1]][loc[0]]

    def __iter__(self):
        for y in range(self.height):
            for x in range(self.width):
                yield x,y

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, id):
        (x, y) = id
        results = [(x+2, y), (x, y-2), (x-2, y), (x, y+2)]
        results = filter(self.in_bounds, results)
        results = list(filter(self.passable, results))
        for loc in results:
            if loc not in self.weights:
                self.weights[loc] = randint(1,100)
        return results

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)


def dijkstra_search(graph, start):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

def draw(g):
    for y in range(g.height):
        row = ' '.join(str(x) for x in g.grid[y])
        print(row)
    print()

def make_room_corridors(g, came_from):
    for loc1,loc2 in came_from.items():
        if loc2:
            g[loc1].rooms = g[loc2].rooms = True
            if loc1[0] == loc2[0]:
                y1 = loc1[1]
                y2 = loc2[1]
                sep = min((y1,y2))+1
                g[loc1[0],sep].corridor = 2

            elif loc1[1] == loc2[1]:
                x1 = loc1[0]
                x2 = loc2[0]
                sep = min((x1,x2))+1
                g[sep, loc1[1]].corridor = 1

# g = SquareGrid(30, 15)
# g.walls = DIAGRAM1_WALLS
g=SquareGrid(17, 17 )
came_from, cost_so_far = dijkstra_search(g, (1, 1))
make_room_corridors(g, came_from)

# print("parents", parents)
# draw_grid(g, width=2, point_to=came_from, start=(1, 1), offset=2)
draw(g)
