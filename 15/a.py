import re

def solve(lines):
    y = 2000000

    regex = re.compile(r'at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

    coords = []

    for line in lines:
        # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
        sx, sy, bx, by = [int(x) for x in regex.search(line).groups()]
        dist = abs(sx - bx) + abs(sy - by)
        coords.append(((sx, sy), (bx, by), dist))

    ans = set()
    for ((sx, sy), (_, _), dist) in coords:
        x = sx

        c = 0
        while True:
            if cover((x+c, y), (sx, sy), dist):

                ans.add((x + c, y))
                ans.add((x - c, y))
                c += 1
            else:
                break

    for ((sx, sy), (bx, by), dist) in coords:
        ans.discard((bx, by))

    print(len(ans))


def cover(coord, s, dist):
    (x, y) = coord
    (sx, sy) = s

    return abs(sx - x) + abs(sy - y) <= dist

