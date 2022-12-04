lines = open("input.txt").readlines()
# lines = ["2-4,6-8"]

count = 0
for line in lines:
    elf_a, elf_b = line.strip().split(",")

    a_1, a_2 = [int(x) for x in elf_a.split("-")]
    b_1, b_2 = [int(x) for x in elf_b.split("-")]

    if a_1 <= b_1 and b_2 <= a_2:
        count += 1
    elif b_1 <= a_1 and a_2 <= b_2:
        count += 1

print(count)
