#This function returns true if there's a cluster where the second
#element is p, t, k. Geminates are ignored. There appears to be no
#palatalized b', nor any clusters with glottal stop (q), so these
#are ignored by the function.
def hasCluster(st):

    for i in range(1, len(st)):

        if st[i] in "ptkṕťḱ" and st[i - 1] in "ptkbdgcvshmnlrṕťḱďǵćv́śḣḿńľŕ" and not st[i - 1] == st[i]:

            return True

    return False

s = []

with open("3. Inflected forms no length.txt", encoding = "utf-8") as f:

    s = f.read().split("\n")

entries = []

for line in s:

    if line:

        if not hasCluster(line):

            entries.append(line)

with open("4. Inflected forms no length no clusters.txt", mode = "w", encoding = "utf-8") as f:

    f.write("\n".join(entries))
