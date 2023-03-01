#Gen = Generation
#EN = Total Encounters
#MD = Method of Encounters
#CTF = The chance to have found a shiny in the given number of encounters
#CNF = The chance to not have found a shiny in the given number of encounters
#SC = Shiny Charm
#mm = Masuda Method
#re = Random Encounters and Soft Resets
while True:
    Gen = int(float(input("Generation")))
    EN = int(float(input("Encounters")))
    MD = str(input("Method"))
    if Gen <= 5:
        if Gen <= 4:
            if MD == ("mm"):
                SO = "5/8192"

                CTF = 1-(1-(5/8192))**(EN)
                CNF = (1-(5/8192))**(EN)
            elif MD == ("re"):
                SO = "1/8192"
                
                CTF = 1-(1-(1/8192))**(EN)
                CNF = (1-(1/8192))**(EN)
        
        elif Gen == 5:
            SC = (input("Shiny Charm"))
            if SC == ("y"):
                if MD == ("mm"):
                    SO = "8/8192"
                    
                    CTF = 1-(1-(8/8192))**(EN)
                    CNF = (1-(8/8192))**(EN)

                elif MD == ("re"):
                    SO = "3/8192"
                    
                    CTF = 1-(1-(3/8192))**(EN)
                    CNF = (1-(3/8192))**(EN)
            elif SC == ("n"):
                if MD == ("mm"):
                    SO = "5/8192"
                    
                    CTF = 1-(1-(5/8192))**(EN)
                    CNF = (1-(5/8192))**(EN)
                elif MD ==("re"):
                    SO = "1/8192"
                    
                    CTF = 1-(1-(1/8192))**(EN)
                    CNF = (1-(1/8192))**(EN)
    elif Gen >= 6:
        SC = (input("Shiny Charm"))
        if SC == ("y"):
            if MD == ("mm"):
                SO = "8/4096"
            
                CTF = 1-(1-(8/4096))**(EN)
                CNF = (1-(8/4096))**(EN)
            elif MD == ("re"):
                SO = "3/4096"

                CTF = 1-(1-(3/4096))**(EN)
                CNF = (1-(3/4096))**(EN)
        elif SC == ("n"):
                if MD == ("mm"):
                    SO = "6/4096"
                    
                    CTF = 1-(1-(6/4096))**(EN)
                    CNF = (1-(6/4096))**(EN)
                elif MD == ("re"):


                    SO = "1/4096"

                    CTF = 1-(1-(1/4096))**(EN)
                    CNF = (1-(1/4096))**(EN)

    CTFP = f"{CTF:.2%}"
    CNFP = f"{CNF:.2%}"
    print(SO)
    print(CTFP)
    print(CNFP)