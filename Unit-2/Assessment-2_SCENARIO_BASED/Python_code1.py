# ============================================================
# ASSESSMENT TOOL 2 - SCENARIO BASED ASSIGNMENT
# CO2: Search and Game-Solving Techniques
# Q1 - Greedy Best-First Search and A*
# Q2 - Hill Climbing, Simulated Annealing and Genetic Algorithm
# Q3 - Online Search Agent
# Q4 - Constraint Satisfaction Problem (CSP)
# Q5 - Minimax and Alpha-Beta Pruning
# ============================================================

import heapq
import random
import math
# ============================================================
# QUESTION 1
# AI-POWERED DRONE NAVIGATION
# Greedy Best-First Search and A* Search
# ============================================================
def drone_search_algorithms():
    print("\n" + "=" * 70)
    print("QUESTION 1: AI-POWERED DRONE NAVIGATION")
    print("=" * 70)
    # Graph representing locations in a flood-affected region.
    # Each edge contains the travel cost considering terrain/weather.
    graph = {
        "Start": [("A", 4), ("B", 2)],
        "A": [("Start", 4), ("C", 3), ("D", 5)],
        "B": [("Start", 2), ("D", 7), ("E", 4)],
        "C": [("A", 3), ("Goal", 5)],
        "D": [("A", 5), ("B", 7), ("Goal", 2)],
        "E": [("B", 4), ("Goal", 3)],
        "Goal": []
    }
    # Straight-line heuristic estimate to the destination.
    heuristic = {
        "Start": 8,
        "A": 6,
        "B": 5,
        "C": 4,
        "D": 2,
        "E": 3,
        "Goal": 0
    }

    # --------------------------------------------------------
    # Greedy Best-First Search
    # --------------------------------------------------------
    def greedy_best_first_search(start, goal):
        priority_queue = [(heuristic[start], start)]
        visited = set()
        parent = {start: None}

        while priority_queue:
            _, current = heapq.heappop(priority_queue)

            if current in visited:
                continue

            visited.add(current)

            if current == goal:
                break

            for neighbor, _ in graph[current]:
                if neighbor not in visited:
                    parent[neighbor] = current
                    heapq.heappush(
                        priority_queue,
                        (heuristic[neighbor], neighbor)
                    )

        if goal not in parent:
            return [], 0

        path = []
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

        cost = 0
        for i in range(len(path) - 1):
            for node, edge_cost in graph[path[i]]:
                if node == path[i + 1]:
                    cost += edge_cost
                    break

        return path, cost

    # --------------------------------------------------------
    # A* Search
    # --------------------------------------------------------
    def a_star_search(start, goal):
        priority_queue = [(heuristic[start], 0, start)]
        parent = {start: None}
        g_cost = {start: 0}

        while priority_queue:
            _, current_cost, current = heapq.heappop(priority_queue)

            if current == goal:
                break

            for neighbor, edge_cost in graph[current]:
                new_cost = current_cost + edge_cost

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    parent[neighbor] = current

                    f_cost = new_cost + heuristic[neighbor]

                    heapq.heappush(
                        priority_queue,
                        (f_cost, new_cost, neighbor)
                    )

        if goal not in parent:
            return [], 0

        path = []
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

        return path, g_cost[goal]

    greedy_path, greedy_cost = greedy_best_first_search("Start", "Goal")
    astar_path, astar_cost = a_star_search("Start", "Goal")

    print("\nGreedy Best-First Search")
    print("Path:", " -> ".join(greedy_path))
    print("Travel Cost:", greedy_cost)

    print("\nA* Search")
    print("Path:", " -> ".join(astar_path))
    print("Travel Cost:", astar_cost)

    print("\nComparison")
    print("Greedy Search uses heuristic only.")
    print("A* uses actual cost + heuristic.")
    print("A* is preferred when safety, cost and optimality are important.")


# ============================================================
# QUESTION 2
# SMART CITY TRAFFIC SIGNAL OPTIMIZATION
# Hill Climbing, Simulated Annealing and Genetic Algorithm
# ============================================================

def traffic_cost(solution):
    """
    Lower cost represents better traffic performance.

    Each value represents the green-light duration at an
    intersection.
    """

    target = [45, 50, 40, 55]

    waiting_time = sum(
        abs(solution[i] - target[i]) * 2
        for i in range(len(solution))
    )

    fuel_consumption = sum(
        (solution[i] - target[i]) ** 2 * 0.1
        for i in range(len(solution))
    )

    congestion = sum(
        abs(solution[i] - target[i])
        for i in range(len(solution))
    )

    total_cost = (
        waiting_time
        + fuel_consumption
        + congestion
    )

    return total_cost


