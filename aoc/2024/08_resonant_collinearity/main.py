import os

from aoc.util.get_input import get_input


class AntennaMap:
    def __init__(self, data: list[str]):
        self.map = []
        for line in data:
            self.map.append([{"node": x, "antinodes": []} for x in line])
        self.rows = len(self.map)
        self.columns = len(self.map[0])
        self.antinode_positions = 0

    def node_mapper(self):
        for r in range(self.rows):
            for c in range(self.columns):
                node = self.map[r][c]["node"]
                if node != ".":
                    self.find_like_nodes(node, (r, c))

    def find_distinct_antinode_positions(self):
        for r in range(self.rows):
            for c in range(self.columns):
                if self.map[r][c]["antinodes"]:
                    self.antinode_positions += 1

    def find_like_nodes(self, node: str, node_position: tuple[int, int]):
        for r in range(self.rows):
            for c in range(self.columns):
                if self.map[r][c]["node"] == node and (r, c) != node_position:
                    self.create_antinode(node_position, (r, c))

    def create_antinode(
        self, node_one_position: tuple[int, int], node_two_position: tuple[int, int]
    ):
        self.map[node_one_position[0]][node_one_position[1]]["antinodes"].append(
            node_one_position
        )
        position_diff = (
            node_two_position[0] - node_one_position[0],
            node_two_position[1] - node_one_position[1],
        )
        antinode_position = (
            node_two_position[0] + position_diff[0],
            node_two_position[1] + position_diff[1],
        )
        ar, ac = antinode_position
        if 0 <= ar < self.rows and 0 <= ac < self.columns:
            self.map[ar][ac]["antinodes"].append(node_two_position)
        while 0 <= ar < self.rows and 0 <= ac < self.columns:
            self.map[ar][ac]["antinodes"].append(antinode_position)
            ar += position_diff[0]
            ac += position_diff[1]


def main():
    if os.path.exists("aoc/2024/08_resonant_collinearity/input.txt"):
        with open("aoc/2024/08_resonant_collinearity/input.txt") as f:
            data = f.read()
    else:
        data = get_input(8, 2024)
        with open("aoc/2024/08_resonant_collinearity/input.txt", "w") as f:
            f.write(data)
    antenna_map = AntennaMap(data.split("\n"))
    antenna_map.node_mapper()
    antenna_map.find_distinct_antinode_positions()
    print(antenna_map.antinode_positions)


if __name__ == "__main__":
    main()
