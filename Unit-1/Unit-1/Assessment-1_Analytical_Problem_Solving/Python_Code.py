# ===========================
# PROGRAM 1 : WATER JUG PROBLEM
# ===========================

print("\n==============================")
print("PROGRAM 1 : WATER JUG PROBLEM")
print("==============================")

jug4 = 0
jug3 = 0

print("Initial State:", (jug4, jug3))

jug4 = 4
print("Fill 4-Gallon Jug      ->", (jug4, jug3))

jug4 = 1
jug3 = 3
print("Pour 4G -> 3G          ->", (jug4, jug3))

jug3 = 0
print("Empty 3-Gallon Jug     ->", (jug4, jug3))

jug3 = 1
jug4 = 0
print("Pour Remaining to 3G   ->", (jug4, jug3))

jug4 = 4
print("Fill 4-Gallon Jug      ->", (jug4, jug3))

jug4 = 2
jug3 = 3
print("Pour 4G -> 3G          ->", (jug4, jug3))

print("Goal Achieved!")
print("The 4-Gallon Jug contains exactly 2 gallons.")


# ===========================
# PROGRAM 2 : MARS ROVER
# ===========================

print("\n==============================")
print("PROGRAM 2 : MARS ROVER")
print("==============================")

class MarsRover:
    def __init__(self):
        self.percepts = [
            "Camera Images",
            "Rock Samples",
            "Soil Samples",
            "Temperature",
            "Atmospheric Pressure",
            "Obstacle Detection",
            "Battery Status"
        ]

        self.actions = [
            "Move Forward",
            "Turn Left",
            "Turn Right",
            "Collect Sample",
            "Capture Image",
            "Analyze Sample",
            "Transmit Data"
        ]

        self.performance = [
            "Accurate Sample Collection",
            "Safe Navigation",
            "Efficient Battery Usage",
            "Mission Completion"
        ]

        self.agent = "Goal-Based Agent"

    def display(self):
        print("\nPercepts:")
        for i in self.percepts:
            print("-", i)

        print("\nActions:")
        for i in self.actions:
            print("-", i)

        print("\nPerformance Measures:")
        for i in self.performance:
            print("-", i)

        print("\nSuitable Agent:", self.agent)

rover = MarsRover()
rover.display()


# ===========================
# PROGRAM 3 : 8 QUEENS
# ===========================

print("\n==============================")
print("PROGRAM 3 : 8 QUEENS")
print("==============================")

N = 8
board = [-1] * N

def safe(row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve(col):
    if col == N:
        return True

    for row in range(N):
        if safe(row, col):
            board[col] = row
            if solve(col + 1):
                return True
    return False

if solve(0):
    print("\nSolution Board:\n")

    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

    print("\nQueen Positions:", board)


# ===========================
# PROGRAM 4 : OLA CAB BOOKING
# ===========================

print("\n==============================")
print("PROGRAM 4 : OLA CAB BOOKING")
print("==============================")

pickup = input("Enter Pickup Location: ")
destination = input("Enter Destination: ")
cab = input("Enter Cab Type (Mini/Micro/Sedan/Prime): ")

print("\n------ OLA CAB BOOKING ------")
print("Pickup Location :", pickup)
print("Destination     :", destination)
print("Cab Type        :", cab)
print("Booking Status  : Confirmed")
print("Driver Assigned : Available Driver")
print("Have a Safe Journey!")


# ===========================
# PROGRAM 5 : LEAST COST SEARCH
# ===========================

print("\n==============================")
print("PROGRAM 5 : LEAST COST SEARCH")
print("==============================")

from queue import PriorityQueue

graph = {
    'S': [('A', 2), ('B', 5)],
    'A': [('C', 4), ('D', 7)],
    'B': [('D', 2)],
    'C': [('G', 3)],
    'D': [('G', 1)],
    'G': []
}

pq = PriorityQueue()
pq.put((0, 'S', ['S']))

visited = set()

while not pq.empty():
    cost, node, path = pq.get()

    if node == 'G':
        print("Least Cost Path:", " -> ".join(path))
        print("Total Cost:", cost)
        break

    if node not in visited:
        visited.add(node)

        for next_node, weight in graph[node]:
            pq.put((cost + weight, next_node, path + [next_node]))
