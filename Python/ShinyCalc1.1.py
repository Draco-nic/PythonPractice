#improved probability calc
while True:
    Gen = int(float(input("Generation")))
    EN = int(float(input("Encounters")))

    if Gen <= 5:
        if Gen <= 4:
            SO = 1/8192
            EN = (EN)

            #Chance to find
            CTF = 1-(1-(1/8192))**(EN)
            #Chance to not find
            CNF = (1-(1/8192))**(EN)
        
        elif Gen == 5:
            SC = (input("Shiny Charm"))
            if SC == ("y"):
                SO = 3/8192
                EN = (EN)

                CTF = 1-(1-(3/8192))**(EN)
                CNF = (1-(3/8192))**(EN)
            else: 
                SC == ("n")
                SO = 1/8192
                EN = (EN)

                #Chance to find
                CTF = 1-(1-(1/8192))**(EN)
                #Chance to not find
                CNF = (1-(1/8192))**(EN)

    print(CTF)
    print(CNF)