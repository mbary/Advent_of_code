from collections import namedtuple
from typing import List, Dict
import re

from instructionreader import InstructionReader
from dock import Stack, Stack2


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = file.read().splitlines()
    
    return data


data = parse_input("input.txt")

print(re.findall(r"\d+", data[0]))

stack_dict = {
        "1":Stack2(["R","S","L","F","Q"])
    ,   "2":Stack2(["N","Z","Q","G","P","T"])
    ,   "3":Stack2(["S", "M", "Q", "B"])
    ,   "4":Stack2(["T","G","Z","J","H","C","B","Q"])
    ,   "5":Stack2(["P","H","M", "B","N","F","S"])
    ,   "6":Stack2(["P","C","Q","N","S","L","V","G"])
    ,   "7":Stack2(["W","C","F"])
    ,   "8":Stack2(["Q","H","G","Z","W","V", "P","M"])
    ,   "9":Stack2(["G","Z","D","L","C","N","R"])
}
# stack = Stack(object_list=["R","S","L","F","Q"])
# print(type(stack))
print(type(stack_dict["1"]))


class DockWorker:

    def __init__(self, stacks: Dict[str, Stack2], instructions: InstructionReader) -> None:
        self.instructions = instructions
        self.stacks = stacks
        pass

    def move_crate(self, source: str, destination: str, num: int) -> None:
        crate = self.stacks[source].remove_crate(num=int(num))
        # print(source,crate)
        

        self.stacks[destination].containers =  self.stacks[destination].containers + crate
        del self.stacks[source].containers[-int(num):]


    def complete_instructions(self):
        for i in range(len(data)):
            move = self.instructions.next_move()
            step, destination, source = move.step, move.destination, move.source
            print("step", step)
            print("destination", destination)
            print("source", source)
            self.move_crate(source=source, destination=destination, num=step)
            # for _ in range(int(step)):
            #     self.move_crate(source=source, destination=destination)


    def get_stacks(self):
        print({x:y.containers for x,y in self.stacks.items() })

instructions = InstructionReader(data)


worker = DockWorker(stacks=stack_dict, instructions=instructions)
worker.complete_instructions()
print(worker.get_stacks())