"""
Lantern fish
Task 1: Count have many lantern fish there are in a pack after 80 days
Task 2: Same but in 256 days

[Task 1] We create a class named Fish. This class will serve us to track
the age of the fish and their cycle. Fish can have new offspring!
To help with the Fish, we create the class FishSchool, used to track the whole
school of Fish. And automatically append new babies.

[Task 2] Performance is an issue. 80 days is doable, but 256 is too much.
If we look closely, there are multiple repeated Fish with the same qualities (`age` and `cycle`).
We can combine these and keep a count of how many there are!
This is done with the method `sort_fish`. To be able to sort them, we need to
create the methods `__str__`, `__hash__` and `__eq__` to the class Fish.
This is done in order to hash the Fish into a dictionary and be able to count them.
We then reduce the amount of Fish to a handful and track their units.
"""

from typing import List

NEW_BORN_CYCLE = 8
ADULT_CYCLE = 6

class Fish():
    """
    Welcome to the class Fish!!
    It has some attributes:
        - age. If age reaches 0 the Fish will have a baby! Age works backwards
        - cycle. After having a baby the age is restarted to this value
        - units. Keeping track of how many fish are identical

    Let's say I create a Fish.

    salmon = Fish(age=1)
    potential_baby = salmon.next_day() # potential baby = None
    salmon.age # age=0, it will have a baby next day
    baby_salmon = salmon.next_day() # baby_salmon=Fish(), age=ADULT_CYCLE, cycle=ADULT_CYCLE
    """

    def __init__(self, age: int, new_born=False, units=1):
        self.age = age
        self.cycle = ADULT_CYCLE
        self.units = units
        if new_born:
            self.age = NEW_BORN_CYCLE
            self.cycle = NEW_BORN_CYCLE

    def next_day(self):
        if self.age == 0:
            self.age = ADULT_CYCLE
            self.cycle = ADULT_CYCLE
            kid = Fish(self.cycle, new_born=True, units=self.units)
            return kid

        self.age -= 1
        return None
    

    def __eq__(self, other) : 
        """
        In order to compare if two Fish are the same, we need to compare their age and their cycle
        """
        return self.age == other.age and self.cycle == other.cycle

    def __str__(self):
        """
        In order to print information about Fish
        """
        return f'Age {self.age}, Cycle {self.cycle}'

    def __hash__(self):
        """
        To be able to count different Fish we need to be able to hash them
        based on their age and cycle
        """
        return hash(str(self))


class FishSchool():
    """
    All fish are stored here!
    """

    def __init__(self, all_fish: List[Fish]):
        """
        Initialize the school with a list of Fish!
        """
        self.all_fish = all_fish.copy()

    def next_day(self):
        """
        Run the method .next_day for all fish in the school
        Append newborns to `all_fish`!
        """
        new_borns = []
        for fish in self.all_fish:
            potential_new_fish = fish.next_day()
            if type(potential_new_fish) == Fish:
                new_borns.append(potential_new_fish)
        self.all_fish += new_borns # update pack

    def get_number_of_fish(self) -> int:
        return sum([fish.units for fish in self.all_fish])

    def sort_fish(self):
        """
        Count the fish with the same `age` and `cycle`.
        It will group all the fish with the same properties and increment their units
        This class updates the attribute `self.all_fish` and their units

        Example:
        # sorting fish
        list_of_fish = [Fish(1), Fish(1), Fish(1), Fish(2)]
        school_of_fish = FishSchool(list_of_fish)
        school_of_fish.sort_fish()

        # same result as:
        list_of_fish_sorted = [Fish(1, units=3), Fish(2)]
        school_of_fish = FishSchool(list_of_fish_sorted)
        """

        dict_of_fish = {}
        for fish in self.all_fish:
            # fish not in dict
            if fish not in dict_of_fish.values():
                dict_of_fish[fish] = fish
            # fish is repeated
            else:
                dict_of_fish[fish].units += fish.units
        self.all_fish = list(dict_of_fish.values())


def get_initial_pack_of_fish(input_filename: str) -> List[Fish]:
    """
    Get input file and return list of Fish
    """
    with open(input_filename) as f:
        lines = f.readlines()

    fish_raw = lines[0].strip().split(',')
    fish_int = [int(fish) for fish in fish_raw]
    fish_bank = [Fish(age_of_fish) for age_of_fish in fish_int]

    return fish_bank


def get_number_of_fish_given_days(fish_list: List[Fish], days: int) -> int:
    """
    Given X days, run simulation of how many Fish there will be in the school
    """
    fish_school = FishSchool(fish_list)
    for _ in range(1, days+1):
        fish_school.next_day()
        fish_school.sort_fish()

    return fish_school.get_number_of_fish()


def main():
    # input
    input_filename = 'day_6/input_hard.txt'

    # part 1
    fish_list: List[Fish] = get_initial_pack_of_fish(input_filename)
    total_fish = get_number_of_fish_given_days(fish_list, 80)
    print('Part 1', total_fish)

    # part 2
    fish_list: List[Fish] = get_initial_pack_of_fish(input_filename)
    total_fish = get_number_of_fish_given_days(fish_list, 256)
    print('Part 2', total_fish)

if __name__ == '__main__':
    main()
