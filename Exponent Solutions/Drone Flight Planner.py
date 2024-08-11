# https://www.tryexponent.com/practice/prepare/drone-flight-planner

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

# This is the equivalent of the method above. This is not how I normally code, this was just for fun.
# It could probably be further reduced to one line by just using the route matrix.
def calc_drone_min_energy_2(route: List[List[int]]) -> int:
    zs = [x[2] for x in route]
    return (zs[max((val for val in enumerate(zs)), key=lambda val: val[1]) [0]] - zs[min((val for val in enumerate(zs[:max((val for val in enumerate(zs)), key=lambda val: val[1]) [0]+1])), key = lambda val: val[1]) [0]])   -   (zs[0] - zs[min((val for val in enumerate(zs[:max((val for val in enumerate(zs)), key=lambda val: val[1]) [0]+1])), key = lambda val: val[1]) [0]])


# Test cases:
m = [ [0,   2, 10],
      [3,   5,  0],
      [9,  20,  6],
      [10, 12, 15],
      [10, 10,  8] ]
print(calc_drone_min_energy(m))

m = [ [0,   2, 10] ]
print(calc_drone_min_energy(m))
