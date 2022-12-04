lines = open("input.txt").readlines()

count = 0
for line in lines:
    elf_a, elf_b = line.strip().split(",")

    a_1, a_2 = [int(x) for x in elf_a.split("-")]
    b_1, b_2 = [int(x) for x in elf_b.split("-")]

    if not (a_2 < b_1 or b_2 < a_1):
        count += 1

print(count)
