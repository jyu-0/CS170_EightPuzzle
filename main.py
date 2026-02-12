import sys
import heapq

# goal state for puzzle (0 is the blank)
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class Node:
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost

    # magic method less than for priority queue to compare nodes
    def __lt__(self, other):
        return self.cost < other.cost

def general_search(problem, queueing_function): 
    # general search algorithm based on the project pseudocode

    # TODO: Implement the search loop
    # nodes = MAKE_QUEUE(MAKE_NODE(problem.INITIAL_STATE))
    # loop do
    #   if EMPTY(nodes) then return "failure"
    #   node = REMOVE_FRONT(nodes)
    #   if GOAL_TEST(node.STATE) succeeds then return node
    #   nodes = QUEUEING_FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
    # end
    return None

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

def expand(node, operators):
    # generates the successors of a node by applying operators (moves).
    successors = []
    # TODO: add the logic to move Blank (0) Up, Down, Left, Right
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
        # TODO: Implement Misplaced Tile logic
        pass
    elif heuristic_mode == 3:
        # TODO: Implement Manhattan Distance logic
        pass
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