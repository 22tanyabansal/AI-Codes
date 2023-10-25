import math

class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

def get_gcd(x, y):
    if y == 0:
        return x
    return get_gcd(y, x % y)

def pour_water(from_capacity, to_capacity, d):
    from_cap = from_capacity
    to_cap = 0
    req_step = 1

    while from_cap != d and to_cap != d:
        max_pour = min(from_cap, to_capacity - to_cap)

        to_cap = to_cap + max_pour
        from_cap = from_cap - max_pour
        req_step += 1

        if from_cap == d or to_cap == d:
            break

        if from_cap == 0:
            from_cap = from_capacity
            req_step += 1

        if to_cap == to_capacity:
            to_cap = 0
            req_step += 1

    return req_step

def find_min_steps(i, j, d):
    if i > j:
        i, j = j, i

    if d > j:
        return -1

    if d % get_gcd(j, i) != 0:
        return -1

    return min(pour_water(j, i, d), pour_water(i, j, d))

def find_path(i, j, d):
    path = []
    from_cap = i
    to_cap = 0

    while from_cap != d and to_cap != d:
        max_pour = min(from_cap, j - to_cap)
        to_cap = to_cap + max_pour
        from_cap = from_cap - max_pour
        path.append(State(from_cap, to_cap))

        if from_cap == d or to_cap == d:
            break

        if from_cap == 0:
            from_cap = i

        if to_cap == j:
            to_cap = 0

    path.append(State(from_cap, to_cap))
    return path

if __name__ == "__main__":
    i = int(input("Enter the size of Jug1 in liters: "))
    j = int(input("Enter the size of Jug2 in liters: "))
    d = int(input("Enter the amount of water you want to measure: "))

    min_steps = find_min_steps(i, j, d)
    if min_steps == -1:
        print(f"Cannot measure {d} liters with jug capacities {i} and {j}.")
    else:
        print(f"Minimum number of steps required to measure water is {min_steps}")
        path = find_path(i, j, d)
        print("Path of states:")
        for state in path:
            print(f"Jug1: {state.jug1} liters, Jug2: {state.jug2} liters")
