def solve(lines):
    m = list(map(lambda a: [ch for ch in a], lines))

    # Find S
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'S':
                start = (i, j)
                break

    # Find E
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'E':
                end = (i, j)
                break

    # change a-z to score 1-26
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'E':
                m[i][j] = 26
            elif m[i][j] == 'S':
                m[i][j] = 1
            elif m[i][j].isalpha():
                m[i][j] = ord(m[i][j]) - ord('a') + 1

    starts = []
    min_starts = []

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                starts.append((i, j))

    for start in starts:
        q = [(start, [start])]

        visited = {}
        visited[start] = True
        paths = []
        print(start, end)

        while q:
            (i, j), path = q.pop(0)
            # print(len(path), (i,j))

            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new = (i + d[0], j + d[1])

                if new in path:
                    continue
                if new[0] < 0 or new[0] >= len(m) or new[1] < 0 or new[1] >= len(m[0]):
                    continue
                if m[new[0]][new[1]] - m[i][j] > 1:
                    continue

                if new == end:
                    paths.append(path + [new])
                    continue

                if new in visited:
                    continue
                visited[new] = True

                q.append((new, path + [new]))

        if paths:
            min_starts.append( min([len(p)-1 for p in paths]))

    print(min(min_starts))

