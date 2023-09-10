#!/usr/bin/env python

"""
Compile multiple markdown into one README
"""

__author__ = "seyLu"
__github__ = "github.com/seyLu"

__licence__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "seyLu"
__status__ = "Prototype"


import os
import re
import sys

MARKDOWN_PATH = "markdown"
SECTIONS_PATH = os.path.join(MARKDOWN_PATH, "sections")


def main() -> None:
    input_file = os.path.join(MARKDOWN_PATH, "main.md")
    output_file = os.path.join("README.md")

    process(input_file, output_file)


def process(input_file: str, output_file: str) -> None:
    try:
        input_f = open(input_file)
    except FileNotFoundError:
        sys.exit("Error: main.md not found")
    else:
        try:
            os.remove(output_file)
        except OSError:
            pass

        lines = input_f.read()

        pattern = re.compile(r"#include \"([\w\/-]*)\"")
        file_path_matches = re.findall(pattern.pattern, lines)

        for file_path in file_path_matches:
            complete_file_path = os.path.join(SECTIONS_PATH, f"{file_path}.md")
            compile(complete_file_path, output_file)

        input_f.close()


def compile(file_path: str, output_file: str) -> None:
    try:
        file_f = open(file_path)
    except FileNotFoundError:
        sys.exit(f"Error: {file_path} not found")
    else:
        with open(output_file, "a+") as output_f:
            for line in file_f.readlines():
                output_f.write(line)
            output_f.write("\n")

        file_f.close()


if __name__ == "__main__":
    main()
