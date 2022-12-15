from collections import namedtuple
from typing import List


class Stack:

    def __init__(self) -> None:
        self.containers = None
    
    def fill_containers(self, object_list: List) -> None:
        self.containers.append(*object_list)

    
    def remove_crate(self):
        self.containers.pop()
    
    def add_crate(self):
        self.containers.append()



