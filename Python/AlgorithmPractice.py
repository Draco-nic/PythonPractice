welcome_prompt = "Welcome, what would you like to do?\n - For patient list, press 1\n - For new diagnosis, press 2\n - Quit, press q\n"
name_prompt = "What is the patients name and diagnoses?"
appearance_prompt = "What is the patients appearance?\n  1: Normal appearance\n  2: Irritable and lethargic\n"
eye_prompt = "How do that patients eyes look?\n  1: Normal or slightly sunken in\n  2: Very sunken in"
skin_prompt = "How quickly does the patient's skin return to normal after pinch?\n  1: Quickly\n  2: Slowly\n"
severe_dehydration = "Severe Dehydration"
some_dehydration = "Some Dehydration"
no_dehydration = "No Dehydration"
error_message = "Could not save patient data due to invalid input"

patients_and_diagnoses = [
    "Mike: Sever dehydration",
    "John: No dehydration",
    "Emily: Some dehydration"
]

def list_patients():
    for patient in patients_and_diagnoses:
        print(patient)

def save_new_diagnosis(name, diagnosis):
    if name == "" or diagnosis == "":
        print(error_message)
        return
    final_diagnosis = name + ": " + diagnosis
    patients_and_diagnoses.append(final_diagnosis)
    print("Final diagnosis:", final_diagnosis,"\n")

def assess_skin(skin):
    if skin == "1":
        return some_dehydration
    elif skin == "2":
        return severe_dehydration
    else:
        return ""

def assess_eyes(eyes):
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration
    else:
        return ""

def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin(skin)
    else:
        return ""

def start_new_diagnosis():
    name = input(name_prompt)
    diagnosis = assess_appearance()
    save_new_diagnosis(name, diagnosis)

def main():
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            return

main()

