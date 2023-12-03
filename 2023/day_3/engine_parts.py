import re
from itertools import chain
from pprint import pprint
with open("input.csv", "r", encoding="utf-8") as f:
    data = f.readlines()

print("rownum: ",len(data))
row = data[1]
print("row len: ", len(row))
print("row: ",row)


# print(re.findall(r"(\W)", row.strip("\n")))`

# print(len(re.findall(r"(\W)", row.strip("\n"))))


special_chars = set(chain.from_iterable([[char for char in re.findall(r"(\W)", row.strip("\n")) if char != '.'] for row in data]))
print(len(list(chain.from_iterable([[char for char in re.findall(r"(\W)", row.strip("\n")) if char != '.'] for row in data]))))
print(special_chars)
rows_2_check = {}
cur_row_idx = 0
for row in data:

    cols_2_check = []
    cur_col_idx = 0
    for char in row:
        if char in special_chars:
            cols_2_check.append(cur_col_idx)
        cur_col_idx += 1
    if cols_2_check:
        rows_2_check[cur_row_idx] = cols_2_check
    cur_row_idx += 1

num_rows = {}
num_row_idx = 0

def check_left(row,col):
    print(row+1,col)
    if data[row][col-1].isnumeric():
        num = re.findall(r"(\d+)", data[row][col-3: col])
        if num:
            print("left")
            print(f"row: {row+1}, col: {col}, num: {int(num[0])}")
            print("")
            return int(num[0])

def check_right(row,col):
    print(row+1,col)
    if data[row][col+1].isnumeric():
        num = re.findall(r"(\d+)", data[row][col+1: col + 4])
        if num:
            print("right")
            print(f"row: {row+1}, col: {col+1}, num: {int(num[0])}")
            print("")
            return int(num[0])
        
def check_up(row,col):
    print(row+1,col)
    if data[row-1][col].isnumeric():
        num = re.findall(r"(\d+)", data[row-1][col-2:col+2])
        print("up")
        print(f"row: {row}, col: {col}, num: {int(num[0])}")
        print("")
        return int(num[0])

def check_down(row,col):
    print(row+1,col)
    if data[row+1][col].isnumeric():
        num = re.findall(r"(\d+)", data[row+1][col-2:col+2])
        print("down")
        print(f"row: {row+2}, col: {col}, num: {int(num[0])}")
        print("")
        return int(num[0])
    

def check_top_right(row,col):
    print(row+1,col)
    print(row,col)
    if data[row-1][col+1].isnumeric():
        num = re.findall(r"(\d+)", data[row-1][col+1:col+4])
        print("top right")
        print(f"row: {row}, col: {col+1}, num: {int(num[0])}")
        print("")
        return int(num[0])


def check_top_left(row,col):
    print(row+1,col)
    if data[row-1][col-1].isnumeric():
        num = re.findall(r"(\d+)", data[row-1][col-3:col])
        print("top left")
        print(f"row: {row}, col: {col-1}, num: {int(num[0])}")
        print("")
        return int(num[0])


def check_bottom_left(row,col):
    print(row+1,col)
    if data[row+1][col-1].isnumeric():
        num = re.findall(r"(\d+)", data[row+1][col-3:col])
        print("top left")
        print(f"row: {row+2}, col: {col-1}, num: {int(num[0])}")
        print("")
        return int(num[0])

def check_bottom_right(row,col):
    print(row+1,col)
    if data[row+1][col+1].isnumeric():
        num = re.findall(r"(\d+)", data[row+1][col+1:col+4])
        print("top right")
        print(f"row: {row+2}, col: {col+1}, num: {int(num[0])}")
        print("")
        return int(num[0])

nums = []
for row_num in rows_2_check.keys():
    for col in rows_2_check[row_num]:
        # if check_left(rows_2_check[row_num][col]):
        left = check_left(row_num, col)
        right = check_right(row_num, col)
        up = check_up(row_num, col)
        down = check_down(row_num,col)

        if up:
            nums.append(up)
        else:
            top_right = check_top_right(row_num, col)
            if top_right:
                nums.append(top_right)

        if down:
            nums.append(down)
        else :
            down_right = check_bottom_right(row_num, col)
            if down_right:
                nums.append(down_right)
        
        if left:
            nums.append(left)
        if right:
            nums.append(right)
print(nums)
print(sum(nums))
print(len(nums))


print(len(list(chain.from_iterable([[char for char in re.findall(r"(\W)", row.strip("\n")) if char != '.'] for row in data]))))
print(special_chars)



# def get_adj_idx(idx):


# def find_adjacent(idx)