from display_solution import *
import time
import heapq
from heurisitc import *
from successors import *


class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)



def a_star(initial_state):
    frontier = []
    heapq.heappush(frontier, Node(initial_state, None, 0, heuristic(initial_state)))

    while frontier:
        current_node = heapq.heappop(frontier)
        if heuristic(current_node.state) == 0:
            return current_node
        for next_state in successors(current_node.state):
            cost = current_node.cost + 1
            heuristic_val = heuristic(next_state)
            heapq.heappush(frontier, Node(next_state, current_node, cost, heuristic_val))
    
    return None



if __name__ == "__main__":
    initial_state = [0, 1, 2, 3, 4, 5, 6, 7] 
    solution = a_star(initial_state)
    display_solution(solution)
