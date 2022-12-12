import string

def parse_input(file_path):
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    
    data = [list(x.split()) for x in data]
    return data


def sort_rucksack(rucksack):
    middle = int(len(rucksack[0])/2)
    left = rucksack[0][:middle]
    right = rucksack[0][middle:]
    return list([tuple(left),tuple(right)])

data = parse_input("./input.txt")

rucksacks = [sort_rucksack(rucksack) for rucksack in data]
smaller_dict = dict(zip((string.ascii_lowercase), range(1,27)))
upper_dict = dict(zip((string.ascii_uppercase), range(27,53)))

letter_dict = {**smaller_dict, **upper_dict}


def find_duplicate(x):
    duplicates = set(x[0]).intersection(set(x[1]))
    return list(duplicates)


all_duplicates = [find_duplicate(rucksack) for rucksack in rucksacks]


point_sum = sum([letter_dict[duplicate[0]] for duplicate in all_duplicates])
print(point_sum)



