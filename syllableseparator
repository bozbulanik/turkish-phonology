
syllables = ["V","VC","CV","CVC","VCC","CVCC","C"]
c = "rtypğsdfghjklşzcvbnmçRTYPĞSDFGHJKLŞZCVBNMÇ"
v = "euıoüaiöEUIOÜAİÖ"

text = input("text: ")

def syllableSeparator(textInput):
    textInputArray = textInput.split(" ")
    dataArray = [[] for _ in range(len(textInputArray))]
    for x in range(len(textInputArray)):
        dataArray[x].append(textInputArray[x])
        syllableText = ""
        for y in textInputArray[x]:
            if y in c:
                syllableText = syllableText + "C"
            elif y in v:
                syllableText = syllableText + "V"
        dataArray[x].append(syllableText)

    outputArray = []
    textResult = ""
    x = 0
    for sozcuk in dataArray:
        syllableArray=[]
        textArray=[]
        for k in range(4,0,-1):
            if sozcuk[1][-k:] in syllables:
                syllableArray.append(sozcuk[1][-k:])
                textArray.append(sozcuk[0][-k:])
                x = k
                break
        if len(sozcuk[1]) >= 4:
            while x < len(sozcuk[1]):
                for k in range(4,0,-1):
                    if sozcuk[1][-x-k:-x] in syllables:
                        syllableArray.append("-")
                        textArray.append("-")
                        syllableArray.append(sozcuk[1][-x-k:-x])
                        textArray.append(sozcuk[0][-x-k:-x])
                        x = abs(-x-k)
                        break            
        syllableArray.reverse()
        textArray.reverse()
        if(syllableArray[0] == "C"):
            syllableArray[0] = syllableArray[0]+syllableArray[2]
            textArray[0] = textArray[0]+textArray[2]
            syllableArray.pop(1)
            textArray.pop(1)
            syllableArray.pop(1)
            textArray.pop(1)
        x = 0
        outputArray.append(textArray)

    for i in outputArray:
            for j in i:
                textResult = textResult+j
            textResult = textResult + " "
    print(textResult)

syllableSeparator(text)
