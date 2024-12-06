import os
from itertools import cycle

from aoc.util.get_input import get_input


class Gallivant:
    def __init__(self, patrol_space: list[str]):
        self.patrol_space = patrol_space
        self.steps = 1
        self.visits = []
        self.initial_position = self._find_initial_position()
        self.steps_cycle = cycle(
            [
                (-1, 0),  # up
                (0, 1),  # right
                (1, 0),  # down
                (0, -1),  # left
            ]
        )
        self.direction = next(self.steps_cycle)  # initial start as up
        self.ARBITRARY_UPPER_BOUND_FOR_LOOP = 7500

    def _find_initial_position(self):
        for r, row in enumerate(self.patrol_space):
            for c, char in enumerate(row):
                if char == "^":
                    self.visits.append((r, c))
                    return r, c

    def gallivant(self):
        current_row, current_column = self.initial_position
        while 0 <= current_row < len(self.patrol_space) and 0 <= current_column < len(
            self.patrol_space[0]
        ):
            direction_row, direction_column = self.direction
            next_step_row, next_step_column = (
                current_row + direction_row,
                current_column + direction_column,
            )
            if 0 <= next_step_row < len(
                self.patrol_space
            ) and 0 <= next_step_column < len(self.patrol_space[0]):
                if self.patrol_space[next_step_row][next_step_column] == "#":
                    self.direction = next(self.steps_cycle)
                else:
                    current_row, current_column = next_step_row, next_step_column
                    self.visits.append((current_row, current_column))
                    self.steps += 1
                    if self.steps > self.ARBITRARY_UPPER_BOUND_FOR_LOOP:
                        raise Exception("Fruit loops")
            else:
                break


def main():
    if os.path.exists("aoc_2024/06_guard_gallivant/input.txt"):
        with open("aoc_2024/06_guard_gallivant/input.txt") as f:
            data = f.read()
    else:
        data = get_input(6, 2024)
        with open("aoc_2024/06_guard_gallivant/input.txt", "w") as f:
            f.write(data)
    patrol_space = data.split("\n")
    gallivant = Gallivant(patrol_space)
    gallivant.gallivant()
    print(len(set(gallivant.visits)))
    obsruction_positions_for_loops = []
    ir, ic = gallivant.initial_position
    for i, row in enumerate(patrol_space):
        for j, char in enumerate(row):
            if char != "#" and char != "^" and (i, j) != (ir - 1, ic):
                new_patrol_space = patrol_space.copy()
                row_list = list(new_patrol_space[i])
                row_list[j] = "#"
                new_patrol_space[i] = "".join(row_list)
                gallivant = Gallivant(new_patrol_space)
                try:
                    gallivant.gallivant()
                except Exception:
                    obsruction_positions_for_loops.append((i, j))
    print(len(set(obsruction_positions_for_loops)))


if __name__ == "__main__":
    main()
