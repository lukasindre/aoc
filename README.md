# Advent of Code

# Setup
## Project
This project uses [poetry](https://python-poetry.org/) to manage dependencies.  To install dependencies, run the following command:
```bash
poetry install
```
## Environment
This directory uses templates to generate puzzle directories and files. `main.py` in your puzzle directory runs your solution.
`main.py` will [automatically](./templates/main.py.jinja) get your puzzle input from [aoc](https://adventofcode.com) and cache it locally.
In order for this to happen, we read your local environment in search of an `AOC_SESSION` variable.  You can grab this
session token from your browser's cookies after logging into advent of code.  This token is used to authenticate your requests.
## Puzzle Generation
To generate a puzzle directory, run the following command with the correct day, year, and puzzle name:
```bash
 poetry run python3 generate_day_files.py --day <DD> --year <YYYY> --puzzle-name <puzzle_name>
```
