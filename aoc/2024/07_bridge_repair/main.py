import os
from itertools import product

from aoc.util.get_input import get_input

MISSING_OPERATIONS = ["+", "*", "||"]  # remove `||` for part 1


class CalibrationEquation:
    def __init__(self, line: str):
        answer, addends = line.split(": ")
        self.answer = int(answer)
        self.addends = [int(x) for x in addends.split(" ")]
        self.is_calibrated = False

    def calibrate(self):
        all_operations = product(MISSING_OPERATIONS, repeat=len(self.addends) - 1)
        for operation in all_operations:
            total = self.addends[0]
            for i, op in enumerate(operation):
                if op == "+":
                    total += self.addends[i + 1]
                elif op == "*":
                    total *= self.addends[i + 1]
                elif op == "||":
                    total = int(f"{total}{self.addends[i + 1]}")
            if total == self.answer:
                self.is_calibrated = True
                break


def main():
    if os.path.exists("aoc/2024/07_bridge_repair/input.txt"):
        with open("aoc/2024/07_bridge_repair/input.txt") as f:
            data = f.read()
    else:
        data = get_input(7, 2024)
        with open("aoc/2024/07_bridge_repair/input.txt", "w") as f:
            f.write(data)
    total = 0
    for line in data.split("\n"):
        equation = CalibrationEquation(line)
        equation.calibrate()
        if equation.is_calibrated:
            total += equation.answer
    print(total)


if __name__ == "__main__":
    main()
