from typing import Generator, List


def read_data(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def yield_data(file_path: str) -> str:
    for row in open(file_path, "r", encoding="utf=8"):
        yield row.split()

data = read_data("./input.txt")
print(data)
# data = yield_data("./input.txt")
data_gen = (char for char in data)

def pass_data(ds):
    return next(ds)



def get_packet(stream: Generator) -> List:
    packet = list()
    packet_set = set()
    start_index = 0
    while len(packet_set) < 4:
        packet.append(pass_data(stream))
        start_index += 1
        print(packet)
        if len(packet) == 4:
            packet_set = set(packet)
            print(packet_set)
            if len(packet_set) <5:
                packet.pop(0)
        
    return start_index

# indecies = []

# try:
#     for i in range(len(data)):
#         indecies.append(get_packet(data_gen))
# except:
#     pass
# print(indecies)
get_packet(data_gen)