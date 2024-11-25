d = {}

d["d"] = "ď"
d["g"] = "ǵ"
d["v"] = "v́"
d["s"] = "ś"
d["h"] = "ḣ"
d["m"] = "ḿ"
d["n"] = "ń"
d["l"] = "ľ"
d["r"] = "ŕ"

def removeDuplicates(st):

    for c in "".join(list(set(st))):
        #<c> is used here for /ts/
        if c not in "bpdtgckIÜU":

            st = st.replace(c * 2, c)
            st = st.replace(f"{c}){c}", c)
            st = st.replace(f"{c}({c}", c)

            if c in d.keys():

                st = st.replace(c + d[c], c)

    return st

s = []

with open("2. Inflected forms.txt", encoding = "utf-8") as f:

    s = f.read().replace("|", "").split("\n")

entries = []

for line in s:

    if line:

        if line == removeDuplicates(line):

            entries.append(line)

with open("3. Inflected forms no length.txt", mode = "w", encoding = "utf-8") as f:

    f.write("\n".join(entries))
