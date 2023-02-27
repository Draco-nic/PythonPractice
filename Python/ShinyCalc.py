#improved probability calc
while True:
    Gen = (input("Generation"))

    if Gen == '3' or '4' or '5':
        SO = 1/8192
        EN = (input("Encounters"))
        EN = int(float(EN))

        #Chance to find
        CTF = 1-(1-(1/8192))**(EN)
        #Chance to not find
        CNF = (1-(1/8192))**(EN)

    elif Gen == '6' or '7' or '8' or '9':
        SO = 1/4096
        EN = (input("Encounters"))
        EN = int(float(EN))

        #Chance to find
        CTF = 1-(1-(1/4096))**(EN)
        #Chance to not find
        CNF = (1-(1/4096))**(EN)

    print(CTF)
    print(CNF)