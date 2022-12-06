"""
A - Rock
B - Paper
C - Scissors

X - Rock
Y - Paper
Z - Scissors
"""

def parse_input(file_path):
    with open(file_path, "r") as f:
        data = f.read().splitlines()

    tuple_data = [list(x.split(" ")) for x in data]
    return tuple_data

def convert_data(data):
    for x in data:
        x[1] = conversion[x[1]]
    return data

conversion = {"X":"A",
            "Y":"B",
            "Z":"C"}

fig_point_map = {"A":1
                , "B":2
                , "C":3}

result_point_map = {"win":6
                ,   "draw":3
                ,   "loss":0}                

# Beating mapping
# Key beats value
beat_map = {"A":"C"
        ,   "B":"A"
        ,   "C":"B"}

strategy = parse_input("./input.txt")   
     
strategy = convert_data(strategy)

print(strategy[0])
print(strategy[0][0], strategy[0][1])

class gamblingElf:
    def __init__(self,strategy) -> None:
        self.strategy = strategy
        self.total_score = 0
    
    def _play(self, play):
        opponent = play[0]
        us = play[1]

        #check if draw
        if opponent == us:
            return 3 + fig_point_map[us]

        # check if win
        elif opponent == beat_map[us]:
            return 6 + fig_point_map[us]

        else:
            return 0 + fig_point_map[us]



    def win_estimate(self):
        for play in self.strategy:
            result = self._play(play)
            self.total_score += result
            print(self.total_score)
        
        print(f"The final Result is: {self.total_score}")


gambling_addict = gamblingElf(strategy=strategy)

gambling_addict.win_estimate()