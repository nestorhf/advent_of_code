"""
Task 1: Move around and keep track of where you are
"""
import pandas as pd
from typing import List


def regular_approach(list_movement: list, list_value: list):
    """
    Easily keep variables and Cycle. Part 1 and 2 are nearly identical
    """
    print('[*] Regular approach')
    # Part 1
    x = 0
    y = 0
    for index in range(len(list_value)):
        if list_movement[index] == 'forward':
            x += list_value[index]
        elif list_movement[index] == 'up':
            y += list_value[index]
        elif list_movement[index] == 'down':
            y -= list_value[index]
    print(f'Part 1: Outcome {abs(x*y)}')
    # Part 2
    aim = 0
    depth = 0
    horizontal = 0
    for index in range(len(list_value)):
        if list_movement[index] == 'forward':
            horizontal += list_value[index]
            depth += list_value[index] * aim
        elif list_movement[index] == 'up':
            aim += list_value[index]
        elif list_movement[index] == 'down':
            aim -= list_value[index]
    print(f'Part 2: Outcome {abs(horizontal*depth)}')


def pandas_approach(df: pd.DataFrame):
    """
    My idea is to group by movement and sum, then apply the different movements
    """
    print('[*] Pandas approach')
    sum_of_values: pd.DataFrame = df.groupby('movement').sum().reset_index()
    x = 0
    y = 0
    for index, row in sum_of_values.iterrows():
        value = int(row['value'])
        movement = row['movement']
        if movement == 'forward':
            x += value
        elif movement == 'up':
            y += value
        elif movement == 'down':
            y -= value
    print(f'Part 1: Outcome {abs(x*y)}')


def main():
    df = pd.read_csv('day_2/input.csv', sep=' ', index_col=False)
    list_value = df['value'].to_list()
    list_movement = df['movement'].to_list()
    regular_approach(list_movement, list_value)
    pandas_approach(df)


if __name__ == '__main__':
    main()
