
syllables = ["V","VC","CV","CVC","VCC","CVCC","C"]


c = "rtypğsdfghjklşzcvbnmçRTYPĞSDFGHJKLŞZCVBNMÇ"
v = "euıoüaiöEUIOÜAİÖ"


text_input = input("text: ")

text_input_arr = text_input.split(" ")
arr = [[] for _ in range(len(text_input_arr))]

def syllableTransciber(textInput):
    for x in range(len(textInput)):
        arr[x].append(textInput[x])
        syllableText = ""
        for y in textInput[x]:
            if y in c:
                syllableText = syllableText + "C"
            elif y in v:
                syllableText = syllableText + "V"
        arr[x].append(syllableText)

syllableTransciber(text_input_arr)    

hecearr=[]
isimarr=[]
results = []
textResult = ""
def heceleyici(text_arr):
    x = 0
    for sozcuk in text_arr:
        hecearr=[]
        isimarr=[]
        for k in range(4,0,-1):
            if sozcuk[1][-k:] in syllables:
                hecearr.append(sozcuk[1][-k:])
                isimarr.append(sozcuk[0][-k:])
                x = k
                break
        if len(sozcuk[1]) >= 4:
            while x < len(sozcuk[1]):
                for k in range(4,0,-1):
                    if sozcuk[1][-x-k:-x] in syllables:
                        hecearr.append("-")
                        isimarr.append("-")
                        hecearr.append(sozcuk[1][-x-k:-x])
                        isimarr.append(sozcuk[0][-x-k:-x])
                        x = abs(-x-k)
                        break            
        hecearr.reverse()
        isimarr.reverse()
        if(hecearr[0] == "C"):
            hecearr[0] = hecearr[0]+hecearr[2]
            isimarr[0] = isimarr[0]+isimarr[2]
            hecearr.pop(1)
            isimarr.pop(1)
            hecearr.pop(1)
            isimarr.pop(1)
        x = 0
        results.append(isimarr)

heceleyici(arr)
for i in results:
        for j in i:
            textResult = textResult+j
        textResult = textResult + " "
print(textResult)