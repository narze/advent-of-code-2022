lines = open("input.txt").readlines()

elves = [0]

for line in lines:
    if len(line.strip()) == 0:
        elves.append(0)
    else:
        elves[-1] += int(line.strip())

print(sum(sorted(elves)[-3:]))
