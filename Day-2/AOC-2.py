with open('input2.in') as file:
    rounds = [i for i in file.read().strip().split("\n")]
    
# print(rounds)

# ---------------------------------------------
# LEFT VS RIGHT | OUT | RIGHT + OUTCOME = TOTAL
# ---------------------------------------------
# A vs X = DRAW = (1 + 3) = 4
# A vs Y = WIN  = (2 + 6) = 8
# A vs Z = LOSS = (3 + 0) = 3
# B vs X = LOSS = (1 + 0) = 1
# B vs Y = DRAW = (2 + 3) = 5
# B vs Z = WIN  = (3 + 6) = 9
# C vs X = WIN  = (1 + 6) = 7
# C vs Y = LOSS = (2 + 0) = 2
# C vs Z = DRAW = (3 + 3) = 6

outcomes_1 = {
    "A X":4, "A Y":8, "A Z":3, 
    "B X":1, "B Y":5, "B Z":9, 
    "C X":7, "C Y":2, "C Z":6
}

total_points_1 = 0
for round in rounds:
    total_points_1 += outcomes_1[round]
    
outcomes_2 = {
    "A X":3, "A Y":4, "A Z":8, 
    "B X":1, "B Y":5, "B Z":9, 
    "C X":2, "C Y":6, "C Z":7
}

total_points_2 = 0
for round in rounds:
    total_points_2 += outcomes_2[round]
    
print(f"Answer to part 1 is {total_points_1}")
print(f"Answer to part 2 is {total_points_2}")
