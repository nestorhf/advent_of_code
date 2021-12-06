"""
Lantern fish
Task 1:  Count have many lantern fish there are in a pack after 80 days
"""

from typing import List

NEW_BORN_CYCLE = 8
ADULT_CYCLE = 6

class Fish():

    def __init__(self, age: int, new_born=False):
        self.age = age
        self.cycle_to_have_baby = 6
        if new_born:
            self.age = NEW_BORN_CYCLE
            self.cycle_to_have_baby = NEW_BORN_CYCLE

    def next_day(self):
        if self.age == 0:
            self.age = ADULT_CYCLE
            self.cycle_to_have_baby = ADULT_CYCLE
            kid = Fish(self.cycle_to_have_baby, new_born=True)  # 
            return kid

        self.age -= 1
        return None

    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f'Age {self.age}, Cycle {self.cycle_to_have_baby}'

class School_of_fish():

    def __init__(self, all_fish: List[Fish]):
        self.all_fish = all_fish

    def next_day(self):
        new_borns = []
        for fish in self.all_fish:
            potential_new_fish = fish.next_day()
            if type(potential_new_fish) == Fish:
                new_borns.append(potential_new_fish)
        self.all_fish += new_borns # update pack

    def get_school_ages(self):
        ages = [fish.age for fish in self.all_fish]
        return ages

    def get_number_of_fish(self) -> int:
        return len(self.all_fish)


def get_initial_pack_of_fish(input_filename: str) -> List[Fish]:
    with open(input_filename) as f:
        lines = f.readlines()

    fish_raw = lines[0].strip().split(',')
    fish_int = [int(fish) for fish in fish_raw]
    fish_bank = [Fish(age_of_fish) for age_of_fish in fish_int]
    for fish in fish_bank:
        print(fish)

    return fish_bank



def main():

    # input
    input_filename = 'day_6/input_hard.txt'
    days = 256
    fish_list = get_initial_pack_of_fish(input_filename)
    fish_school = School_of_fish(fish_list)
    

    print(f'Day {0}: {fish_school.get_school_ages()}')
    original_number_fish = fish_school.get_number_of_fish()
    all_growths = []
    all_growths.append(original_number_fish)

    for day in range(1, days+1):
        fish_school.next_day()
        # if day % 10 == 0:
        #     print(f'Day {day}: {fish_school.get_number_of_fish()}')

        # get growth rate
        new_number_fish = fish_school.get_number_of_fish()
        all_growths.append(new_number_fish)
        print(f'Growth rate day {day}: {new_number_fish/original_number_fish}, mean: {all_growths.mean()}')
        original_number_fish = new_number_fish


    print(fish_school.get_number_of_fish())



if __name__ == '__main__':
    main()
