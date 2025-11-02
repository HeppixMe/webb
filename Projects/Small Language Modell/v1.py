import random



text = open("C:/Users/leopold/Documents/GPT/text.txt", "r")
textList = []
for i in text:
    i = i.removesuffix("\n").split(" ")
    for x in i:
        textList.append(x)

Memory = {}

for i in range(len(textList)):
    if textList[i] in Memory and not i == len(textList)-1:
        Memory[textList[i]].append(textList[i+1])
    elif not textList[i] in Memory and not i == len(textList)-1:
        Memory[textList[i]] = [textList[i+1]]

        
lastWord = textList[random.randint(0,len(textList)-2)]
out = lastWord + " "
running = int(input("Wie viele Sätze? >> "))
while running > 0:
    while lastWord == textList[len(textList)-1]:
        lastWord = textList[random.randint(0,len(textList)-2)] 
    word = Memory[lastWord][random.randint(0,len(Memory[lastWord])-1)]
    out += word + " "
    lastWord = word
    if out.endswith(". ") or out.endswith("! ") or out.endswith("? "): 
        running -= 1

print(out)
s = input("\n\nSpeichern? >> ").lower()
if not s == ""  and not s == "nein" and not s == "n" and not s == "no":
    outputs = open("C:/Users/leopold/Documents/GPT/outputs.txt", "a")
    outputs.write("\n\n"+out)
    outputs.close()
    print("gespeichert!")
else: print("nicht gespeichert!")
text.close()