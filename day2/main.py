
with open('day2.in') as file:
    rounds = [i for i in file.read().strip().split("\n")]

# print(rounds)

# ax - 1+3 = 4 - draw
# ay - 2+6 = 8 - win 
# az - 3+0 = 3 - lose
# bx - 1+0 = 1 - lose
# by - 2+3 = 5 - draw
# bz - 3+6 = 9 - win
# cx - 1+6 = 7 - win
# cy - 2+0 = 2 - lose
# cz - 3+3 = 6 - draw


outcomes = {
        "A X":4,"A Y":8,"A Z":3,
        "B X":1,"B Y":5,"B Z":9,
        "C X":7,"C Y":2,"C Z":6
        }


total_score_1= 0

for round in rounds:
    total_score_1 += outcomes[round]


outcomes2 = {
        "A X":3,"A Y":4,"A Z":8,
        "B X":1,"B Y":5,"B Z":9,
        "C X":2,"C Y":6,"C Z":7
        }

total_score_2= 0

for round in rounds:
    total_score_2 += outcomes2[round]

print("score for part 1",total_score_1)
print("score2 for part 2",total_score_2)
