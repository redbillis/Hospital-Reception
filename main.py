from person import Person
from patient import Patient
from doctor import Doctor

run = True
while run:
    print("_______________________________________________________________________")
    name = input("Full Name: ")

    # Choosing patients condition.
    condition = ["Broken bone", "Heart Pain", "Stomach pain", "Kidney issues"]
    print("\nChoose on of the following conditions")
    print("Choose 0 for Broken bone")
    print("Choose 1 for Heart Pain")
    print("Choose 2 for Stomach pain")
    print("Choose 3 for Kidney issues\n")

    state_1 = True
    while state_1:
        choice = int(input("Please insert your choice between 0 and 3: "))
        if (choice >= 0 and choice <= 3):
            state_1 = False
        else:
            print("\nIncorrect input, try again!\n")

    # Check for insurance.
    print("\nDo you have insurance?")

    state_2 = True
    while state_2:
        insurance = input("Please enter 'y' for Yes or 'n' for No: ")

        if (insurance == 'y'):
            answer = True
            state_2 = False

        elif (insurance == 'n'):
            answer = False
            state_2 = False
            
        else:
            print("\nIncorrect input, try again!\n")

    patient = Patient(name, condition[choice], answer)

    # Printing patient's info.
    print("\n#############################")
    print("#### ------------------- ####")
    print("#### Patient information ####")
    print("#### ------------------- ####")
    print("-> Name: ", patient.name)
    print("-> Occupation: ", patient.get_occupation())
    print("-> Condition: ", patient.get_condition())
    print("-> Insurance: ", patient.is_insured())
    print("#############################\n")

    #############################################################################################

    occupation =["Arthrologist", "Cardiologist", "Gastroenterologist", "Urologist"]
    department =["Emergencies", "Cardiology", "Gastroenterology", "Urology"]

    James = Doctor("Dr.James", occupation[0], department[0])
    House = Doctor("Dr.House",occupation[1], department[1])
    Zivago = Doctor("Dr.Zivago",occupation[2], department[2])
    Karen = Doctor("Dr.Karen",occupation[3], department[3])

    docs_wl = [James, House, Zivago, Karen]

    #############################################################################################

    if (patient.is_insured() == True):

        if (patient.condition == "Broken bone"):
            if (docs_wl[0] == James):
                print(James.name, "will attend to your wounds.\n\n")
                James.assign_patient(patient)
            else:
                busy = James.is_with_patient()

        elif (patient.condition == "Heart Pain"):
            if (docs_wl[1] == House):
                print(House.name, "will be examining your heart.\n\n")
                House.assign_patient(patient)
            else:
                busy = House.is_with_patient()

        elif (patient.condition == "Stomach pain"):
            if (docs_wl[2] == Zivago):
                print(Zivago.name, "will take care of your pain.\n\n")
                Zivago.assign_patient(patient)
            else:
                busy = Zivago.is_with_patient()

        elif (patient.condition == "Kidney issues"):
            if (docs_wl[3] == Karen):
                print(Karen.name, "will be your doctor.\n\n")
                Karen.assign_patient(patient)
            else:
                busy = Karen.is_with_patient()
    else:
        print("\nPlease come back with an insurance number.\n")
        run = False