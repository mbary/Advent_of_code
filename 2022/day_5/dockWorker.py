from collections import namedtuple
from typing import List
import re

from instructionreader import InstructionReader


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = file.read().splitlines()
    
    return data


data = parse_input("input.txt")

print(re.findall(r"\d+", data[0]))




