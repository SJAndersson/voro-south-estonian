s = []

with open("Võro Instituut dictionary.txt", encoding = "utf-8") as f:

    s = f.read().split("\n")

entries = []

for line in s:

    if line:

        #A . marks the following vowel as overlong. You may wish to
        #include such words, but remember that this interacts with
        #syllable structure, and unless you know the ways in which
        #consonant and vowel length interact, it may be hard to
        #accurately predict even from orthographies with a . which
        #vowels are short/long/overlong.
        if line.endswith("kuular") and "=" not in line and ">" not in line and "<" not in line and "." not in line:

            entries.append(line)

output = "\n".join(entries)

for i in range(0, 10):

    output = output.replace(str(i), "1")

output = output.replace("*", "")
output = output.replace("†", "")
output = output.replace("I", "")
output = output.replace(":", "")
output = output.replace(" m ", " ")
output = output.replace(" ,", ",")

output = output.replace("i̬", "I")
output = output.replace("ü̬", "Ü")
output = output.replace("u̬", "U")

output = output.replace("ds", "z")
output = output.replace("ts", "c")
output = output.replace("tts", "cc")

output = output.replace("dś", "ź")
output = output.replace("tś", "ć")
#output = output.replace("ttś", "cc")
#Long palatalized /ts/ is unattested

with open("1. Audio, no alt, no dot.txt", mode = "w", encoding = "utf-8") as f:

    f.write(output)
