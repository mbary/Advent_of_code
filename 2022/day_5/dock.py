from typing import List

class Stack:

    def __init__(self) -> None:
        self.containers = None
    
    def fill_containers(self, object_list: List) -> None:
        self.containers.append(*object_list)
    
    def remove_crate(self):
        self.containers.pop()
    
    def add_crate(self, crate):
        self.containers.append(crate)





class Crane:

    def __init__(self, stack: Stack) -> None:
        self.stack = stack
        pass

    def move_crate(self, source, destination):
        crate = self.stack.remove_crate()
        
    def add_stack(self, stack: Stack) -> None:
            