def hill_climbing(initial_solution):
    current = initial_solution[:]

    while True:
        current_cost = traffic_cost(current)

        neighbors = []

        for i in range(len(current)):
            for change in [-5, 5]:
                neighbor = current[:]
                neighbor[i] += change

                if 20 <= neighbor[i] <= 90:
                    neighbors.append(neighbor)

        if not neighbors:
            break

        best_neighbor = min(
            neighbors,
            key=traffic_cost
        )

        if traffic_cost(best_neighbor) < current_cost:
            current = best_neighbor
        else:
            break

    return current


def simulated_annealing(initial_solution):
    current = initial_solution[:]
    current_cost = traffic_cost(current)

    temperature = 100.0

    while temperature > 0.1:

        neighbor = current[:]

        index = random.randint(0, len(neighbor) - 1)
        change = random.choice([-5, 5])

        neighbor[index] += change

        if not 20 <= neighbor[index] <= 90:
            temperature *= 0.95
            continue

        neighbor_cost = traffic_cost(neighbor)

        difference = neighbor_cost - current_cost

        if difference < 0:
            current = neighbor
            current_cost = neighbor_cost

        else:
            probability = math.exp(
                -difference / temperature
            )

            if random.random() < probability:
                current = neighbor
                current_cost = neighbor_cost

        temperature *= 0.95

    return current


def genetic_algorithm():
    population_size = 20
    generations = 50
    chromosome_length = 4

    def create_solution():
        return [
            random.randint(20, 90)
            for _ in range(chromosome_length)
        ]

    population = [
        create_solution()
        for _ in range(population_size)
    ]

    for generation in range(generations):

        population.sort(
            key=traffic_cost
        )

        survivors = population[:10]

        new_population = survivors[:]

        while len(new_population) < population_size:

            parent1 = random.choice(survivors)
            parent2 = random.choice(survivors)

            crossover_point = random.randint(
                1,
                chromosome_length - 1
            )

            child = (
                parent1[:crossover_point]
                + parent2[crossover_point:]
            )

            # Mutation
            if random.random() < 0.2:
                index = random.randint(
                    0,
                    chromosome_length - 1
                )

                child[index] += random.choice(
                    [-5, 5]
                )

                child[index] = max(
                    20,
                    min(90, child[index])
                )

            new_population.append(child)

        population = new_population

    population.sort(key=traffic_cost)

    return population[0]


def traffic_signal_optimization():
    print("\n" + "=" * 70)
    print("QUESTION 2: SMART CITY TRAFFIC SIGNAL OPTIMIZATION")
    print("=" * 70)

    initial_solution = [30, 30, 70, 70]

    print("\nInitial Signal Timings:")
    print(initial_solution)

    print("\nInitial Traffic Cost:")
    print(round(traffic_cost(initial_solution), 2))

    hill_solution = hill_climbing(initial_solution)

    print("\nHill Climbing Result:")
    print("Signal Timings:", hill_solution)
    print("Traffic Cost:", round(traffic_cost(hill_solution), 2))

    random.seed(42)

    annealing_solution = simulated_annealing(
        initial_solution
    )

    print("\nSimulated Annealing Result:")
    print("Signal Timings:", annealing_solution)
    print(
        "Traffic Cost:",
        round(traffic_cost(annealing_solution), 2)
    )

    random.seed(42)

    genetic_solution = genetic_algorithm()

    print("\nGenetic Algorithm Result:")
    print("Signal Timings:", genetic_solution)
    print(
        "Traffic Cost:",
        round(traffic_cost(genetic_solution), 2)
    )

    print("\nRecommendation:")
    print(
        "Genetic Algorithm is suitable for large traffic "
        "optimization problems because it explores multiple "
        "solutions and reduces the risk of getting trapped "
        "in local optima."
    )


# ============================================================
# QUESTION 3
# AUTONOMOUS MARS ROVER
# ONLINE SEARCH AGENT
# ============================================================

