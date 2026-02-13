import sys
import heapq
import copy

# goal state for puzzle (0 is the blank)
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class Node:
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost
        self.h = 0

    # magic method less than for priority queue to compare nodes
    def __lt__(self, other):
        return self.cost < other.cost

def general_search(initial_state, mode): 
    # general search algorithm based on the project pseudocode

    # nodes = MAKE_QUEUE(MAKE_NODE(problem.INITIAL_STATE))
    # loop do
    #   if EMPTY(nodes) then return "failure"
    #   node = REMOVE_FRONT(nodes)
    #   if GOAL_TEST(node.STATE) succeeds then return node
    #   nodes = QUEUEING_FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
    # end

    visited = set() 
    
    #initial node
    root = make_node(initial_state)
    root.h = calculate_heuristic(root.state, mode)
    root.cost = root.depth + root.h # f(n) = g(n) + h(n)
    
    nodes = make_queue(root)
    num_expanded = 0
    max_queue_size = 1

    while True:
        if not nodes:
            return "failure"
        
        node = remove_front(nodes)
        
        print(f"The best state to expand with g(n) = {node.depth} and h(n) = {node.h} is...")
        for row in node.state:
            print(row)
        
        # check if goal state is reached
        if goal_test(node.state):
            print(f"\nGoal reached! Depth: {node.depth}, Nodes expanded: {num_expanded}")
            return node
        
        # convert state to tuple to store in 'visited' set
        state_tuple = tuple(tuple(row) for row in node.state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        num_expanded += 1
        for child in expand(node):
            child.h = calculate_heuristic(child.state, mode)
            child.cost = child.depth + child.h
            queueing_function(nodes, [child])
        
        max_queue_size = max(max_queue_size, len(nodes))

def make_node(state):
    # creates a node with state
    return Node(state, None, None, 0, 0)

def make_queue(node):
    # initializes the queue with the first node
    queue = []
    heapq.heappush(queue, node)
    return queue

def remove_front(nodes):
    # removes and returns the node with the lowest cost (g + h)
    return heapq.heappop(nodes)

def goal_test(state):
    # check if the current state matches the goal 
    return state == GOAL_STATE

def expand(node):
    # generates the successors of a node by applying operators (moves).
    successors = []
    state = node.state
    size = len(state)
    
    # 1. find where blank, 0 is
    blank_r, blank_c = -1, -1
    for r in range(size):
        for c in range(size):
            if state[r][c] == 0:
                blank_r, blank_c = r, c
                break

    # 2. define the moves (row_change, col_change)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_r, new_c = blank_r + dr, blank_c + dc
        
        if 0 <= new_r < size and 0 <= new_c < size:
            # create copy so we don't mess up the original state
            new_state = copy.deepcopy(state)
            
            # swap blank and new position
            new_state[blank_r][blank_c], new_state[new_r][new_c] = \
                new_state[new_r][new_c], new_state[blank_r][blank_c]
            
            # create the child node and increase depth by 1 for every mov
            child = Node(state=new_state, parent=node, operator=None, 
                         depth=node.depth + 1, cost=0)
            successors.append(child)
            
    return successors

def queueing_function(nodes, new_nodes):
    # add new nodes to the queue, the sorting is done by the heap 
    for node in new_nodes:
        heapq.heappush(nodes, node)
    return nodes

def calculate_heuristic(state, heuristic_mode):
    # Calculates h(n) based on the selected mode:
    # 1: Uniform Cost Search (h = 0)
    # 2: Misplaced Tile Heuristic
    # 3: Manhattan Distance Heuristic
    if heuristic_mode == 1:
        return 0
    elif heuristic_mode == 2:
        # count number of tiles are in wrong position
        misplaced_count = 0
        for i in range(3):
            for j in range(3):
                # blank (0) does not count as misplaced
                if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                    misplaced_count += 1
        return misplaced_count
    elif heuristic_mode == 3:
        # sum Manhattan distance for each tile
        manhattan_distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:  # skip blank tile (0)  
                    tile = state[i][j]
                    # find where tile should be in goal state
                    goal_i = (tile - 1) // 3
                    goal_j = (tile - 1) % 3
                    # add the Manhattan distance (abs diff in rows + cols)
                    manhattan_distance += abs(i - goal_i) + abs(j - goal_j)
        return manhattan_distance
    return 0

def main():
    print("Welcome to 8-Puzzle Solver.")
    choice = input("Type '1' to use a default puzzle, or '2' to create your own: ")
    
    initial_state = []
    
    if choice == '1':
        # TODO: default puzzle dictionary
        print("Using default puzzle...")
        initial_state = [[1, 2, 3], [4, 8, 0], [7, 6, 5]] # example of puzzle
    elif choice == '2': 
        print("Enter your puzzle, use a zero to represent the blank.")
        row1 = list(map(int, input("Enter the first row, use space or tabs between numbers: ").split()))
        row2 = list(map(int, input("Enter the second row, use space or tabs between numbers: ").split()))
        row3 = list(map(int, input("Enter the third row, use space or tabs between numbers: ").split()))
        initial_state = [row1, row2, row3]
        
    algo_choice = int(input("Enter choice of algorithm\n1. Uniform Cost Search\n2. A* with the Misplaced Tile heuristic.\n3. A* with the Manhattan distance heuristic.\n"))
    
    result = general_search(initial_state, algo_choice)
    
    if result:
        print("Goal Reached!")
    else:
        print("Failure")

if __name__ == "__main__":
    main()