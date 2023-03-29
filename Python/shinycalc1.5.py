from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Shiny Probability Calculator")
root.geometry("350x400")
root.resizable(width=False, height=False)

root.iconbitmap(r'C:\\Users\\dtdm9\\Downloads\\shiny-charm.ico')

def shinycalc():
     while(True):
        if menu.get() and menu2.get() and encounters_entry.get():
            generation = (menu.get())
            method = (menu2.get())
            encounters = int(float(encounters_entry.get()))
            sc = (sc1.get())

            def shinyodds():
                    ctf = 1-(1-(((so)+(sco))/8192))**(encounters)
                    global ctfp
                    ctfp = f"{ctf:.2%}" 

            def gen1():
                    global so
                    global sco
                    so = 1
                    sco = 0
                    shinyodds()

            def gen2():
                global so
                global sco
                if method == "Random Encounters":
                    so = 1
                    sco = 0
                elif method == "Masuda Method":
                    so = 5
                    sco = 0
                shinyodds()
            
            def gen3():
                global so
                global sco
                if generation == 5:
                    if method == "Random Encounters":
                        if sc == "yes":
                            so = 1
                            sco = 2
                        elif sc == "no":
                            so = 1
                            sco = 0
                    elif method == "Masuda Method":
                        if sc == "yes":
                            so = 6
                            sco = 2
                        elif sc == "no":
                            so = 6
                            sco = 0
                elif generation >= 6:
                    if method == "Random Encounters":
                        if sc == "yes":
                            so = 2
                            sco = 4
                        elif sc == "no":
                            so = 2
                            sco = 0
                    elif method == "Masuda Method":
                        if sc == "yes":
                            so = 6
                            sco = 4
                        elif sc == "no":
                            so = 6
                            sco = 0
                shinyodds()

            if generation <= 3:
                gen1()
            elif generation == 4:
                gen2()
            elif generation >= 5:
                gen3()
                
            odds_label.config(text = f"Odds of finding a shiny Pokemon: {ctfp}", font=("Ariel", 10))
            return
        else:
            odds_label.config(text="Error, missing information")


my_label_frame = LabelFrame(root, text="Shiny Calculator")
my_label_frame.pack(pady=30)
my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

# Define labels and entry boxes
def shinycharm():
     gen = menu.get()
     if (gen >= 5):
          sc_entry['state'] = NORMAL
          sc_entry.config(text = "Shiny Charm")
     else:
          sc_entry['state'] = DISABLED
          sc_entry.config(text = "Shiny Charm")
        
menu = IntVar()
menu.set("Select Generation")
menu_options = [2, 3, 4, 5, 6, 7, 8, 9]

menu2 = StringVar(value="Select Method")
menu2.set("Select Method")
generation_label = Label(my_frame, text="Generation")
generation_entry = OptionMenu(my_frame, menu, "Select Generation", *(menu_options), command=lambda _: shinycharm())

method_label = Label(my_frame, text="Method")
method_entry = OptionMenu(my_frame, menu2, "Select Method", "Random Encounters", "Masuda Method")

encounters_label = Label(my_frame, text="Encounters")
encounters_entry = Entry(my_frame, font=("Ariel", 10))

sc_label = Label(my_frame, text="Shiny Charm")
sc1 = StringVar(value= "no")
sc_entry = Checkbutton(my_frame, text="Shiny Charm", onvalue= "yes", offvalue= "no", variable= sc1)

# Put labels and entry boxes on screen
generation_label.grid(row=0, column=0)
generation_entry.grid(row=0, column=1)

method_label.grid(row=1, column=0)
method_entry.grid(row=1, column=1, pady=20)

encounters_label.grid(row=2, column=0)
encounters_entry.grid(row=2, column=1)

sc_label.grid(row=3, column=0)
sc_entry.grid(row=3, column=1, pady=20)
#sc_entry.config(state=DISABLED)

my_button = Button(my_label_frame, text="Calculate Odds", command=shinycalc)
my_button.pack(pady=20)

# Output label
odds_label = Label(root, text="", font=("Ariel", 18))
odds_label.pack(pady=20)

root.mainloop()