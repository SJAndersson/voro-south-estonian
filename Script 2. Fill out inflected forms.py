#2025-02-01
#This reads in forms with audio
#It inflects the forms based on the template in the dictionary
#For example:
#ahnõq|kaal,-kaala,-.kaala
#becomes
#ahnõqkaal,ahnõqkaala,ahnõq.kaala

s = []

with open("1. Audio.txt", encoding = "utf-8") as f:

    s = f.read().split("\n")

#Only two lines don't have a space, I'm getting rid of them
s = [line for line in s if " " in line]

#The word/inflections is everything before the first space
s = [line[:line.index(" ")] for line in s]

output = []
stem = 0

for line in s:

    #There are four categories of lines based on a 2x2:
    #Is there a pipe symbol?
    #Is there a dash?

    #No, no:
    #aaḿ,aami,.aami
    #Processing needed: NONE

    #No, yes:
    #aadoḿ,-i,-it
    #Processing needed: fill in first form as stem

    #Yes, no:
    #aloma|nõ
    #Processing needed: get rid of pipe

    #Yes, yes:
    #ahnõq|kaal,-kaala,-.kaala
    #Processing needed: fill in stem from first form, get rid of pipe

    if "|" in line and "-" not in line:

        #e.g.: aloma|nõ
        output.append(line.replace("|", ""))

    elif "-" in line:

        #A small number of prefixes are listed in the dictionary, e.g.:
        #keedi-
        #We do not keep these since they're not whole words
        if "," not in line:

            continue

        stem = line[:line.index(",")]

        if "|" in stem:

            #e.g.: ahnõq|kaal,-kaala,-.kaala
            stem = stem[:stem.rfind("|")]

        #e.g.:
        #aadoḿ,-i,-it
        #ahnõq|kaal,-kaala,-.kaala
        output.append(line.replace("-", stem).replace("|", ""))

    else:

        #e.g.: aaḿ,aami,.aami
        output.append(line)

#Write to file
with open("2. Inflected forms.txt", mode = "w", encoding = "utf-8") as f:

    f.write("\n".join(output).replace(",", " "))
