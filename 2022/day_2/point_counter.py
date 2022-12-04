def parse_input(file_path):
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    # data = data.split(",")
    # print(data)
    # print(",".join(data).split(" "))
    tuple_data = [tuple(x.split(" ")) for x in data]
    print(tuple_data)

parse_input("./input.txt")