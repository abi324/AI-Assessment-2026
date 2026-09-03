# PYTHON PROGRAMS – RESOLUTION ALGORITHM

## Question 1 – Rain and Wet Ground

```python
# Resolution Algorithm - Rain and Wet Ground

def resolve(clause1, clause2):
    resolvents = []

    for literal in clause1:
        opposite = literal[1:] if literal.startswith("~") else "~" + literal

        if opposite in clause2:
            new_clause = (clause1 - {literal}) | (clause2 - {opposite})
            resolvents.append(new_clause)

    return resolvents


def resolution(clauses, goal):
    clauses = [set(clause) for clause in clauses]

    # Add negation of goal
    negated_goal = "~" + goal if not goal.startswith("~") else goal[1:]
    clauses.append({negated_goal})

    print("\nInitial Clauses:")
    for i, clause in enumerate(clauses, 1):
        print(f"C{i} = {clause}")

    while True:
        new_clauses = []

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):

                for resolvent in resolve(clauses[i], clauses[j]):

                    print(
                        f"Resolve C{i + 1} and C{j + 1} -> "
                        f"{resolvent if resolvent else 'EMPTY CLAUSE'}"
                    )

                    if not resolvent:
                        return True

                    if resolvent not in clauses and resolvent not in new_clauses:
                        new_clauses.append(resolvent)

        if not new_clauses:
            return False

        clauses.extend(new_clauses)


# Knowledge Base
clauses = [
    {"~R", "W"},
    {"R"}
]

goal = "W"

print("===== RESOLUTION: RAIN AND WET GROUND =====")

result = resolution(clauses, goal)

if result:
    print("\nConclusion: Ground is Wet - PROVED.")
else:
    print("\nConclusion: Goal cannot be proved.")
```

### Expected Conclusion

**Ground is Wet – PROVED.**

---

# Question 2 – Student Assignment Submission

```python
# Resolution Algorithm - Student Assignment

def resolve(clause1, clause2):
    resolvents = []

    for literal in clause1:
        opposite = literal[1:] if literal.startswith("~") else "~" + literal

        if opposite in clause2:
            new_clause = (clause1 - {literal}) | (clause2 - {opposite})
            resolvents.append(new_clause)

    return resolvents


def resolution(clauses, goal):
    clauses = [set(c) for c in clauses]

    negated_goal = "~" + goal if not goal.startswith("~") else goal[1:]
    clauses.append({negated_goal})

    print("\nInitial Clauses:")

    for i, clause in enumerate(clauses, 1):
        print(f"C{i} = {clause}")

    while True:
        new_clauses = []

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):

                for resolvent in resolve(clauses[i], clauses[j]):

                    print(
                        f"Resolve C{i + 1} and C{j + 1} -> "
                        f"{resolvent if resolvent else 'EMPTY CLAUSE'}"
                    )

                    if not resolvent:
                        return True

                    if resolvent not in clauses and resolvent not in new_clauses:
                        new_clauses.append(resolvent)

        if not new_clauses:
            return False

        clauses.extend(new_clauses)


clauses = [
    {"~S", "M"},
    {"S"}
]

goal = "M"

print("===== RESOLUTION: STUDENT ASSIGNMENT =====")

result = resolution(clauses, goal)

if result:
    print("\nConclusion: Rahul receives internal marks - PROVED.")
else:
    print("\nConclusion: Goal cannot be proved.")
```

### Expected Conclusion

**Rahul receives internal marks – PROVED.**

---

# Question 3 – Library Membership

```python
# Resolution Algorithm - Library Membership

def resolve(clause1, clause2):
    resolvents = []

    for literal in clause1:
        opposite = literal[1:] if literal.startswith("~") else "~" + literal

        if opposite in clause2:
            new_clause = (clause1 - {literal}) | (clause2 - {opposite})
            resolvents.append(new_clause)

    return resolvents


def resolution(clauses, goal):
    clauses = [set(c) for c in clauses]

    negated_goal = "~" + goal if not goal.startswith("~") else goal[1:]
    clauses.append({negated_goal})

    print("\nInitial Clauses:")

    for i, clause in enumerate(clauses, 1):
        print(f"C{i} = {clause}")

    while True:
        new_clauses = []

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):

                for resolvent in resolve(clauses[i], clauses[j]):

                    print(
                        f"Resolve C{i + 1} and C{j + 1} -> "
                        f"{resolvent if resolvent else 'EMPTY CLAUSE'}"
                    )

                    if not resolvent:
                        return True

                    if resolvent not in clauses and resolvent not in new_clauses:
                        new_clauses.append(resolvent)

        if not new_clauses:
            return False

        clauses.extend(new_clauses)


clauses = [
    {"~L", "B"},
    {"L"}
]

goal = "B"

print("===== RESOLUTION: LIBRARY MEMBERSHIP =====")

result = resolution(clauses, goal)

if result:
    print("\nConclusion: Priya can borrow books - PROVED.")
else:
    print("\nConclusion: Goal cannot be proved.")
```

