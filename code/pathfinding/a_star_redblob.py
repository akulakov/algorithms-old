from implementation import *
import collections

def reconstruct_path(came_from, end, current):
    if current != end:
        return [current] + reconstruct_path(came_from, end, came_from[current])
    else:
        return [end]

def heuristic(p1, p2):
    (x1,y1),(x2,y2) = (p1,p2)
    # return math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    return abs(x1-x2) + abs(y1-y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

cf, co = a_star_search(diagram4, (1, 4), (7, 8))
draw_grid(diagram4, width=3, point_to=cf, start=(1, 4), goal=(7, 8))
print()
draw_grid(diagram4, width=3, number=co, start=(1, 4), goal=(7, 8))
print()
p = reconstruct_path(cf, end=(1, 4), current=(7, 8))
# print("p", list(reversed(p)))
# draw_grid(diagram4, width=3, path=reconstruct_path(fr.came_from, end=(1, 4), current=(7, 8)))
draw_grid(diagram4, width=3, path=p)
