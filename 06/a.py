def solve(lines):
    input = lines[0]

    for i in range(0, len(input)):
        print(input[i:i+4])
        if len(set(input[i:i+4])) == 4:
            print(i+4)
            break
