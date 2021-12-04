"""
We're playing Bingo with a giant squid that is attaquing our submarine!
Task 1: Guess the winning board
Task 2: We're losing at bingo! Guess which one is going to be the latest losing board
"""

from typing import List


class BingoBoard():
    def __init__(self, bingo_board: list):
        self.length_x = len(bingo_board)
        self.length_y = len(bingo_board[0])
        self.original_board = bingo_board
        self.crossed_board = bingo_board.copy()
        self.last_number_crossed = 0

    def display_board(self):
        print()
        print('Bingo board:')
        for row in self.crossed_board:
            print(row)
        print()


    def cross_number_from_board(self, number: int):
        numbers_crossed = 0
        for y in range(self.length_y):
            for x in range(self.length_x):
                if self.crossed_board[y][x] == number:
                    self.crossed_board[y][x] = 'x'
                    self.last_number_crossed = number
                    numbers_crossed += 1
        return numbers_crossed

    def check_if_bingo(self):
        # check all rows
        for y in range(self.length_y):
            crosses_in_one_row = 0
            for x in range(self.length_x):
                if self.crossed_board[y][x] == 'x':
                    crosses_in_one_row += 1 # count one!
            if crosses_in_one_row == self.length_x:
                return True

        # check all columns
        for x in range(self.length_x):
            crosses_in_one_column = 0
            for y in range(self.length_y):
                if self.crossed_board[y][x] == 'x':
                    crosses_in_one_column += 1 # count one!
            if crosses_in_one_column == self.length_y:
                return True
        return False

    def count_sum_of_unchecked(self) -> int:
        sum_of_unchecked = 0
        # check all rows
        for y in range(self.length_y):
            for x in range(self.length_x):
                if self.crossed_board[y][x] != 'x':
                    sum_of_unchecked += self.crossed_board[y][x]
        return sum_of_unchecked
    
    def calculate_score_of_board(self) -> int:
        sum_of_unchecked = self.count_sum_of_unchecked()
        last_number_crossed = self.last_number_crossed
        print(f'Sum of unchecked = {sum_of_unchecked}')
        print(f'Last num crossed = {last_number_crossed}')
        return sum_of_unchecked * last_number_crossed


def get_bingo_numbers_and_board_from_text_file(path_to_file: str):
    # load file
    with open(path_to_file) as f:
        lines = f.readlines()
        
    # load numbers, rows 1 and 2
    bingo_numbers = lines.pop(0).rstrip('\n').split(',')
    bingo_numbers = [int(number) for number in bingo_numbers]  # cast to int
    lines.pop(0)

    # load bingo boards
    bingo_board = []
    list_bingo_boards: List[BingoBoard] = []
    for line in lines:
        if line == '\n':
            list_bingo_boards.append(BingoBoard(bingo_board)) # add board to list
            bingo_board = []  # new empty board
            continue
        row_of_board = line.rstrip('\n').split(' ') 
        row_of_board = [int(element) for element in row_of_board if element != '']
        bingo_board.append(row_of_board) # add row to board
    list_bingo_boards.append(BingoBoard(bingo_board))

    return bingo_numbers, list_bingo_boards


def play_bingo(numbers, boards) -> int:
    """
    Input the winning numbers and the amount of boards
    """
    for number in numbers:
        for board in boards:
            board.cross_number_from_board(number)
            if board.check_if_bingo():
                board.display_board()
                return board.calculate_score_of_board()
    return 0  # no board got bingo



def lose_at_bingo(numbers, boards) -> int:
    """
    Input the winning numbers and the amount of boards
    """
    new_boards = boards.copy()
    last_board = boards[0]
    for number in numbers:
        for board in boards:
            board.cross_number_from_board(number)
            if board.check_if_bingo():
                new_boards.remove(board)
                last_board = board
        boards = new_boards.copy()
        if len(boards) == 0:
            last_board.display_board()
            return last_board.calculate_score_of_board()
    return 0  # no board got bingo


def main():
    # input
    input_filename = 'day_4/input_hard.txt'
    numbers, bingo_boards = get_bingo_numbers_and_board_from_text_file(input_filename)

    winning_score = play_bingo(numbers, bingo_boards)
    print(f'Part 1: {winning_score}')

    losing_score = lose_at_bingo(numbers, bingo_boards)
    print(f'Part 2: {losing_score}')



if __name__ == '__main__':
    main()
