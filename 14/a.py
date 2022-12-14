# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9

def solve(lines):
    paths = []
    for line in lines:
        dots = []
        for dot in line.split(" -> "):
            x,y = dot.split(",")
            dots.append((int(x),int(y)))
        paths.append(dots)

    # Find upper & lower bounds
    min_x = min([dot[0] for path in paths for dot in path])
    max_x = max([dot[0] for path in paths for dot in path])
    min_y = 0
    max_y = max([dot[1] for path in paths for dot in path])

    print(min_x, max_x, min_y, max_y)

    rows = []
    for i in range(max_y - min_y + 1):
        cols = []
        for j in range(max_x - min_x + 1):
            cols.append(".")
        rows.append(cols)

    rows = draw(rows, paths, min_x)

    count = 0
    while(True):
        (rows, overflow) = add_sand(rows, (500,0), min_x)
        print_map(rows)
        if overflow:
            break
        else:
            count += 1

    print_map(rows)
    print(count)

def add_sand(rows, sand, x_offset):
    x, y = sand
    x -= x_offset

    while(True):
        if y >= len(rows):
            break
        if x < 0 or x >= len(rows[0]):
            break

        down = y+1 >= len(rows) or rows[y+1][x] == "."
        down_left = y+1 >= len(rows) or x-1 < 0 or rows[y+1][x-1] == "."
        down_right = y+1 >= len(rows) or x + 1 >= len(rows[0]) or rows[y+1][x+1] == "."

        if down: # Drop
            y += 1
        elif down_left: # Drop down left
            y += 1
            x -= 1
        elif down_right:
            y += 1
            x += 1
        else: # Stop
            rows[y][x] = "o"
            return (rows, False)

    return (rows, True)

def print_map(rows):
    for i, row in enumerate(rows):
        print("".join(row))

def draw(rows, paths, x_offset):
    for path in paths:
        print(f"draw {path}")
        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i+1]
            x1 -= x_offset
            x2 -= x_offset
            if x1 == x2:
                if y1 > y2:
                    y1, y2 = y2, y1

                for y in range(y1, y2 + 1):
                    rows[y][x1] = "#"
            else:
                if x1 > x2:
                    x1, x2 = x2, x1
                for x in range(x1, x2 + 1):
                    print(y1,x)
                    rows[y1][x] = "#"

    return rows
