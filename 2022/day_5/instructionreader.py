import re
from typing import List
from collections import namedtuple

class InstructionReader:
    """ _summary_

    _extended_summary_
    """
    def __init__(self, instruction_list: List) -> None:
        self.instructions = (x for x in instruction_list)
        print(type(self.instructions))


    @staticmethod
    def parse_move(move: str) -> List:
        return re.findall(r"\d+", move)

    
    @staticmethod
    def get_move(x):
        move = namedtuple("Move",["step", "source", "destination"])
        alist = InstructionReader.parse_move(next(x))
        move = move(step=alist[0], source=alist[1], destination=alist[2])
        return move

    
    def next_move(self):
        return self.get_move(self.instructions)