def mars_rover_online_search():
    print("\n" + "=" * 70)
    print("QUESTION 3: AUTONOMOUS MARS ROVER")
    print("=" * 70)

    # Unknown environment.
    # The rover discovers the environment while moving.
    environment = {
        "Start": ["A", "B"],
        "A": ["Start", "C"],
        "B": ["Start", "D"],
        "C": ["A", "Goal"],
        "D": ["B", "E"],
        "E": ["D", "Goal"],
        "Goal": []
    }

    # Initially the rover knows only the starting location.
    discovered_map = {
        "Start": ["A", "B"]
    }

    current = "Start"
    goal = "Goal"

    path = [current]

    print("\nInitial Rover Knowledge:")
    print(discovered_map)

    while current != goal:

        possible_moves = environment[current]

        print("\nRover is currently at:", current)
        print("Newly observed locations:", possible_moves)

        # Update internal model.
        discovered_map[current] = possible_moves

        if goal in possible_moves:
            current = goal
            path.append(current)
            break

        # Select an unexplored safe location.
        next_location = None

        for location in possible_moves:
            if location not in path:
                next_location = location
                break

        if next_location is None:
            break

        current = next_location
        path.append(current)

    print("\nUpdated Internal Model:")
    for location, neighbors in discovered_map.items():
        print(location, "->", neighbors)

    print("\nOnline Search Path:")
    print(" -> ".join(path))

    print("\nConclusion:")
    print(
        "Online search is suitable because the rover does not "
        "have a complete map and must continuously update its "
        "knowledge while exploring."
    )


# ============================================================
# QUESTION 4
# UNIVERSITY EXAM TIMETABLE
# CONSTRAINT SATISFACTION PROBLEM
# Backtracking + Forward Checking
# ============================================================

def exam_timetable_csp():
    print("\n" + "=" * 70)
    print("QUESTION 4: UNIVERSITY EXAM TIMETABLE USING CSP")
    print("=" * 70)

    subjects = [
        "Mathematics",
        "Physics",
        "Chemistry",
        "ComputerScience"
    ]

    time_slots = [
        "Monday-Morning",
        "Monday-Afternoon",
        "Tuesday-Morning",
        "Tuesday-Afternoon"
    ]

    # Students enrolled in each subject.
    students = {
        "Mathematics": {"S1", "S2", "S3"},
        "Physics": {"S2", "S4"},
        "Chemistry": {"S1", "S5"},
        "ComputerScience": {"S3", "S4", "S5"}
    }

    # Example precedence constraint:
    # Mathematics must be scheduled before Computer Science.
    precedence = {
        "ComputerScience": "Mathematics"
    }

    assignment = {}

    domains = {
        subject: time_slots[:]
        for subject in subjects
    }

    def has_student_conflict(subject, slot):
        for assigned_subject, assigned_slot in assignment.items():

            if assigned_slot == slot:

                if students[subject].intersection(
                    students[assigned_subject]
                ):
                    return True

        return False

    def satisfies_precedence(subject, slot):
        if subject not in precedence:
            return True

        prerequisite = precedence[subject]

        if prerequisite not in assignment:
            return True

        return (
            time_slots.index(
                assignment[prerequisite]
            )
            <
            time_slots.index(slot)
        )

    def forward_check():
        for subject in subjects:

            if subject in assignment:
                continue

            valid_values = []

            for slot in domains[subject]:

                if has_student_conflict(subject, slot):
                    continue

                if not satisfies_precedence(subject, slot):
                    continue

                valid_values.append(slot)

            if not valid_values:
                return False

        return True

    def backtracking_search():

        if len(assignment) == len(subjects):
            return True

        # Minimum Remaining Values strategy.
        unassigned = [
            subject
            for subject in subjects
            if subject not in assignment
        ]

        subject = min(
            unassigned,
            key=lambda s: len(domains[s])
        )

        original_domain = domains[subject][:]

        for slot in original_domain:

            if has_student_conflict(subject, slot):
                continue

            assignment[subject] = slot

            if satisfies_precedence(
                subject,
                slot
            ) and forward_check():

                if backtracking_search():
                    return True

            del assignment[subject]

        return False

    success = backtracking_search()

    if success:

        print("\nValid Exam Timetable Found:")

        for subject in subjects:
            print(
                f"{subject:20} -> "
                f"{assignment[subject]}"
            )

        print("\nCSP Constraints Satisfied:")
        print("1. No student has overlapping exams.")
        print("2. Each subject has one time slot.")
        print("3. Mathematics is scheduled before Computer Science.")
        print("4. Forward checking reduces invalid choices.")

    else:
        print("\nNo valid timetable found.")

    print("\nRecommended Strategy:")
    print(
        "Backtracking Search with Forward Checking is "
        "appropriate for solving the timetable CSP."
    )


