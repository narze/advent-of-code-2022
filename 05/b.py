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

    # Move items at once
    for move in moves:
        move_count, from_stack, to_stack = regex.search(move).groups()

        # Remove last move_count items from stack
        items = stacks[from_stack][-int(move_count):]
        del stacks[from_stack][-int(move_count):]
        [stacks[to_stack].append(item) for item in items]

    # Get top item from each stack
    [print(stack[-1], end="") for stack in stacks.values()]
