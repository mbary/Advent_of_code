import string 

def parse_input(file_path):
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    
    data = [list(x.split()) for x in data]
    return data


def get_groups(my_list):
    
    groups = [[y[0] for y in my_list[x:x+3]] for x in range(0, len(my_list),3)]    
    return groups

data = parse_input("./input2.txt")

groups = get_groups(data)

smaller_dict = dict(zip((string.ascii_lowercase), range(1,27)))
upper_dict = dict(zip((string.ascii_uppercase), range(27,53)))

letter_dict = {**smaller_dict, **upper_dict}
print(data[3:6])
def get_allocationn(data):
    all_uniques = []
    for x in data:
        a,b,c = set(x[0]),set(x[1]), set(x[2])
        int_all = a.intersection(b,c)
        all_uniques.append(list(int_all)[0])
    return all_uniques

all_allocations = get_allocationn(groups)

print(all_allocations)
point_sum = sum([letter_dict[x] for x in all_allocations])
print(point_sum)
