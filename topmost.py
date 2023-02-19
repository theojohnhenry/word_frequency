import wordfreq
import sys
import urllib.request

stopwordList = []
textList = []
textPath = str(sys.argv[2])

stopwordsFile = open(sys.argv[1], encoding="utf-8")
for lines in stopwordsFile:
    lines = lines.strip("\n")
    stopwordList.append(lines)
stopwordsFile.close()

if ("http://" in textPath) or ("https://" in textPath):
    response = urllib.request.urlopen(textPath)
    textList = response.read().decode("utf8").splitlines()

else:
    textFile = open(textPath, encoding="utf-8")
    for lines in textFile:
        textList.append(lines)
    textFile.close()
def main():

    textTokenized = wordfreq.tokenize(textList)
    textCounted = wordfreq.countWords(textTokenized, stopwordList)
    wordfreq.printTopMost(textCounted, int(sys.argv[3]))

main()

