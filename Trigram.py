# Finalized on 21/3/2020 by Youssef Hassan

def ReadFile(FileName):
    FileInstance = open(FileName, "r", encoding="utf-8")
    All_Lines = FileInstance.read()
    FileInstance.close()
    return All_Lines


def countSentences(listWords):
    dictCount = {}
    for i in range(len(listWords) - 1):
        tempString = listWords[i] + " " + listWords[i + 1]
        if tempString in dictCount:
            dictCount[tempString] += 1
        else:
            dictCount[tempString] = 1
    for i in range(len(listWords) - 2):
        tempString = listWords[i] + " " + listWords[i + 1] + " " + listWords[i + 2]
        if tempString in dictCount:
            dictCount[tempString] += 1
        else:
            dictCount[tempString] = 1
    return dictCount


def computeProbabilities(WholeText, dictCount):
    dictProbabilities = {}
    for i in range(2, len(WholeText)):
        tempString = WholeText[i - 2] + " " + WholeText[i - 1]
        if tempString not in dictProbabilities:
            dictProbabilities[tempString] = {}

        if WholeText[i] not in dictProbabilities[tempString]:
            dictProbabilities[tempString][WholeText[i]] = float(dictCount[tempString + " " + WholeText[i]]) / dictCount[
                tempString]
    return dictProbabilities


def getNHighestProbs(sequenceProbabilities, n):
    listHighestProbs = []
    for sequence in sequenceProbabilities:
        if len(listHighestProbs) < n:
            tempSequence = sequence
            for i in range(len(listHighestProbs)):
                if sequenceProbabilities[tempSequence] > sequenceProbabilities[listHighestProbs[i]]:
                    sequence = listHighestProbs[i]
                    listHighestProbs[i] = tempSequence
                    tempSequence = sequence
            listHighestProbs.append(tempSequence)
        else:
            tempSequence = sequence
            for i in range(n):
                if sequenceProbabilities[tempSequence] > sequenceProbabilities[listHighestProbs[i]]:
                    sequence = listHighestProbs[i]
                    listHighestProbs[i] = tempSequence
                    tempSequence = sequence
    return listHighestProbs


searchedSequence = input("Enter two words to auto-fill the third:\n")

WholeText = ReadFile("Data.txt")
WholeText = WholeText.split()

dictCount = countSentences(WholeText)
dictProbabilities = computeProbabilities(WholeText, dictCount)

if len(searchedSequence.split()) != 2:
    print("Input error: incorrect number of words entered!")
if searchedSequence not in dictProbabilities:
    print("Word sequence doesn't exist in corpus!")
else:
    listHighestProbs = getNHighestProbs(dictProbabilities[searchedSequence], 7)
    for sequence in listHighestProbs:
        print("{}: {}".format(sequence, dictProbabilities[searchedSequence][sequence]))

