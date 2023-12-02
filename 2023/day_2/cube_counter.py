from pathlib import Path
import re

def read_input(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
    return data

def get_cubes(line):
    cube_dict = {}
    cubes = re.findall(r"(\d+\s\w+)",line)

    for pair in cubes:
        numb,col = pair.split(" ")
        if col in cube_dict.keys():
            cube_dict[col] += int(numb)
        else:
            cube_dict[col] = int(numb)
    
    return cube_dict  

def check_possibility(cube_dict):
    return all([cube_dict[col ]<=AVAILABLE_CUBES[col] for col in cube_dict.keys()])

def get_game_id(row):
    return int(re.findall(r"(\d+):",row)[0])


def calculate_corr_ids(data):
    corr_ids = 0

    for row in data:
        sets = row.split(";")
        if all(check_possibility(get_cubes(set)) for set in sets):
            corr_ids += get_game_id(row)

    return corr_ids 


AVAILABLE_CUBES = {
    "red":12,
    "green":13,
    "blue":14
}

if __name__ == "__main__":
        

    raw_data = read_input("./input.csv")

    data = raw_data.split("\n")

    print(calculate_corr_ids(data))
