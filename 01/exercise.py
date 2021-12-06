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
    When calculating the difference of an average, let's say that the averages that I want to
    compare are these two sets:

    list_numbers = [1,2,3,4]
    set_a = [1,2,3]
    set_b =   [2,3,4]

    The only difference between the sets is [1] and [4], since they share [2,3]
    We can just compare 1(index 0) and 4 (index 0 + window_number)
    There is no need for an average, just a simple comparison
    """
    counter = 0
    for index in range(len(list_numbers) - window_of_average):
        if list_numbers[index] < list_numbers[index + window_of_average]:
            counter += 1
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
