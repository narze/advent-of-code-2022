def solve(lines):
    max_score = 0
    # Map input to int
    lines = list(map(lambda line: list(map(lambda x: int(x), line)), lines))

    print(max([get_score(lines, x, y) for x in range(len(lines[0])) for y in range(len(lines))]))

def get_score(lines, x, y):
    height = int(lines[y][x])

    l_dist = 0
    r_dist = 0
    u_dist = 0
    d_dist = 0

    # To left
    for xx in reversed(range(0, x)):
        l_dist += 1
        if lines[y][xx] >= height:
            break

    # To right
    for xx in range(x + 1, len(lines[0])):
        r_dist += 1
        if lines[y][xx] >= height:
            break

    # To top
    for yy in reversed(range(0, y)):
        u_dist += 1
        if lines[yy][x] >= height:
            break

    # To bottom
    for yy in range(y + 1, len(lines)):
        d_dist += 1
        if lines[yy][x] >= height:
            break

    print(x,y,"score",  l_dist, r_dist, u_dist, d_dist, "=",  l_dist* r_dist* u_dist* d_dist)

    return l_dist* r_dist* u_dist* d_dist
