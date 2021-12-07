"""
Crabs
Task 1: Get the average movement of a crab
Task 2: Get the average movement of a crab

Thoughts:
This seemed easy. If the problem were more complex, instead of brute forcing
you could implement some heuristics. Instead of looping through all numbers you
can start by the `avg` value, which is better than the edges.
You could move in the direction in which the fuel is smaller. 
array = [140 120 100 120 130]
Let's say you start at 120 fuel. Then you calculate the one on the right and it
turns out is 130 fuel. I assume that the fuel formula returns a bell curve, so you don't need to 
keep on going. It's best to turn back and look at the left. If the left side is
bigger then you have reached a local minimum, and you can be pretty certain
that that is a good solution (valley)
"""

from typing import List
from collections import Counter

def get_input(input_filename: str) -> List[int]:
    """
    Get input file and return list of Fish
    """
    with open(input_filename) as f:
        lines = f.readlines()

    crabs_string = lines[0].strip().split(',')
    crabs_int = [int(crab) for crab in crabs_string]
    return crabs_int


def get_linear_fuel(crab_list: List[int]):

    # get most popular number
    crab_list.sort()
    crab_counter = (Counter(crab_list))

    # get range of crab position
    first_point = crab_list[0]
    last_point = crab_list[-1]

    list_fuel = []
    for horizontal_position in range(first_point, last_point+1):
        fuel = 0
        for crab_position, number_of_crabs in crab_counter.items():
            fuel += abs(crab_position - horizontal_position) * number_of_crabs
        list_fuel.append(fuel)

    return min(list_fuel)


def get_incremental_fuel(crab_list: List[int]):

    # get most popular number
    crab_list.sort()
    crab_counter = (Counter(crab_list))

    # get range of positions of crabs
    first_point = crab_list[0]
    last_point = crab_list[-1]

    list_fuel = []
    for target_horizontal in range(first_point, last_point+1):
        fuel = 0
        for crab_position, number_of_crabs in crab_counter.items():
            difference = abs(crab_position - target_horizontal)
            # formula for arithmetic sequence sum. I have taught this and now is useful!
            # S = n_elements*(element_1, element_1) / 2
            fuel_per_crab = int(difference*(1+difference)/2)
            fuel += fuel_per_crab * number_of_crabs
        list_fuel.append(fuel)

    return min(list_fuel)


def main():
    # input
    input_filename = '07_crabs/input_hard.txt'
    crab_list: List[int] = get_input(input_filename)

    # part 1
    min_fuel: int = get_linear_fuel(crab_list)
    print(f'Part 1: {min_fuel}')

    # part 2
    min_fuel: int = get_incremental_fuel(crab_list)
    print(f'Part 2: {min_fuel}')


if __name__ == '__main__':
    main()
