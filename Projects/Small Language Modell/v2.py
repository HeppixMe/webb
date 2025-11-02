import random

deutsche_pronomen = [
    # Personalpronomen
    "ich", "du", "er", "sie", "es", "wir", "ihr", "sie", "meiner", "deiner", "seiner", "ihrer", "unser", "euer", "mir", "dir", "ihm", "uns", "euch", "ihnen", "mich", "dich", "ihn",

    # Reflexivpronomen (inkl. sich)
    "sich",

    # Possessivpronomen (Grundformen)
    "mein", "dein", "sein", "ihr", "unser", "euer", "meine", "deine", "seine", "ihre", "unsere", "eure", "meinem", "deinem", "seinem", "ihrem", "unserem", "eurem",

    # Demonstrativpronomen
    "dieser", "diese", "dieses", "diesem", "diesen", "dessen", "derer", "derselbe", "derselben", "derselben", "derselben", "derjenige", "dasselbe", "selber", "selbst", "jener", "jene", "jenes",

    # Relativpronomen
    "der", "die", "das", "dem", "den", "denen", "wessen", "welcher", "welche", "welches",

    # Interrogativpronomen
    "wer", "was", "wem", "wen",

    # Indefinitpronomen
    "man", "jemand", "jemandes", "jemandem", "jemanden", "niemand", "niemandes", "niemandem", "niemanden",
    "etwas", "nichts", "alle", "einer", "eine", "eines", "einem", "einen", "keiner", "keine", "keines", "keinem", "keinen",
    "irgendwer", "irgendjemand", "irgendetwas", "irgendwen", "irgendwem", "irgendwas", "irgendwen"
]

# Optional: Duplikate entfernen und sortieren
deutsche_pronomen = sorted(list(set(deutsche_pronomen)))

text = open("C:/Users/leopold/Documents/GPT/text.txt", "r")
textList = []
for i in text:
    i = i.removesuffix("\n").split(" ")
    for x in range(len(i)):
        if x in deutsche_pronomen:
            textList.append(i[x]+" " +i[x+1])
            x+=1
        else:
            textList.append(i[x])

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
s = "" #input("\n\nSpeichern? >> ").lower()
if not s == ""  and not s == "nein" and not s == "n" and not s == "no":
    outputs = open("C:/Users/leopold/Documents/GPT/outputs.txt", "a")
    outputs.write("\n\n"+out)
    outputs.close()
    print("gespeichert!")
else: print("nicht gespeichert!")
text.close()