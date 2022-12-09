def solve(lines):
    knots = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

    tail_marks = set()

    # limit = 100
    for x, line in enumerate(lines):
        # if x > limit:
        #     break
        line = line.split(" ")
        direction = line[0]
        step = int(line[1])

        for _ in range(step):
            if direction == "U":
                knots[0][1] += 1
            elif direction == "D":
                knots[0][1] -= 1
            elif direction == "L":
                knots[0][0] -= 1
            elif direction == "R":
                knots[0][0] += 1

            for i in range(1, len(knots)):
                # print(i)
                # 3 steps
                if (abs(knots[i-1][0]-knots[i][0]) > 2) or ( abs(knots[i-1][1]-knots[i][1]) > 2):
                    raise Exception("Impossible")

                if (abs(knots[i-1][0]-knots[i][0]) == 2 and abs(knots[i-1][1]-knots[i][1]) >= 1) or (abs(knots[i-1][0]-knots[i][0]) >= 1 and abs(knots[i-1][1]-knots[i][1]) == 2):
                    # b follows a diagonally
                    if knots[i-1][0] > knots[i][0]:
                        knots[i][0] += 1
                    elif knots[i-1][0] < knots[i][0]:
                        knots[i][0] -= 1
                    else:
                        raise Exception("Impossible")

                    if knots[i-1][1] > knots[i][1]:
                        knots[i][1] += 1
                    elif knots[i-1][1] < knots[i][1]:
                        knots[i][1] -= 1
                    else:
                        raise Exception("Impossible")

                # 2 steps
                elif (abs(knots[i-1][0]-knots[i][0]) == 2 and abs(knots[i-1][1]-knots[i][1]) == 0):
                    # b follows a horizontally
                    if knots[i-1][0] > knots[i][0]:
                        knots[i][0] += 1
                    elif knots[i-1][0] < knots[i][0]:
                        knots[i][0] -= 1
                    else:
                        raise Exception("Impossible")
                elif (abs(knots[i-1][0]-knots[i][0]) == 0 and abs(knots[i-1][1]-knots[i][1]) == 2):
                    # b follows a vertically
                    if knots[i-1][1] > knots[i][1]:
                        knots[i][1] += 1
                    elif knots[i-1][1] < knots[i][1]:
                        knots[i][1] -= 1
            print(knots)


            tail_marks.add((knots[-1][0], knots[-1][1]))

    print(len(tail_marks))
