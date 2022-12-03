rucksacks = open("input.txt").readlines()

# map a-z to 1-26
# map A-Z to 27-52
ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities = list(range(1, 53))
mapping = dict(zip(ch, priorities))

sum = 0

def grouper(n, iterable):
    args = [iter(iterable)] * n
    return zip(*args)

groups = grouper(3, rucksacks)

for group in groups:
    a, b, c = set([c for c in group[0].strip()]), set([c for c in group[1].strip()]), set([c for c in group[2].strip()])
    # print(a,b,c)

    for char in a:
        if char in b and char in c:
            print(char, mapping[char])
            sum += mapping[char]
            break

print("sum:", sum)
