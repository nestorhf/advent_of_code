"""
Task 1: With the length you can infer which number it is
Task 2: Infer all numbers with domain and get a 1 to 1 mapping of of the side
ABCDEFG to the appropriate answer
"""

from typing import List
from collections import Counter

# dictionary with numbers
NUMBERS = {
    0: 'ABCEFG',
    1: 'CF',
    2: 'ACDEG',
    3: 'ACDFG',
    4: 'BCDF',
    5: 'ABDFG',
    6: 'ABDEFG',
    7: 'ACF',
    8: 'ABCDEFG',
    9: 'ABCDFG'
}
POSSIBLE_CONNECTIONS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# get possible connections into a dictionary

def get_easy_result(output_numbers: List[str]):
    instances_of_unique_numbers = 0
    list_lengths = [len(value) for value in NUMBERS.values()]
    list_lengths = Counter(list_lengths)
    unique_lengths = [key for key, value in Counter(list_lengths).items() if value == 1]
    for outputs in output_numbers:
        for output in outputs:
            if len(output) in unique_lengths:
                instances_of_unique_numbers += 1
    return instances_of_unique_numbers


def get_mapping_lengths():
    dictionary_aggregated_lengths = {}
    for key, value in NUMBERS.items():
        if len(value) not in dictionary_aggregated_lengths:
            dictionary_aggregated_lengths[len(value)] = []
        dictionary_aggregated_lengths[len(value)].append(key)
    return dictionary_aggregated_lengths


def load_input(input_path: str):
    with open(input_path) as f:
        lines = f.readlines()
    numbers_coded = []
    output_numbers = []
    for line in lines:
        line_numbers_coded, line_numbers_output = line.strip().split(' | ')
        numbers_coded.append(line_numbers_coded.split(' '))
        output_numbers.append(line_numbers_output.split(' '))
    return numbers_coded, output_numbers

def get_dictionay_possible_solutions():
    dictionary_solutions = {}
    for letter in POSSIBLE_CONNECTIONS:
        dictionary_solutions[letter.upper()] = POSSIBLE_CONNECTIONS.copy()
    return dictionary_solutions

def get_repeated_chars(list_of_words: List[str]):
    joined_words = "".join(list_of_words)
    repeated_letters = ''
    for key, value in Counter(joined_words).items():
        if value == len(list_of_words):
            repeated_letters += key
    return repeated_letters


def get_complete_decoded_answer(numbers_coded, output_numbers):
    mapping_lengths = get_mapping_lengths()
    total_sum = 0
    for row_index, _ in enumerate(numbers_coded):
        # new row
        solutions_dict = get_dictionay_possible_solutions()
        row_numbers_coded = numbers_coded[row_index]
        row_output_numbers = output_numbers[row_index]
        # solve mistery
        for number_coded in row_numbers_coded:
            list_number_coded = [char for char in number_coded]
            numbers_same_length = mapping_lengths[len(number_coded)]
            numbers_chars = [NUMBERS[digit] for digit in numbers_same_length]
            repeated_chars = get_repeated_chars(numbers_chars)
            # reduce domain
            for char in repeated_chars:
                alive = set(solutions_dict[char])
                could_be = set(list_number_coded)
                new_alive = list(alive.intersection(could_be))
                solutions_dict[char] = new_alive
        # Clean up if alive
        solved = []
        for key, value in solutions_dict.items():
            if len(value) == 1:
                solved.append(key)
        while len(solved) > 0:
            key_to_delete = solved.pop()
            letter_to_delete = solutions_dict[key_to_delete]
            for key, value in solutions_dict.items():
                if len(value) > 1:
                    # remove
                    new_removed = list(set(value) - set(letter_to_delete))
                    if len(new_removed) == 1:
                        solved.append(key)
                    solutions_dict[key] = new_removed
        numbers_translated = translate_numbers(solutions_dict)
        sum_numbers_string = ''
        for num in row_output_numbers:
            num = ''.join(sorted(num))
            sum_numbers_string += str(numbers_translated[num])
        total_sum += int(sum_numbers_string)
    return total_sum


def translate_numbers(solutions_dict: dict):
    numbers_translated = {}
    for key, value in NUMBERS.items():
        translated_word = ''
        for char in value:
            new_char = solutions_dict[char][0]
            translated_word += new_char
        numbers_translated[key] = ''.join(sorted(translated_word))
    numbers_translated = {value: key for key, value in numbers_translated.items()}
    return numbers_translated
        

def main():
    input_path = '08_numbers/input_hard.txt'
    numbers_coded, output_numbers = load_input(input_path)
    # task 1
    result_1 = get_easy_result(output_numbers)
    print(f'Task 1: {result_1}')
    # task 2
    result_2 = get_complete_decoded_answer(numbers_coded, output_numbers)
    print(f'Task 2: {result_2}')
    

if __name__ == '__main__':
    main()
