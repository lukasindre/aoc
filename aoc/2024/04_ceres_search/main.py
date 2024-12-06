import os

from aoc.util.get_input import get_input


def main():
    if os.path.exists("aoc_2024/ceres_search/input.txt"):
        with open("aoc_2024/ceres_search/input.txt") as f:
            data = f.read()
    else:
        data = get_input(4, 2024)
        with open("aoc_2024/ceres_search/input.txt", "w") as f:
            f.write(data)

    count = 0
    mas_count = 0
    rows = data.split("\n")
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == "X":
                if (
                    j + 3 < len(row)
                    and row[j + 1] == "M"
                    and row[j + 2] == "A"
                    and row[j + 3] == "S"
                ):
                    count += 1
                if (
                    j - 3 >= 0
                    and row[j - 1] == "M"
                    and row[j - 2] == "A"
                    and row[j - 3] == "S"
                ):
                    count += 1
                if (
                    i + 3 < len(rows)
                    and rows[i + 1][j] == "M"
                    and rows[i + 2][j] == "A"
                    and rows[i + 3][j] == "S"
                ):
                    count += 1
                if (
                    i - 3 >= 0
                    and rows[i - 1][j] == "M"
                    and rows[i - 2][j] == "A"
                    and rows[i - 3][j] == "S"
                ):
                    count += 1
                if (
                    i + 3 < len(rows)
                    and j + 3 < len(row)
                    and rows[i + 1][j + 1] == "M"
                    and rows[i + 2][j + 2] == "A"
                    and rows[i + 3][j + 3] == "S"
                ):
                    count += 1
                if (
                    i - 3 >= 0
                    and j + 3 < len(row)
                    and rows[i - 1][j + 1] == "M"
                    and rows[i - 2][j + 2] == "A"
                    and rows[i - 3][j + 3] == "S"
                ):
                    count += 1
                if (
                    i + 3 < len(rows)
                    and j - 3 >= 0
                    and rows[i + 1][j - 1] == "M"
                    and rows[i + 2][j - 2] == "A"
                    and rows[i + 3][j - 3] == "S"
                ):
                    count += 1
                if (
                    i - 3 >= 0
                    and j - 3 >= 0
                    and rows[i - 1][j - 1] == "M"
                    and rows[i - 2][j - 2] == "A"
                    and rows[i - 3][j - 3] == "S"
                ):
                    count += 1
            if char == "A":
                # M . M
                # . A .
                # S . S
                # top down
                if (
                    j + 1 < len(row)
                    and j - 1 >= 0
                    and i + 1 < len(rows)
                    and i - 1 >= 0
                    and rows[i - 1][j - 1] == "M"
                    and rows[i - 1][j + 1] == "M"
                    and rows[i + 1][j - 1] == "S"
                    and rows[i + 1][j + 1] == "S"
                ):
                    mas_count += 1

                # S . S
                # . A .
                # M . M
                # down up
                if (
                    j + 1 < len(row)
                    and j - 1 >= 0
                    and i + 1 < len(rows)
                    and i - 1 >= 0
                    and rows[i - 1][j - 1] == "S"
                    and rows[i - 1][j + 1] == "S"
                    and rows[i + 1][j - 1] == "M"
                    and rows[i + 1][j + 1] == "M"
                ):
                    mas_count += 1

                # M . S
                # . A .
                # M . S
                # left right
                if (
                    j + 1 < len(row)
                    and j - 1 >= 0
                    and i + 1 < len(rows)
                    and i - 1 >= 0
                    and rows[i - 1][j - 1] == "M"
                    and rows[i - 1][j + 1] == "S"
                    and rows[i + 1][j - 1] == "M"
                    and rows[i + 1][j + 1] == "S"
                ):
                    mas_count += 1

                # S . M
                # . A .
                # S . M
                # right left
                if (
                    j + 1 < len(row)
                    and j - 1 >= 0
                    and i + 1 < len(rows)
                    and i - 1 >= 0
                    and rows[i - 1][j - 1] == "S"
                    and rows[i - 1][j + 1] == "M"
                    and rows[i + 1][j - 1] == "S"
                    and rows[i + 1][j + 1] == "M"
                ):
                    mas_count += 1

    print(count)
    print(mas_count)


if __name__ == "__main__":
    main()
