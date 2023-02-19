def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            if line[start].isspace():
                start = start+1
            
            elif line[start].isdigit():
                end = start
                while end<len(line) and line[end].isdigit():
                    end = end+1
                words.append(line[start:end])
                start = end
            

            elif line[start].isalpha():
                end = start
                while end<len(line) and line[end].isalpha():
                    end = end+1
                words.append(line[start:end].lower())
                start = end   

            else:
                words.append(line[start])
                start = start + 1
    return words        

def countWords(words, Stopwords):
    dic = dict()
    for word in words:
        if word not in Stopwords:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] = dic.get(word) + 1
    return dic



def printTopMost(frequencies,n):
        sortedfreq = sorted(frequencies.items(), key=lambda x: -x[1])
        if n < len(sortedfreq):
            for i in range(n):
                print(sortedfreq[i][0].ljust(20) + str(sortedfreq[i][1]).rjust(5))
        else: 
            for i in range(len(sortedfreq)):
                print(sortedfreq[i][0].ljust(20) + str(sortedfreq[i][1]).rjust(5))

            
