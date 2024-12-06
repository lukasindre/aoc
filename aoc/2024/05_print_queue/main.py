import os

from aoc.util.get_input import get_input


class Update:
    def __init__(self, update_sequence: list[int]):
        self.update_sequence = update_sequence
        self.correct_order = True
        self.middle_number = self.update_sequence[len(self.update_sequence) // 2]

    def determine_order(self, ordering_rules: list[tuple[int, int]]):
        for i, x in enumerate(self.update_sequence):
            if i == 0:
                pre_sub_list = []
                post_sub_list = self.update_sequence[i + 1 :]
            elif i == len(self.update_sequence) - 1:
                pre_sub_list = self.update_sequence[:i]
                post_sub_list = []
            else:
                pre_sub_list = self.update_sequence[:i]
                post_sub_list = self.update_sequence[i + 1 :]
            for y in pre_sub_list:
                if (y, x) not in ordering_rules:
                    self.correct_order = False
                    return
            for y in post_sub_list:
                if (x, y) not in ordering_rules:
                    self.correct_order = False
                    return

    def fix_order(self, ordering_rules: list[tuple[int, int]]):
        pass


def main():
    if os.path.exists("aoc_2024/05_print_queue/input.txt"):
        with open("aoc_2024/05_print_queue/input.txt") as f:
            data = f.read()
    else:
        data = get_input(5, 2024)
        with open("aoc_2024/05_print_queue/input.txt", "w") as f:
            f.write(data)
    order_data, update_data = data.split("\n\n")
    ordering = []
    for line in order_data.split("\n"):
        x, y = line.split("|")
        ordering.append((int(x), int(y)))
    updates = []
    for line in update_data.split("\n"):
        updates.append([int(x) for x in line.split(",")])
    total = 0
    for update in updates:
        u = Update(update)
        u.determine_order(ordering)
        if u.correct_order:
            total += u.middle_number
    print(total)


if __name__ == "__main__":
    main()
