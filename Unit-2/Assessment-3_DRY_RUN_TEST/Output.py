Q1 – A* Search Algorithm
import heapq

# Graph
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 3, 'D': 7, 'E': 2},
    'C': {'A': 4, 'B': 3, 'E': 3},
    'D': {'B': 7, 'E': 2, 'G': 2},
    'E': {'B': 2, 'C': 3, 'D': 2},
    'G': {'D': 2}
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'G': 0
}

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    g = {node: float('inf') for node in graph}
    g[start] = 0

    parent = {}
    closed = set()

    while open_list:
        f, current = heapq.heappop(open_list)

        if current in closed:
            continue

        print("\nCurrent Node:", current)
        print("g(n):", g[current])
        print("h(n):", heuristic[current])
        print("f(n):", g[current] + heuristic[current])

        if current == goal:
            break

        closed.add(current)

        for neighbour, cost in graph[current].items():
            new_g = g[current] + cost

            if new_g < g[neighbour]:
                g[neighbour] = new_g
                parent[neighbour] = current

                new_f = new_g + heuristic[neighbour]
                heapq.heappush(open_list, (new_f, neighbour))

    # Construct path
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    print("\nOptimal Path:", " -> ".join(path))
    print("Total Path Cost:", g[goal])


# Run A* Search
astar('A', 'G')
Q2 – Minimax with Alpha-Beta Pruning
import math

# Game Tree
tree = {
    "A": ["B", "C"],      # MAX
    "B": [3, 5, 6],       # MIN
    "C": [9, 1, 2]        # MIN
}

pruned = []

def minimax(node, alpha, beta, maximizing):

    # Leaf node
    if isinstance(node, int):
        print("Leaf:", node, "Alpha:", alpha, "Beta:", beta)
        return node

    # MAX node
    if maximizing:
        value = -math.inf

        for child in tree[node]:
            value = max(value, minimax(child, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    # MIN node
    else:
        value = math.inf

        children = tree[node]

        for i, child in enumerate(children):
            value = min(value, minimax(child, alpha, beta, True))
            beta = min(beta, value)

            if beta <= alpha:
                pruned.extend(children[i + 1:])
                break

        return value


# Run Minimax with Alpha-Beta Pruning
result = minimax("A", -math.inf, math.inf, True)

print("\nFinal Minimax Value:", result)

if result == 3:
    print("Best Move for MAX: Left Subtree")
else:
    print("Best Move for MAX: Right Subtree")

print("Pruned Nodes:", pruned)