### Expected Conclusion

**Priya can borrow books – PROVED.**

---

# Question 4 – Placement Eligibility

```python
# Resolution Algorithm - Placement Eligibility

def resolve(clause1, clause2):
    resolvents = []

    for literal in clause1:
        opposite = literal[1:] if literal.startswith("~") else "~" + literal

        if opposite in clause2:
            new_clause = (clause1 - {literal}) | (clause2 - {opposite})
            resolvents.append(new_clause)

    return resolvents


def resolution(clauses, goal):
    clauses = [set(c) for c in clauses]

    negated_goal = "~" + goal if not goal.startswith("~") else goal[1:]
    clauses.append({negated_goal})

    print("\nInitial Clauses:")

    for i, clause in enumerate(clauses, 1):
        print(f"C{i} = {clause}")

    while True:
        new_clauses = []

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):

                for resolvent in resolve(clauses[i], clauses[j]):

                    print(
                        f"Resolve C{i + 1} and C{j + 1} -> "
                        f"{resolvent if resolvent else 'EMPTY CLAUSE'}"
                    )

                    if not resolvent:
                        return True

                    if resolvent not in clauses and resolvent not in new_clauses:
                        new_clauses.append(resolvent)

        if not new_clauses:
            return False

        clauses.extend(new_clauses)


clauses = [
    {"~A", "P"},
    {"A"}
]

goal = "P"

print("===== RESOLUTION: PLACEMENT ELIGIBILITY =====")

result = resolution(clauses, goal)

if result:
    print("\nConclusion: Arun is eligible for placement - PROVED.")
else:
    print("\nConclusion: Goal cannot be proved.")
```

### Expected Conclusion

**Arun is eligible for placement – PROVED.**

---

# Question 5 – Access Control System

```python
# Resolution Algorithm - Access Control System

def resolve(clause1, clause2):
    resolvents = []

    for literal in clause1:

        if literal.startswith("~"):
            opposite = literal[1:]
        else:
            opposite = "~" + literal

        if opposite in clause2:

            new_clause = (
                clause1 - {literal}
            ) | (
                clause2 - {opposite}
            )

            resolvents.append(new_clause)

    return resolvents


def resolution(knowledge_base, goal):

    clauses = [set(clause) for clause in knowledge_base]

    # Add negation of goal
    if goal.startswith("~"):
        negated_goal = goal[1:]
    else:
        negated_goal = "~" + goal

    clauses.append({negated_goal})

    print("==============================================")
    print(" RESOLUTION ALGORITHM - ACCESS CONTROL")
    print("==============================================")

    print("\nInitial Clauses:")

    for index, clause in enumerate(clauses, 1):
        print(f"C{index} = {clause}")

    while True:

        new_clauses = []

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):

                resolvents = resolve(
                    clauses[i],
                    clauses[j]
                )

                for resolvent in resolvents:

                    print(
                        f"\nResolving C{i + 1} and C{j + 1}"
                    )

                    if len(resolvent) == 0:

                        print("Result = □ (Empty Clause)")

                        return True

                    print("Result =", resolvent)

                    if (
                        resolvent not in clauses
                        and resolvent not in new_clauses
                    ):
                        new_clauses.append(resolvent)

        if not new_clauses:
            return False

        clauses.extend(new_clauses)


# Knowledge Base

knowledge_base = [
    {"~P", "A"},   # P -> A
    {"~A", "G"},   # A -> G
    {"P"}          # Correct password entered
]

goal = "G"

result = resolution(
    knowledge_base,
    goal
)

print("\n==============================================")

if result:
    print("FINAL CONCLUSION:")
    print("The user is GRANTED ACCESS.")
    print("Goal G is logically PROVED.")
else:
    print("FINAL CONCLUSION:")
    print("The goal could not be proved.")

print("==============================================")
```


