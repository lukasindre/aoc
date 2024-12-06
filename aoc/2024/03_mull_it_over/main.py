import re

from aoc.util.get_input import get_input


def main():
    data = get_input(3, 2024)
    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    total = 0
    for match in mul_pattern.finditer(data):
        total += int(match.group(1)) * int(match.group(2))
    print(total)

    enhanced_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")
    do = True
    total = 0
    for match in enhanced_pattern.finditer(data):
        if match.group() == "do()":
            do = True
        elif match.group() == "don't()":
            do = False
        elif do:
            total += int(match.group(1)) * int(match.group(2))
    print(total)


if __name__ == "__main__":
    main()
