from aoc.util.get_input import get_input


class Report:
    def __init__(self, line: list[int]):
        self.line = line
        self.sorted_asc = sorted(self.line)
        self.sorted_desc = sorted(self.line, reverse=True)

    def _is_sorted(self) -> bool:
        return any([self.line == self.sorted_asc, self.line == self.sorted_desc])

    def _small_changes(self) -> int:
        number_of_problems = 0
        index = 0
        while index < len(self.line) - 1:
            if 1 <= abs(self.line[index] - self.line[index + 1]) <= 3:
                pass
            else:
                number_of_problems += 1
            index += 1
        return number_of_problems

    def is_safe(self) -> bool:
        return self._is_sorted() and self._small_changes() == 0


def main():
    data = get_input(2, 2024)
    total_safe = 0
    could_be_safe = 0
    for line in data.split("\n"):
        report = Report([int(x) for x in line.split()])
        if report.is_safe():
            total_safe += 1
        else:
            sublists_one_less = [
                report.line[:i] + report.line[i + 1 :] for i in range(len(report.line))
            ]
            for sublist in sublists_one_less:
                report = Report(sublist)
                if report.is_safe():
                    could_be_safe += 1
                    break
    print(total_safe)
    print(total_safe + could_be_safe)


if __name__ == "__main__":
    main()
