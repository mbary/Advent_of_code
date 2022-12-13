def parse_input(file_path):
    with open(file_path, "r") as f:
        data = f.read().splitlines()

    tuple_data = [list(x.split(" "))[0] for x in data]
    return tuple_data


data = parse_input("./input.txt")
# print(data)

data = [x.split(',') for x in data]
# print(data)
# data[0][0].split('-')


def get_pairs(x):
    p1,p2 = x[0],x[1]
    p1,p2 = p1.split('-'),p2.split('-')
    return ((int(p1[0]),int(p1[1])), (int(p2[0]), int(p2[1])))

pairs = [get_pairs(x) for x in data]
print(pairs[0])
    

def check_pair(x):

    p1,p2 = x[0],x[1]

    if p1[0]>= p2[0] and p1[1] <= p2[1]:
        return 1
    
    elif p2[0]>=p1[0] and p2[1]<=p1[1]:
        return 1
    
    else: return 0

overlapping = [check_pair(x) for x in pairs]
# print(overlapping)
print(sum(overlapping))
    