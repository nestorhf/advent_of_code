"""
Task 1: With the length you can infer which number it is
Task 2: Infer all numbers with domain and get a 1 to 1 mapping of of the side
ABCDEFG to the appropriate answer
"""

from typing import List, Tuple, Dict
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


def get_easy_result(output_numbers: List[str]) -> int:
    """
    Easy solution
    1. Count the length of each number (0: ABCEFG)
    2. Get those ones that have a unique length
    3. In the output, count the lenghts and increment
    """
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
    """
    Get a dictionary with the key being the length, and value the numbers that have that length

    For instance:
        - key= 6. Meaning the length of the word
        - value= [0, 6, 9]. All those numbers have a representation of length 6.
    This is useful because when we get a random digit of length 6, we can
    instantly know which numbers could it potentially refer to
    """
    dictionary_aggregated_lengths = {}
    for key, value in NUMBERS.items():
        if len(value) not in dictionary_aggregated_lengths:
            dictionary_aggregated_lengths[len(value)] = []
        dictionary_aggregated_lengths[len(value)].append(key)
    return dictionary_aggregated_lengths


def load_input(input_path: str) -> Tuple[List[str], List[str]]:
    """
    Loads the input and returns numbers coded (ABDGF) and the output numbers
    """
    with open(input_path) as f:
        lines = f.readlines()
    numbers_coded = []
    output_numbers = []
    for line in lines:
        line_numbers_coded, line_numbers_output = line.strip().split(' | ')
        numbers_coded.append(line_numbers_coded.split(' '))
        output_numbers.append(line_numbers_output.split(' '))
    return numbers_coded, output_numbers


def initialize_domain():
    """
    Initialize a domain for each side (A,B,C,D,E,F,G) with lower case (abcdefg)
    Upper case mean the actual position and lower case means the messed up input
    """
    dictionary_solutions = {}
    for letter in POSSIBLE_CONNECTIONS:
        dictionary_solutions[letter.upper()] = POSSIBLE_CONNECTIONS.copy()
    return dictionary_solutions


def get_repeated_chars(list_of_words: List[str]) -> str:
    """
    Get which characters a list of words have in common. These characters must
    be present in all words
    """
    joined_words = "".join(list_of_words)
    repeated_letters = ''
    for key, value in Counter(joined_words).items():
        if value == len(list_of_words):
            repeated_letters += key
    return repeated_letters


def reduce_domains(row_numbers_coded, mapping_lengths):
    """
    Initialize the domain for the problem
    Then proceed to solve. If there's repeated characters between letters,
    reduce the domain to those repeated letters (or less)
    The domain keeps a count of alive answers and is being updated every iteration
    """
    # new row
    domains = initialize_domain()
    # solve mistery
    for number_coded in row_numbers_coded:
        list_number_coded = [char for char in number_coded]
        numbers_same_length = mapping_lengths[len(number_coded)]
        numbers_chars = [NUMBERS[digit] for digit in numbers_same_length]
        repeated_chars = get_repeated_chars(numbers_chars)
        # reduce domain
        for char in repeated_chars:
            alive = set(domains[char])
            could_be = set(list_number_coded)
            new_alive = list(alive.intersection(could_be))
            domains[char] = new_alive
    return domains


def clean_up_domains(domains):
    """
    In the final stage, some anwers have been reached. 
    If there's an answer assigned, let's say A->g, then 'g' needs to be deleted
    from all the other domains. Do this until all domains have 1 digit.
    """
    # initialize solved
    solved = []
    for key, value in domains.items():
        if len(value) == 1:
            solved.append(key)

    # run until all solved answers have been deleted from other domains
    while len(solved) > 0:
        key_to_delete = solved.pop()
        letter_to_delete = domains[key_to_delete]
        for key, value in domains.items():
            if len(value) > 1:
                # remove from domain
                new_removed = list(set(value) - set(letter_to_delete))
                if len(new_removed) == 1:
                    solved.append(key) # add to solved
                domains[key] = new_removed
    return domains


def translate_numbers(domains: dict) -> Dict[str, int]:
    """
    Given the solved domain, we are going to translate the upper cases into
    lower cases with the mapping (domain, only 1 to 1 mapping)
    """
    numbers_translated = {}
    for key, value in NUMBERS.items():
        translated_word = ''
        for char in value:
            new_char = domains[char][0]
            translated_word += new_char
        numbers_translated[key] = ''.join(sorted(translated_word))
    numbers_translated = {value: key for key, value in numbers_translated.items()}
    return numbers_translated


def get_complete_decoded_answer(numbers_coded, output_numbers) -> int:
    """
    For every row, calculate the sum of the output numbers bu solving the input
    `numbers_coded`.
    Return the total sum.
    """
    mapping_lengths = get_mapping_lengths()
    total_sum = 0
    for row_index, _ in enumerate(numbers_coded):
        domains = reduce_domains(numbers_coded[row_index], mapping_lengths)
        domains = clean_up_domains(domains)
        numbers_translated = translate_numbers(domains)
        sum_numbers_string = ''
        for num in output_numbers[row_index]:
            num = ''.join(sorted(num))
            sum_numbers_string += str(numbers_translated[num])
        total_sum += int(sum_numbers_string)
    return total_sum


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
