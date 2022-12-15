import re

def solve(lines):
    max_i = 4000000
    # max_i = 20
    max_j = 4000000
    # max_j = 20
    regex = re.compile(r'at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

    coords = []

    for line in lines:
        # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
        sx, sy, bx, by = [int(x) for x in regex.search(line).groups()]
        dist = abs(sx - bx) + abs(sy - by)
        coords.append(((sx, sy), (bx, by), dist))


    for ((sx, sy), _, dist) in coords:
        for i in range(dist + 1):
            j = dist + 1 - i
            if in_bound((sx + i, sy + j), max_i, max_j):
                find(coords,(sx + i, sy + j), max_i, max_j)
            if in_bound((sx - i, sy + j), max_i, max_j):
                find(coords,(sx - i, sy + j), max_i, max_j)
            if in_bound((sx - i, sy - j), max_i, max_j):
                find(coords,(sx - i, sy - j), max_i, max_j)
            if in_bound((sx + i, sy - j), max_i, max_j):
                find(coords,(sx + i, sy - j), max_i, max_j)

def find(coords, z, max_i, max_j):
    (i,j) = z
    if i < 0 or j < 0 or i > max_i or j > max_j:
        return

    found = False
    for ((sx, sy), (bx, by), dist) in coords:
        if cover((i, j), (sx, sy), dist):
            found = True
            break

    if not found:
        print("distress beacon at", i, j)
        print(i * 4000000 + j)
        exit(0)

def cover(coord, s, dist):
    (x, y) = coord
    (sx, sy) = s

    return abs(sx - x) + abs(sy - y) <= dist

def in_bound(coord, max_i, max_j):
    (i, j) = coord
    return i >= 0 and j >= 0 and i <= max_i and j <= max_j
