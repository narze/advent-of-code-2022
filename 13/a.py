def solve(lines):
    pairs = []

    for i in range(0, len(lines), 3):
        pairs.append((eval(lines[i]), eval(lines[i+1])))

    sum = 0
    for i, pair in enumerate(pairs):
        print(pair)
        if compare(pair[0], pair[1]) == -1:
            sum += i + 1
    print(sum)

def compare(a, b):
    print(f"Comparing {a} and {b}")

    if type(a) is int and type(b) is int:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    if type(a) is int and type(b) is not int:
        return compare([a], b)

    if type(a) is not int and type(b) is int:
        return compare(a, [b])

    if type(a) is list and type(b) is list:
        if len(a) == 0 and len(b) == 0:
            return 0
        elif len(a) == 0 and len(b) > 0:
            return -1
        elif len(a) > 0 and len(b) == 0:
            return 1

        if compare(a[0], b[0]) == 0:
            return compare(a[1:], b[1:])
        else:
            return compare(a[0], b[0])
