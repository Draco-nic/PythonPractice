gen_prompt = "What generation are you playing?\n 1: Gen 2-3\n 2: Gen 4\n 3: Gen 5\n 4: Gen 6-9\n"
method_prompt = "What method are you using to hunt?\n 1: Random Encounters\n 2: Masuda Method\n"
encounter_prompt = "How many encounters have you had?\n"
sc_prompt = "Do you have the shiny charm?\n Y\n N\n"
generation = int(float(input(gen_prompt)))
encounters = int(float(input(encounter_prompt)))

def shinyodds():
        ctf = 1-(1-(so/8192))**(encounters)
        cnf = (1-(so/8192))**(encounters)
        ctfp = f"{ctf:.2%}"
        cnfp = f"{cnf:.2%}"
        print(ctfp)
        print(cnfp)

def shinycalc():
    while(True):
        if generation == 1:
            gen1()
        elif generation == 2:
            gen2()
        elif generation >= 3:
            gen3()
        return
    
       
def gen1():
    global so 
    so = 1
    shinyodds()

def gen2():
    global so
    method = input(method_prompt)
    if method == "1":
        so = 1
    elif method == "2":
        so = 5
    shinyodds()
       
def gen3():
    global so
    method = input(method_prompt)
    sc = input(sc_prompt)
    if generation >= 4:
        if method == "1":
            if sc == "Y":
                so = 6
            elif sc == "N":
                so = 2
        elif method == "2":
            if sc == "Y":
                so = 16
            elif sc == "N":
                so = 12
    elif generation == 3:
        if method == "1":
            if sc == "Y":
                so = 3
            elif sc == "N":
                so = 1
        elif method == "2":
            if sc == "Y":
                so = 8
            elif sc == "N":
                so = 6
    shinyodds()
            
shinycalc()