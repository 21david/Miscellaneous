# https://www.tryexponent.com/practice/prepare/drone-flight-planner

# One line elegant solution, after seeing solution
def calc_drone_min_energy(route: List[List[int]]) -> int:
    return max(route[0][2], max(alt[2] for alt in route)) - route[0][2]

# Elegant solution, after seeing solution
def calc_drone_min_energy(route: List[List[int]]) -> int:
    max_alt = route[0][2]
    max_alt = max(max_alt, max(alt[2] for alt in route))
    return max_alt - route[0][2]

# Basic solution
def calc_drone_min_energy(route: List[List[int]]) -> int:
    min_energy = 0
    curr_energy = 0
    for i in range(1, len(route)):
        curr_energy += (route[i-1][2] - route[i][2])
        min_energy = min(min_energy, curr_energy)
    return -min_energy


# Older solution I wrote
'''
Possible brute force: Guess and check approach
Start by giving it 0 energy
Check if it crashes with that energy
Repeat with 1 more energy each time until it can finish its route
The first time it finishes its route is the answer
'''

'''
More optimal, linear approach:
Find the biggest "rise"
    In the example, this would be from 6 -> 15
    In other examples, it may be through multiple points, like 6 -> 10 -> 15
    Figure out how much kWh you had right before the rise
    Do this formula:
      (amount risen) - (energy before the rise)
'''

def calc_drone_min_energy(route: List[List[int]]) -> int:
    zs = [x[2] for x in route]
    peak_point_idx = max((val for val in enumerate(zs)), key=lambda val: val[1]) [0]
    min_point_before_peak_idx = min((val for val in enumerate(zs[:peak_point_idx+1])), key = lambda val: val[1]) [0]
    most_energy_needed = zs[peak_point_idx] - zs[min_point_before_peak_idx]
    energy_before_using_max_energy = zs[0] - zs[min_point_before_peak_idx]
    return most_energy_needed - energy_before_using_max_energy


# Test cases:
m = [ [0,   2, 10],
      [3,   5,  0],
      [9,  20,  6],
      [10, 12, 15],
      [10, 10,  8] ]
print(calc_drone_min_energy(m))

m = [ [0,   2, 10] ]
print(calc_drone_min_energy(m))
