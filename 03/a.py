rucksacks = open("input.txt").readlines()

# map a-z to 1-26
# map A-Z to 27-52
ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities = list(range(1, 53))
mapping = dict(zip(ch, priorities))

sum = 0

for sack in rucksacks:
    sack = sack.strip()

    half = int(len(sack) / 2)

    a, b = set([c for c in sack[:half]]), set([c for c in sack[half:]])

    for char in a:
        if char in b:
            print(char, mapping[char])
            sum += mapping[char]
            break
    # print(a,b)

print("sum:", sum)
