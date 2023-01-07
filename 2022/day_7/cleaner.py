# from pprint import pprint

# with open("./input.txt", "r", encoding="utf=8") as f:
#     data = f.read().splitlines()

# pprint(data)


# def is_file(x):
#     if x[0] != "$":
#         first,_ = x.split(" ")
#         return first.isnumeric()
    
#     else: return False

# def is_dir(x):
#     if x[0] != "$":
#         first,_ = x.split(" ")
#         return first == "dir"

#     else: return False

# def is_command(x):
#     return x.split(" ")[0] == "$"

# def is_cd(x):
#     return x.split(" ")[1] == "cd"    

# def parse_instructions(data):
#     pass

# def is_ls(x):
#     return x.split(" ")[1] == "ls"


# structure = {"/":{"parent":None,
#                 "children":{}}}

# current_dir = "/"

# for line in data:
#     if is_dir(line):
#         structure[current_dir]


from collections import defaultdict

with open("input.txt") as f:
    commands = f.readlines()

sizes = defaultdict(int)
stack = []

i = 0
for c in commands:
    if c.startswith("$ ls") or c.startswith("dir"):
        continue
    if c.startswith("$ cd"):
        dest = c.split()[2]
        if dest == "..":
            stack.pop()
        else:
            i += 1
            path = f"{stack[-1]}_{dest}" if stack else dest
            stack.append(path)
    else:
        size, file = c.split()
        for path in stack:
            sizes[path] += int(size)

needed_size = 30000000 - (70000000 - sizes["/"])
for size in sorted(sizes.values()):
    if size > needed_size:
        break

print(sum(n for n in sizes.values() if n <= 100000)) # task 1
print(size) # task 2