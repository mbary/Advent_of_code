from collections import namedtuple
from typing import List, Dict
import re

from instructionreader import InstructionReader
from dock import Stack


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = file.read().splitlines()
    
    return data


data = parse_input("input.txt")

print(re.findall(r"\d+", data[0]))

stack_dict = {
        "1":Stack(["R","S","L","F","Q"])
    ,   "2":Stack(["N","Z","Q","G","P","T"])
    ,   "3":Stack(["S", "M", "Q", "B"])
    ,   "4":Stack(["T","G","Z","J","H","C","B","Q"])
    ,   "5":Stack(["P","H","M", "B","N","F","S"])
    ,   "6":Stack(["P","C","Q","N","S","L","V","G"])
    ,   "7":Stack(["W","C","F"])
    ,   "8":Stack(["Q","H","G","Z","W","V", "P","M"])
    ,   "9":Stack(["G","Z","D","L","C","N","R"])
}
# stack = Stack(object_list=["R","S","L","F","Q"])
# print(type(stack))
print(type(stack_dict["1"]))


class DockWorker:

    def __init__(self, stacks: Dict[str, Stack], instructions: InstructionReader) -> None:
        self.instructions = instructions
        self.stacks = stacks
        pass

    def move_crate(self, source: str, destination: str) -> None:
        crate = self.stacks[source].remove_crate()
        # print(source,crate)
        self.stacks[destination].add_crate(crate)


    def complete_instructions(self):
        for i in range(len(data)):
            move = self.instructions.next_move()
            step, destination, source = move.step, move.destination, move.source
            print("step", step)
            print("destination", destination)
            print("source", source)
            for _ in range(int(step)):
                self.move_crate(source=source, destination=destination)


    def get_stacks(self):
        print({x:y.containers for x,y in self.stacks.items() })

instructions = InstructionReader(data)


worker = DockWorker(stacks=stack_dict, instructions=instructions)
worker.complete_instructions()
print(worker.get_stacks())