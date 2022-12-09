def solve(lines):
    # print(lines)
    visible_count = 0
    border = 2 * (len(lines)-1) + 2 * (len(lines[0])-1)
    visible_count += border

    for i, line in enumerate(lines):
        if i == 0 or i == len(lines) - 1:
            # print("skip first,last line")
            continue

        for j, char in enumerate(line):
            if j == 0 or j == len(line) - 1:
                # print("skip front, back")
                continue

            val = int(char)

            # From left
            if j > 0:
                if max([int(x) for x in line[0:j]]) < val:
                    visible_count += 1
                    # print(i,j,"found from left")
                    continue

            # From right
            if j < len(line) - 1:
                if max([int(x) for x in line[j + 1:]]) < val:
                    visible_count += 1
                    # print(i,j,"found from right")
                    continue

            col = list(map(lambda line: line[j], lines))
            # print("".join(col))

            # From top
            if i > 0:
                if max([int(x) for x in col[0:i]]) < val:
                    visible_count += 1
                    # print(i,j,"found from top")
                    continue

            # From bottom
            if i < len(lines) - 1:
                if max([int(x) for x in col[i + 1:]]) < val:
                    visible_count += 1
                    # print(i,j,"found from bottom")
                    continue

            # print(i,j,"Not found!")

    # print("border", border)
    print("visible", visible_count)
