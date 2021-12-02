from person import Person
from patient import Patient

class Doctor(Person):
    def __init__(self, name, occupation, department):
        super().__init__(name, occupation)
        self.dpt = department
        self.current_patient = []

    def get_current_patient(self):
        print(self.current_patient[0].name)

    def assign_patient(self, patient):
        self.current_patient.append(patient)

    def is_with_patient(self):
        if (self.current_patient != None):
            print("Doctor is occupied with another patient!")
            return True         
        else:
            print("Free!")
            return False