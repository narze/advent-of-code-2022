import functools

def solve(lines):
    entries = []
    for i, line in enumerate(lines):
        if i % 7 == 0:
            entries.append({"inspects": 0})

        if i % 7 == 1:
            entries[-1]["items"] = [int(x) for x in line.split(": ")[-1].split(", ")]

        if i % 7 == 2:
            entries[-1]["op"] = line.split("= old ")[-1]

        if i % 7 == 3:
            entries[-1]["exp"] = int(line.split("divisible by ")[-1])

        if i % 7 == 4:
            entries[-1]["true"] = int(line.split("monkey ")[-1])

        if i % 7 == 5:
            entries[-1]["false"] = int(line.split("monkey ")[-1])

    print(entries)

    for nth in range(20):
        for i, entry in enumerate(entries):
            new_items = []
            for old in entry["items"]:
                new_level = eval(f"{old} {entry['op']}") // 3

                if new_level % entry["exp"] == 0:
                    entries[entry["true"]]["items"].append(new_level)
                else:
                    entries[entry["false"]]["items"].append(new_level)

                entries[i]["inspects"] += 1
                entries[i]["items"] = []

    print(entries)
    print(functools.reduce(lambda a,b: a*b,[x["inspects"] for x in sorted(entries, key=lambda x: x["inspects"])[-2:]]))

