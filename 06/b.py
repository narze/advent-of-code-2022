def solve(lines):
    input = lines[0]

    for i in range(0, len(input)):
        print(input[i:i+14])
        if len(set(input[i:i+14])) == 14:
            print(i+14)
            break
