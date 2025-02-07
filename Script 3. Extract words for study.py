#2025-02-01
#This script takes in inflected forms
#It saves forms with the monophthong /i/

#A function which takes in a string of words and an index
#It returns a sliced substring of the input string:
#from just after the last vowel before the index, to the index
#If there is no vowel before the index, it returns the slice:
#from the start of the space-separated word to the index
def fromLastVowel(wd, ind):

    for i in range(ind - 1, -1, -1):

        if wd[i] in "iüyueöõoäaIUÜ ":

            return wd[i + 1:ind]

    return wd[:ind]

#A function which takes in a word and returns a modified version of it
#i is replaced with i1
#.ii is replaced with i3, even across intervening consonants
#Other ii is replaced with i2
def getQuantities(wd):

    wdOut = ""

    for i in range(len(wd)):

        #i
        if wd[i] == "i":

            #i not in a diphthong
            #First line excludes diphthongs ending in i
            #Second line excludes diphthongs starting in i
            #Third line excludes "diphthongs" starting in i,
            #where the second half is overlong
            if (i == 0 or wd[i - 1] not in "üyueöõoäaIUÜ") and\
            (i == len(wd) - 1 or wd[i + 1] not in "üyueöõoäaIUÜ") and\
            (i > len(wd) - 3 or\
             wd[i + 1] != "." or\
             (wd[i + 1] == "." and wd[i + 2] not in "üyueöõoäaIUÜ")):

                #Long or overlong i
                if wd[i+1:].startswith("i"):

                    #Overlong i
                    if "." in fromLastVowel(wd, i):

                        wdOut += "i3"

                    #Long i
                    else:

                        wdOut += "i2"

                #Short i
                else:

                    wdOut += "i1"

            #i in a diphthong
            else:

                wdOut += "i0"
                
        #Not i
        else:

            wdOut += wd[i]

    #ii consists of two i characters, but we want a single length mark
    wdOut = wdOut.replace("i3i1", "i3")
    wdOut = wdOut.replace("i2i1", "i2")
    wdOut = wdOut.replace("i2i0", "i0")
    wdOut = wdOut.replace("i3i0", "i0")

    return wdOut

s = []

with open("2. Inflected forms.txt", encoding = "utf-8") as f:

    s = f.read().split("\n")

output = []

for line in s:

    #We only care about words with /i/
    if "i" in line:

        #Get the length of each /i/
        line = getQuantities(line)

        #We only care about words with /i/ in Q1, Q2 or Q3
        #(/i/ in diphthongs is coded as Q0)
        if any([(x in line) for x in ["1", "2", "3"]]):

            output.append(line)

#Write to file
with open("3. Words for study.txt", mode = "w", encoding = "utf-8") as f:

    f.write("\n".join(output))
