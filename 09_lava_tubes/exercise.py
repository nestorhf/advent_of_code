"""
Lava tubes
Task 1: Find local minimums
Task 2: Infer all numbers with domain and get a 1 to 1 mapping of of the side
"""

from typing import List

def get_map(input_path: str) -> List[List[int]]:
    with open(input_path) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    map = []
    for line in lines:
        list_digits = []
        for digit in line:
            list_digits.append(int(digit))
        map.append(list_digits)
    return map


class Point():
    """
    Point class, storing position x,y and value
    """
    def __init__(self, x, y, map: List[List[int]]):
        self.x = x
        self.y = y
        self.value = map[y][x]

    def __str__(self):
        return f'{self.x},{self.y}, {self.value}'

    def __repr__(self):
        return f'{self.x},{self.y}, {self.value}'
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


def get_new_to_explore(point: Point, map, total_basin: List[Point]):
    """
    inputs:
        - `point` that you would like to explore
        - `map`
        - `total_basin`, which is a list of Points that are already added to the basin

    Given a point (.)

    219
    3.9
    985

    We want to explore the possible basin nodes [3,1,8,9]
    The `total_basin` keeps track of Points already added to the basin. Maybe
    number `1` has already been added to the basin, and therefore we can't add
    it.
    
    Given those circumstances, the function will return [3,8], which are Points
    that are not found in `total_basin` but that they meet the criteria
    """

    new_to_explore: List[Point] = []
    x = point.x
    y = point.y

    # left and right
    for dx in [-1, 1]:
        neighbor_x = dx + x
        if neighbor_x < 0 or neighbor_x == len(map[0]):
            continue
        potential_explorer = Point(neighbor_x, y, map)
        if potential_explorer.value != 9 and potential_explorer not in total_basin:
            new_to_explore.append(potential_explorer)

    # up and down
    for dy in [-1, 1]:
        neighbor_y = dy + y
        if neighbor_y < 0 or neighbor_y == len(map):
            continue

        potential_explorer = Point(x, neighbor_y, map)
        if potential_explorer.value != 9 and potential_explorer not in total_basin:
            new_to_explore.append(potential_explorer)

    return new_to_explore


def is_minimum(x: int, y: int, map: List[List[int]]):
    """
    Given coordinates x,y and a map, return True if it's a local minimum and False if not
    """

    digit = map[y][x]
    # left and right
    for dx in [-1, 1]:
        neighbor_x = dx + x
        if neighbor_x < 0 or neighbor_x == len(map[0]):
            continue
        if map[y][neighbor_x] <= digit:  # important!
            return False

    # up and down
    for dy in [-1, 1]:
        neighbor_y = dy + y
        if neighbor_y < 0 or neighbor_y == len(map):
            continue
        if map[neighbor_y][x] <= digit:  # important!
            return False
    return True


def find_local_minimums(map: List[List[int]]):
    """
    Get sum of local minimums + 1
    """
    list_minimums = []
    for y, row in enumerate(map):
        for x, digit in enumerate(row):
            # check if it's minimum
            if is_minimum(x, y, map):
                list_minimums.append(digit+1)

    return sum(list_minimums)


def find_basins(map: List[List[int]]):
    """
    Find all basins and return the multiplication of the biggest 3

    1. To do this, we first need to find the coordinates of the minimums
    2. Starting on a minimum, we look at the surrounding neighbours
    3. Check if neighbors meet criteria
    4. Iterate
    5. Find area of basin
    6. Return multiplication of biggest 3 areas
    """

    # find minimums
    list_minimums = []
    for y, row in enumerate(map):
        for x, digit in enumerate(row):
            if is_minimum(x, y, map):
                list_minimums.append(Point(x,y,map))

    # find areas of basins
    lengths_of_all_basins: List[int] = []
    while len(list_minimums) > 0:
        total_basin = []
        to_explore = []
        minimum = list_minimums.pop()
        to_explore.append(minimum)
        total_basin.append(minimum)
        while len(to_explore) > 0:
            explored_point = to_explore.pop()
            x = explored_point.x
            y = explored_point.y
            new_to_explore = get_new_to_explore(explored_point, map, total_basin)
            total_basin += new_to_explore
            to_explore += new_to_explore
        lengths_of_all_basins.append(len(total_basin))

    # Get 3 biggest and mulitiply
    lengths_of_all_basins.sort()
    three_biggest = lengths_of_all_basins[-3:]
    return_value = 1
    for item in three_biggest:
        return_value *= item

    return return_value


def main():
    input_path = '09_lava_tubes/input_hard.txt'
    map = get_map(input_path)
    answer_1 = find_local_minimums(map)
    print(f'Task 1: {answer_1}')

    answer_2 = find_basins(map)
    print(f'Task 2: {answer_2}')
    

if __name__ == '__main__':
    main()
