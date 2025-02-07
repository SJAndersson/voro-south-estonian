#2025-02-01
#This script reads the full dictionary as input
#It saves all words which have audio files

s = []

with open("Võro Instituut dictionary.txt", encoding = "utf-8") as f:

    #'kuular' at the end of a line means there is an audio file
    s = [line for line in f.read().split("\n") if line.endswith("kuular")]

output = "\n".join(s)

#Getting rid of numbers
for i in range(10):

    output = output.replace(str(i), "")

#Getting rid of various special characters/formatting
output = output.replace("*", "")
output = output.replace("†", "")
output = output.replace("I", "")
output = output.replace(":", "")
output = output.replace(" m ", " ")
output = output.replace(" ,", ",")

#Formatting so the first space is always where the word/inflections end
output = output.replace(", ", ",")

#Simplifying transcriptions, especially of di-/trigraphs
output = output.replace("i̬", "I")
output = output.replace("ü̬", "Ü")
output = output.replace("u̬", "U")

output = output.replace("ds", "z")
output = output.replace("tts", "cc")
output = output.replace("ts", "c")

output = output.replace("dś", "ź")
#output = output.replace("ttś", "cc")
output = output.replace("tś", "ć")
#Long palatalised /ts/ is unattested

#Write to file
with open("1. Audio.txt", mode = "w", encoding = "utf-8") as f:

    f.write(output)
