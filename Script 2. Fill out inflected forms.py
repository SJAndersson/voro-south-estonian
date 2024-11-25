s = []

with open("1. Audio, no alt, no dot.txt", encoding = "utf-8") as f:

    s = f.read().split("\n")

entries = []

for line in s:

    if line:

        hasSpace = bool(" " in line)
        hasComma = bool("," in line)
        headword = ""

        if hasSpace and not hasComma:

            headword = line[:line.index(" ")]

        elif hasComma and not hasSpace:

            headword = line[:line.index(",")]

        elif hasComma and hasSpace:

            headword = line[:min(line.index(" "), line.index(","))]

        else:

            continue

        if "1" in line:

            inflections = line[:line.index("1")]

            #Get rid of forms where the audio might contain multiple
            #sets of pronunciations
            if " e " not in inflections:
            
                stem = headword

                if "|" in line:

                    stem = headword[:headword.rfind("|")]

                inflections = inflections.replace("-", stem + "|")

                entries.append(inflections)           

        else:

            #This if statement removes I think in total 2 words which
            #are inflected but don't have an inflection class listed.
            if "-" not in line:

                entries.append(headword)       

with open("2. Inflected forms.txt", mode = "w", encoding = "utf-8") as f:

    f.write("\n".join(entries).replace(",", ""))
