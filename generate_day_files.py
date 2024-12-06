import os

import click
from jinja2 import Environment, FileSystemLoader


def render_template(template_dir, template_file, context, output_dir, output_file):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)

    rendered_content = template.render(context)

    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, output_file), "w") as f:
        f.write(rendered_content)


@click.command()
@click.option("--day", required=True, type=int, help="Day of the event")
@click.option("--year", required=True, type=int, help="Year of the event")
@click.option("--puzzle_name", required=True, type=str, help="Name of the puzzle")
def main(day, year, puzzle_name):
    template_dir = "templates"
    template_files = ["main.py.jinja", "__init__.py.jinja", "README.md.jinja"]

    context = {"year": year, "day": day, "puzzle_name": puzzle_name}

    output_dir = f"aoc/{year}/{day:02}_{puzzle_name}"

    for template_file in template_files:
        render_template(
            template_dir,
            template_file,
            context,
            output_dir,
            template_file.replace(".jinja", ""),
        )


if __name__ == "__main__":
    main()
