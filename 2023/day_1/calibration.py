def _get_first_digit(string):
    # print(string)
    for char in string:
        if char.isdigit():
            # print(char)
            return char

def _get_last_digit(string):
    for char in string[::-1]:
        if char.isdigit():
            # print(char)
            return char 



def _get_cal_values(string):
    first = _get_first_digit(string)
    last = _get_last_digit(string)
    # print(first, last)
    return int(first + last)


all_cal_vals = 0

if __name__ == "__main__":

    with open("./input.csv", "r", encoding="utf-8") as f:
        data = f.readlines()
        # print(data)
        for line in data:
            print("this is line",line)
            all_cal_vals += _get_cal_values(line)


    print(all_cal_vals)



