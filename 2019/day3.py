import pandas as pd

df = pd.read_csv("day3.csv", index_col= False)
df = df.transpose()
df.reset_index(inplace=True)

df.columns = ["input1", "input2"]
input1 = df["input1"].to_list()
input2 = df["input2"].to_list()


def simulate_movement(input_moves):
    coordinates = {}

    x = 0
    y = 0

    step = 0

    for move in input_moves:
        direction = move[0]
        distance = int(float(move[1:]))

        move_x = move_y = 0

        if direction == "L":
            move_x = -1

        elif direction == "R":
            move_x = 1
        
        elif direction == "D":
            move_y = -1

        elif direction == "U":
            move_y = 1
        
        for _ in range(0, distance):
            x += move_x
            y += move_y
            step +=1
        
            if (x,y) not in coordinates:
                coordinates[(x,y)] = step
    
    return coordinates


line_1 = simulate_movement(input1)
line_2 = simulate_movement(input2)


intersections = list(set(line_1.keys()) & set(line_2.keys()))

def shortest():
    distance = []

    for intersection in intersections:
        dist = abs(intersection[0]) + abs(intersection[1])
        distance.append(dist)
    return min(distance)

shortest()

def get_fewest():
    combined_steps = [line_1[i] + line_2[i] for i in intersections]
    return min(combined_steps)

get_fewest()