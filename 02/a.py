entries = open("input.txt").readlines()

# entries = ["A Y", "B X", "C Z"]
op_moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}
my_moves = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

win = 6
draw = 3
lose = 0

score = {
    "rock": {
        "paper": win,
        "rock": draw,
        "scissors": lose,
    },
    "paper": {
        "paper": draw,
        "rock": lose,
        "scissors": win,
    },
    "scissors": {
        "paper": lose,
        "rock": win,
        "scissors": draw,
    },
}
base_score = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

def get_score(op_move, my_move):
    op_rps = op_moves[op_move]
    my_rps = my_moves[my_move]
    return score[op_rps][my_rps] + base_score[my_rps]

sum_score = 0

for entry in entries:
    op, me = entry.split()
    sum_score += get_score(op, me)

print(sum_score)
