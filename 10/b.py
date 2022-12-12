def solve(lines):
    cycles = []
    acc = [1]

    for line in lines:
        if line.startswith("noop"):
            cycles.append(0)
        elif line.startswith("addx"):
            value = int(line.split(" ")[1])
            cycles.append(0)
            cycles.append(value)

    for c in cycles:
        acc.append(acc[-1] + c)

    screen = ""

    for i, pos in enumerate(acc):
        if i%40 == 0:
            screen += "\n"

        if (i % 40) == pos-1 or (i % 40) == pos or (i % 40) == pos+1:
            screen += "#"
        else:
            screen += "."

    print(screen)
