s = []

with open("5. Neutral words for study.txt", encoding = "utf-8") as f:

    s = f.read().split("\n")

entries = []

for line in s:

    if line:

        if "'" not in line:

            entries.append(line)

with open("6. Study words (primary stress).txt", mode = "w", encoding = "utf-8") as f:

    f.write("\n".join(entries))
