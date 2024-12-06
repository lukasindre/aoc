import typing
from collections import Counter

from aoc.util.get_input import get_input


def main():
    input = get_input(1, 2024)
    first_column, second_column = split_and_sort(input)
    print(get_total_distance_sum(first_column, second_column))
    print(similarity_score(first_column, second_column))


def similarity_score(first_column: list[int], second_column: list[int]) -> int:
    c = Counter(second_column)
    score = 0
    for item in first_column:
        if item in c:
            score += int(item) * c[item]
    return score


def get_total_distance_sum(first_column: list[int], second_column: list[int]) -> int:
    total_distance = 0
    zipped_columns = zip(first_column, second_column)
    for pair in zipped_columns:
        total_distance += abs(int(pair[0]) - int(pair[1]))
    return total_distance


def split_and_sort(input: str) -> typing.Tuple[list[int], list[int]]:
    input_rows = input.split("\n")
    first_column = []
    second_column = []
    for row in input_rows:
        if row:
            first, second = row.split()
            first_column.append(first)
            second_column.append(second)
    first_column.sort()
    second_column.sort()
    return first_column, second_column


if __name__ == "__main__":
    main()
