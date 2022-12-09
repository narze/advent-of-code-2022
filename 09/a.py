def solve(lines):
    ax = 0
    ay = 0
    bx = 0
    by = 0

    b_marks = set()

    for line in lines:
        line = line.split(" ")
        direction = line[0]
        step = int(line[1])

        for _ in range(step):
            if direction == "U":
                ay += 1
            elif direction == "D":
                ay -= 1
            elif direction == "L":
                ax -= 1
            elif direction == "R":
                ax += 1

            # 3 steps
            if (abs(ax-bx) == 2 and abs(ay-by) == 1) or (abs(ax-bx) == 1 and abs(ay-by) == 2):
                # b follows a diagonally
                if ax > bx:
                    bx += 1
                elif ax < bx:
                    bx -= 1
                else:
                    raise Exception("Impossible")

                if ay > by:
                    by += 1
                elif ay < by:
                    by -= 1
                else:
                    raise Exception("Impossible")

            # 2 steps
            elif (abs(ax-bx) == 2 and abs(ay-by) == 0):
                # b follows a horizontally
                if ax > bx:
                    bx += 1
                elif ax < bx:
                    bx -= 1
                else:
                    raise Exception("Impossible")
            elif (abs(ax-bx) == 0 and abs(ay-by) == 2):
                # b follows a vertically
                if ay > by:
                    by += 1
                elif ay < by:
                    by -= 1

            b_marks.add((bx, by))

    print(len(b_marks))
