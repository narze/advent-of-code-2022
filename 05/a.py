import re

def solve(lines):
    stacks_input = []
    nums = ""
    moves = []
    state = 0
    stacks = {}

    # Prep data
    for line in lines:
        if state == 0:
            if line.strip()[0].isnumeric():
                nums = line
                state = 1
            else:
                stacks_input.append(line)
        else:
            if line != "":
                moves.append(line)

    # Put in stacks
    for i, c in enumerate(nums):
        if c.isnumeric():
            if c not in stacks:
                stacks[c] = []
            for stack_line in reversed(stacks_input):
                if i < len(stack_line) and stack_line[i].isalpha():
                    stacks[c].append(stack_line[i])

    # print(stacks)
    regex = re.compile(r'move (\d+) from (\d+) to (\d+)')

    # Move items by popping & appending
    for move in moves:
        move_count, from_stack, to_stack = regex.search(move).groups()

        for _ in range(int(move_count)):
            item = stacks[from_stack].pop()
            stacks[to_stack].append(item)

    # print(stacks)

    # Get top item from each stack
    [print(stack[-1], end="") for stack in stacks.values()]
