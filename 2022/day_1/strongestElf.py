# load in the dataset
with open("input.txt", "r") as f:
    split_data = f.read().splitlines()

coma_joined = ",".join(split_data)
double_split = coma_joined.split(",,")
int_split = [x.split(",") for x in double_split]
print(int_split)

digit_elfes = [[int(x) for x in elf] for elf in int_split]

def sum_elfs(data):
    return [sum(x) for x in data]

summed_elfes = sum_elfs(digit_elfes)

strongest_elf = max(summed_elfes)
top3_stronges_elfes = list(sorted(summed_elfes,reverse=True))[:3]

print(strongest_elf)
print(top3_stronges_elfes)