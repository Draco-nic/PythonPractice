#improved probability calc
while True:
    Gen = int(float(input("Generation")))
    EN = int(float(input("Encounters")))

    if Gen <= 5:
        SO = 1/8192
        EN = (EN)

        #Chance to find
        CTF = 1-(1-(1/8192))**(EN)
        #Chance to not find
        CNF = (1-(1/8192))**(EN)

    elif Gen >= 6:
        SO = 1/4096
        EN = (EN)

        #Chance to find
        CTF = 1-(1-(1/4096))**(EN)
        #Chance to not find
        CNF = (1-(1/4096))**(EN)

    print(CTF)
    print(CNF)