# ============================================================
# QUESTION 5
# STRATEGIC GAME AI
# MINIMAX AND ALPHA-BETA PRUNING
# ============================================================

def minimax_without_pruning(node, maximizing_player):
    """
    Simple Minimax implementation.

    Leaf nodes contain numerical evaluation scores.
    Internal nodes contain child nodes.
    """

    if isinstance(node, int):
        return node

    if maximizing_player:
        best_value = float("-inf")

        for child in node:
            value = minimax_without_pruning(
                child,
                False
            )

            best_value = max(
                best_value,
                value
            )

        return best_value

    else:
        best_value = float("inf")

        for child in node:
            value = minimax_without_pruning(
                child,
                True
            )

            best_value = min(
                best_value,
                value
            )

        return best_value


def alpha_beta_pruning(
    node,
    maximizing_player,
    alpha,
    beta
):
    """
    Minimax with Alpha-Beta pruning.
    Returns:
        best value,
        number of evaluated leaf nodes
    """

    if isinstance(node, int):
        return node, 1

    evaluated_nodes = 0

    if maximizing_player:

        best_value = float("-inf")

        for child in node:

            value, count = alpha_beta_pruning(
                child,
                False,
                alpha,
                beta
            )

            evaluated_nodes += count

            best_value = max(
                best_value,
                value
            )

            alpha = max(
                alpha,
                best_value
            )

            if beta <= alpha:
                break

        return best_value, evaluated_nodes

    else:

        best_value = float("inf")

        for child in node:

            value, count = alpha_beta_pruning(
                child,
                True,
                alpha,
                beta
            )

            evaluated_nodes += count

            best_value = min(
                best_value,
                value
            )

            beta = min(
                beta,
                best_value
            )

            if beta <= alpha:
                break

        return best_value, evaluated_nodes


def game_evaluation_function(
    soldiers,
    health,
    resources,
    distance_to_enemy,
    territory,
    remaining_time
):
    """
    Example evaluation function for a strategy game.

    Higher score = better position for the AI.
    """

    score = (
        soldiers * 2
        + health * 1.5
        + resources * 1.2
        - distance_to_enemy * 0.5
        + territory * 2
        + remaining_time * 0.2
    )

    return score


def strategic_game_ai():
    print("\n" + "=" * 70)
    print("QUESTION 5: STRATEGIC GAME AI")
    print("=" * 70)

    # Game tree.
    #
    # MAX represents the AI.
    # MIN represents the human opponent.
    #
    # Each leaf contains an evaluation score.

    game_tree = [
        [
            [3, 5],
            [6, 9]
        ],
        [
            [1, 2],
            [0, 4]
        ],
        [
            [7, 8],
            [5, 6]
        ]
    ]

    minimax_value = minimax_without_pruning(
        game_tree,
        True
    )

    alpha_beta_value, evaluated_nodes = alpha_beta_pruning(
        game_tree,
        True,
        float("-inf"),
        float("inf")
    )

    print("\nMinimax Result:")
    print("Best Game Value:", minimax_value)

    print("\nAlpha-Beta Pruning Result:")
    print("Best Game Value:", alpha_beta_value)
    print("Evaluated Leaf Nodes:", evaluated_nodes)

    print("\nEvaluation Function Example:")

    score = game_evaluation_function(
        soldiers=50,
        health=80,
        resources=60,
        distance_to_enemy=20,
        territory=40,
        remaining_time=90
    )

    print("Game State Score:", round(score, 2))

    print("\nEvaluation Factors:")
    print("1. Number of soldiers")
    print("2. Health of units")
    print("3. Resources collected")
    print("4. Distance to enemy")
    print("5. Territory controlled")
    print("6. Remaining time")

    print("\nRecommendation:")
    print(
        "Minimax with Alpha-Beta Pruning is recommended "
        "because it produces the same optimal decision as "
        "Minimax while avoiding unnecessary branches."
    )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("\n")
    print("=" * 70)
    print("SIMATS ENGINEERING")
    print("ASSESSMENT TOOL 2 - ARTIFICIAL INTELLIGENCE")
    print("COURSE CODE: CSA17")
    print("SCENARIO BASED ASSIGNMENT")
    print("=" * 70)

    # Execute all five questions.

    drone_search_algorithms()

    traffic_signal_optimization()

    mars_rover_online_search()

    exam_timetable_csp()

    strategic_game_ai()

    print("\n" + "=" * 70)
    print("ALL FIVE SCENARIO-BASED AI PROGRAMS EXECUTED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()
