from typing import List

class Stack:

    def __init__(self, object_list) -> None:
        self.containers = object_list
        
    
    # def fill_containers(self, object_list: List) -> None:
    #     self.containers.append(object_list)
    #     self.containers = [ x for x in self.containers]
    def remove_crate(self):
        return self.containers.pop()
    
    def add_crate(self, crate):
        self.containers.append(crate)





# class Crane:

#     def __init__(self, stack: Stack) -> None:
#         self.stack = stack
#         pass

#     def move_crate(self, source, destination):
#         crate = self.stack.remove_crate()
        
#     def add_stack(self, stack: Stack) -> None:
            