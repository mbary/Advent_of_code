from collections import namedtuple
from typing import List
import re



def parse_input(file_path):
    with open(file_path, "r") as file:
        data = file.read().splitlines()
    
    return data


data = parse_input("input.txt")

print(re.findall(r"\d+", data[0]))




class Stack:

    def __init__(self) -> None:
        self.containers = None
    
    def fill_containers(self, object_list: List) -> None:
        self.containers.append(*object_list)

    
    def remove_crate(self):
        self.containers.pop()
    
    def add_crate(self):
        self.containers.append()



class InstructionReader:


    def __init__(self, instruction_list: List) -> None:
        self.instructions = (x for x in instruction_list)
        print(type(self.instructions))
    @staticmethod
    def parse_move(move):
        return re.findall(r"\d+", move)
    
    @staticmethod
    def get_move(x):
        move = namedtuple("Move",["step", "source", "destination"])
        
        alist = InstructionReader.parse_move(next(x))
        move = move(step=alist[0], source=alist[1], destination=alist[2])
        return move

    
    def next_move(self):
        return self.get_move(self.instructions)

test = InstructionReader(data)

move = test.next_move()
print(getattr(move,"destination"))
print(move.destination)
