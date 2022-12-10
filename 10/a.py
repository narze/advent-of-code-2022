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

    print(acc)
    x = [20, 60, 100, 140, 180, 220]

    strength = 0
    for i in x:
        strength += i * acc[i-1]
    print(strength)
