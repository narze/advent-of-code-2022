import functools

def solve(lines):
    entries = []

    entries.append([[2]])
    entries.append([[6]])

    for i in range(0, len(lines), 3):
        entries.append(eval(lines[i]))
        entries.append(eval(lines[i+1]))

    # print(entries)

    # sorted_entries = sorted(entries, cmp=compare) # Python 2
    sorted_entries = sorted(entries, key=functools.cmp_to_key(compare))

    packet_a = sorted_entries.index([[2]]) + 1
    packet_b = sorted_entries.index([[6]]) + 1

    print(packet_a, "*", packet_b, "=", packet_a * packet_b)

def compare(a, b):
    # print(f"Comparing {a} and {b}")

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
