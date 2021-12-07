"""
Hypothermal vents!! Watch out!
Task 1: Given some lines (starting point and ending point) calculate all
intersections of those lines
Task 2: Same but take into account diagonal lines
"""

from typing import List
from collections import Counter


class Point():
    """
    Overengineered class to store a point (x,y)
    Dataclass did not suffice because I also want to get the string form of the point
    """

    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def get_string(self):
        return (f'{self.x},{self.y}')


class Line():
    """
    Class to hold the line
    Each line has a first point and last points (x1, y1) and (x2, y2)
    Each line has a vector, which is point_2 - point_1, or in other words: (x2-x1, y2-y1)
    This vector indicates direction, and it will be used to get the points from the line.
    """

    def __init__(self, first_point: Point, last_point: Point):
        self.first_point = first_point
        self.last_point = last_point
        self.vector = Point(last_point.x - first_point.x, last_point.y - first_point.y)

    def get_points_of_line(self, diagonal=False):
        """
        Calculate the points that a line crosses.
        To do so, we see if any point in the vector is 0, which indicates no movement.
        If the value diagonal is set, lines that have a diagonal movement will return points


        The strategy to generate the points of the line is simple:
        - Determine the movement with the sign of the vector
        - Create a range between the first point and last
        - Append all points and return
        """
        points = []
        sign_vector_x = 1 if self.vector.x > 0 else -1
        sign_vector_y = 1 if self.vector.y > 0 else -1

        if self.vector.x == 0:  # y value changes
            for i in range(self.first_point.y, self.last_point.y + sign_vector_y, sign_vector_y):
                points.append(Point(self.first_point.x, i))
            return points

        elif self.vector.y == 0:  # x value changes
            for i in range(self.first_point.x, self.last_point.x + sign_vector_x, sign_vector_x):
                points.append(Point(i, self.first_point.y))
            return points

        elif diagonal:
            list_of_x = list(
                range(self.first_point.x, self.last_point.x + sign_vector_x, sign_vector_x)
            )
            list_of_y = list(
                range(self.first_point.y, self.last_point.y + sign_vector_y, sign_vector_y)
            )
            for x, y in zip(list_of_x, list_of_y):
                points.append(Point(x, y))
            return points

        return None  # if no match


def get_lines(path_to_input: str) -> List[Line]:
    """
    Split the input into lines. Lines are made of two points (x1, y1) and (x2, y2)
    """

    with open(path_to_input) as f:
        lines = f.readlines()

    raw_lines = [line.strip() for line in lines]

    lines = []
    for raw_line in raw_lines:
        point_1, point_2 = raw_line.split(' -> ')
        x1, y1 = point_1.split(',')
        x2, y2 = point_2.split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        lines.append(Line(Point(x1, y1), Point(x2, y2)))
    return lines


def get_points(lines: List[Line], diagonal=False) -> List[Point]:
    """
    Given all lines, get all the points combined of all lines stored in a list
    """
    all_points = []
    for line in lines:
        points = line.get_points_of_line(diagonal)
        if points is not None:
            all_points += points
    return all_points


def main():
    """
    The approach is the following:

    Gather the lines and store them in a class called Line
    This class can retrieve the Points that make up a line
    By creating a counter of those points, you can see how many of those points
    were repeated more than once.

    Regarding both parts, part 1 you don't have to take into acccounts
    diagonals, but in part 2 you do.

    Part 2 is a minor change with the flag `diagonal=True` so that the function get_points_of_line
    Returns diagonal points as well.
    """

    # input
    input_filename = 'day_5/input_hard.txt'
    lines: List[Line] = get_lines(input_filename)

    # part 1
    points: List[Point] = get_points(lines)
    points_string: List[str] = [point.get_string() for point in points]
    counter_of_points = dict(Counter(points_string))
    intersection_of_lines = [item for item in list(counter_of_points.values()) if item > 1]
    print(f'Part 1: {len(intersection_of_lines)}')

    # part 2
    points: List[Point] = get_points(lines, diagonal=True)
    points_string: List[str] = [point.get_string() for point in points]
    counter_of_points = dict(Counter(points_string))
    intersection_of_lines = [item for item in list(counter_of_points.values()) if item > 1]
    print(f'Part 2: {len(intersection_of_lines)}')


if __name__ == '__main__':
    main()
