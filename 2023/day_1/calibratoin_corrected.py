DIGIT_DICT = {"zero":0,"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}



def _get_first_digit(string):
    char_so_far = ""
    for char in string:
        char_so_far += char
        for key in DIGIT_DICT.keys():
            if key in char_so_far:
                return str(DIGIT_DICT[key])
            elif char.isdigit():
                return char

def _get_last_digit(string):
    char_so_far = ""
    for char in string[::-1]:
        char_so_far += char
        for key in DIGIT_DICT.keys():
            if key in char_so_far[::-1]:
                return str(DIGIT_DICT[key])
            elif char.isdigit():

                return char 



def _get_cal_values(string):
    first = _get_first_digit(string)
    last = _get_last_digit(string)
    final = int(str(first) + str(last))
    return final



if __name__ == "__main__":

    all_cal_vals = 0
    with open("./input.csv", "r", encoding="utf-8") as f:
        data = f.readlines()
        for line in data:
            print("this is line",line)
            all_cal_vals += _get_cal_values(line)

    print(all_cal_vals)