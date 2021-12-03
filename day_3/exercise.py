"""
Task 1: Move around and keep track of where you are
"""
from collections import Counter

import pandas as pd


def get_life_support_rating(list_of_readings: list, strategy: str):
    """
    Generate rating based on list of readings and strategy

    To do this we get a list of readings and a strategy ('min' or 'max')
    :param list_of_readings: list containing words of the same length consisting of '0' and '1's
    :param strategy: Either 'min' or 'max', if your strategy is to look for the least recurring
    digit or the most.
    """
    list_of_alive = list_of_readings.copy()
    for position_of_letter in range(len(list_of_readings[0])):
        word_transposed = [word[position_of_letter] for word in list_of_alive]
        winning_digit = get_most_recurring_digit(word_transposed, strategy)
        # update alive list
        list_of_alive = [
            list_of_alive[index] for index, letter in enumerate(word_transposed)
            if winning_digit == letter
        ]
        if len(list_of_alive) == 1:  # reached the end! Last man standing
            return int(list_of_alive[0], 2)


def get_power_consumption(list_of_readings: list, strategy: str) -> int:
    """
    Return the most (or least) recurring indexes based on a list of readings and a strategy
    - min will get you the least recurring digits
    - max will get you the most recurring digits
    """
    reading = ''
    for index in range(len(list_of_readings[0])):
        word_transposed = [word[index] for word in list_of_readings]
        reading += get_most_recurring_digit(word_transposed, strategy)
    return int(reading, 2)  # bin -> int


def get_most_recurring_digit(word: list, strategy: str):
    """
    Given a word, returns the most recurring digit, following one strategy if there's a tie
    # TODO: Function could be cleaner

    :param strategy: can be 'min' or 'max'. Min will return the least recurring digit
    :param word: regular word as a string. It has to be composed of '0' and '1'
    """
    counter = dict(Counter(word))
    # edge case, if there's a tie
    if counter['0'] == counter['1']:
        winning_digit = '1'
        if strategy == 'min':
            winning_digit = '0'
        return winning_digit
    # strategies min and max
    if strategy == 'min':
        return min(counter, key=counter.get)
    return max(counter, key=counter.get)


def regular_approach(list_of_readings: list):
    """
    Easily keep variables and Cycle
    """
    print('[*] Regular approach')

    gamma = get_power_consumption(list_of_readings, strategy='max')
    epsilon = get_power_consumption(list_of_readings, strategy='min')
    print(f'Part 1: {gamma*epsilon}')

    co2 = get_life_support_rating(list_of_readings, strategy='min')
    oxygen = get_life_support_rating(list_of_readings, strategy='max')
    print(f'Part 2: {co2 * oxygen}')


def main():
    df = pd.read_csv('day_3/input.csv', dtype=object, index_col=False)
    list_of_readings = df['values'].to_list()
    regular_approach(list_of_readings)


if __name__ == '__main__':
    main()
