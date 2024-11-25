def searchLeft(st, j, targ):

    for i in range(j - 1, -1, -1):

        if st[i] == targ or st[i] == "#":

            return True

        elif st[i] == "i":

            continue

        else:

            return False

def searchRight(st, j, targ):

    for i in range(j + 1, len(st)):

        if st[i] == targ or st[i] == "#":

            return True

        elif st[i] == "i":

            continue

        else:

            return False

def getVowels(wd):

    vowels = []
    curVowel = ""

    #We add a padding final word boundary so we don't miss
    #word-final vowels
    for c in wd + "#":

        if c in "aeiouõäöüyIÜU":

            curVowel += c

        else:

            if curVowel:

                vowels.append(curVowel)
                curVowel = ""

    return vowels

def getBackness(vowel):

    if vowel in "aouõyU":

        return "b"

    elif vowel in "eäöüIÜ":

        return "f"

    else:

        return "i"

def getBacknesses(vowels):

    backnesses = []

    for vow in vowels:

        backnesses.append("".join([getBackness(x) for x in vow]))

    return backnesses

s = []

with open("4. Inflected forms no length no clusters.txt", encoding = "utf-8") as f:

    s = f.read().split("\n")

entries = ["First line"]

backNeutral = {"#", "b", "bi", "i", "ib"}
frontNeutral = {"#", "f", "fi", "i", "if"}

for line in s:

    if line:

        for word in line.split(" "):

            v = getVowels(word)
            vB = ["#"] + getBacknesses(v) + ["#"]
            uniqueB = set(vB)

            if "i" in uniqueB and (uniqueB.issubset(backNeutral) or uniqueB.issubset(frontNeutral)):

                for ind in range(len(vB)):

                    if vB[ind] == "i" and (searchLeft(vB, ind, "b") or searchLeft(vB, ind, "f")) and (searchRight(vB, ind, "b") or searchRight(vB, ind, "f")):

                        entries.append(line)

                        break

            if entries[-1] == line:

                break

with open("5. Neutral words for study.txt", mode = "w", encoding = "utf-8") as f:

    f.write("\n".join(entries[1:]))
