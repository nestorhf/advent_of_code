"""
Task 1: Calculate the difference of the reading column, and get which ones are positive and which
ones are positive and which one aren't
Task 2: Same, but first calculate the moving average of the 3 values next to you, and then
calculate the difference
"""
from typing import List
import pandas as pd


def positive_movements_optimized(window_of_average: int, list_numbers: List[int]) -> int:
    """
    When comparing the difference of an average, let's say that the averages that I want to compare
    are these two 

    list_numbers = [1,2,3,4]
    set_a = [1,2,3]
    set_b =   [2,3,4]

    As you can see, the only difference is 1 and 4, since they share [2,3]
    If we just compare 1(index 0) and 4 (index 0 + window_number)
    There is no need for an average, just a simple comparison
    """
    counter = 0
    for index in range(len(list_numbers) - window_of_average):
        if list_numbers[index] < list_numbers[index + window_of_average]:
            counter += 1
    return counter


def positive_movements(window_of_average: int, list_numbers: List[int]) -> int:
    """
    Function used to get the total number of positive differences, taken into account the window of
    moving averages.

    It functions by splitting into 2 the list of numbers passed.
    Let's say that the inputs are:
        - window_of_average: 3
        - list_numbers: [3, 4, 5, 6, 2, 6, 8]
    Then:
        - last_numbers: [3, 4, 5]
        - remaining_numbers: [6, 2, 6, 8]
    Loop 1 iter:
        - sum_1 = 12
        - sum_2 = 15
        - counter = 1
    Loop 2 iter:
        - sum_1 = 15
        - sum_2 = 13
        - counter = 1
    Loop 3 iter:
        - sum_1 = 13
        - sum_2 = 14
        - counter = 2
    Loop 4 iter:
        - sum_1 = 14
        - sum_2 = 16
        - counter = 3

    Return value = 3.
    There is no need to calculate the average, as both sums would be divided by the same number
    """
    counter = 0
    last_numbers = list_numbers[:window_of_average]  # first X previous numbers
    remaining_numbers = list_numbers[window_of_average:]

    for number in remaining_numbers:
        last_numbers.append(number)  # add new number to last position
        sum_1 = sum(last_numbers[:window_of_average])
        sum_2 = sum(last_numbers[-window_of_average:])
        # now compare
        if sum_1 < sum_2:
            counter += 1
        last_numbers.pop(0)  # update

    return counter


def regular_approach(df: pd.DataFrame):
    """
    This one is a bit more complex
    My strategy is the following one.
    - Create a function that is able to calculate the amount of positive movements given a window
      to calculate the averages
    - Input 1 and 3
    """
    print('[*] List approach')
    list_numbers = df['reading'].to_list()
    solution_1 = positive_movements_optimized(1, list_numbers)
    solution_2 = positive_movements_optimized(3, list_numbers)
    print(f'Answer 1: {solution_1}')
    print(f'Answer 2: {solution_2}')


def pandas_approach(df: pd.DataFrame):
    """
    Not much to explain here. With very little thought, looking on the internet I was able to find
    the `.diff` function and also the `.rolling(window=X).mean()` feature. This makes it very easy
    but at the same time is not fun because you have a very narrow understanding of what you're
    doing
    """
    print('[*] Pandas approach')
    df['difference'] = df['reading'].diff()
    df['moving_average'] = df['reading'].rolling(window=3).mean()
    df['moving_average_diff'] = df['moving_average'].diff()
    filtered_only_positive = df[df['difference'] > 0]
    filtered_moving_average_diff = df[df['moving_average_diff'] > 0]
    print(f'Answer 1: {len(filtered_only_positive)}')
    print(f'Answer 2: {len(filtered_moving_average_diff)}')


def main():
    df = pd.read_csv('input.csv', index_col=False)
    regular_approach(df)
    pandas_approach(df)


if __name__ == '__main__':
    main()
