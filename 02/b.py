entries = open("input.txt").readlines()

# entries = ["A Y", "B X", "C Z"]
op_moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

my_results = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

result_score = {
    "win": 6,
    "draw": 3,
    "lose": 0,
}

move = {
    "rock": {
        "lose": "scissors",
        "draw": "rock",
        "win": "paper",
    },
    "paper": {
        "lose": "rock",
        "draw": "paper",
        "win": "scissors",
    },
    "scissors": {
        "lose": "paper",
        "draw": "scissors",
        "win": "rock",
    },
}

base_score = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

def get_score(op_move, my_move):
    op_rps = op_moves[op_move]
    my_result = my_results[my_move]
    my_rps = move[op_rps][my_result]
    return base_score[my_rps] + result_score[my_result]

sum_score = 0

for entry in entries:
    op, me = entry.split()
    sum_score += get_score(op, me)

print(sum_score)
