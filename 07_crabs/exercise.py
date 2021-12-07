"""
Crabs
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


def easy_calculation(crab_list: List[int]):
    # get most popular number
    crab_list.sort()
    most_popular = (Counter(crab_list))
    print(most_popular)

    # brute force it
    unique_crab_list = list(set(crab_list))
    first_point = crab_list[0]
    last_point = crab_list[-1]

    lowest = -1
    for i in range(first_point, last_point+1):
        print(i)


def main():
    # input
    input_filename = '07_crabs/input_easy.txt'

    # part 1
    crab_list: List[int] = get_input(input_filename)
    easy_calculation(crab_list)

if __name__ == '__main__':
    main()
