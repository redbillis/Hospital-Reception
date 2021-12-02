from person import Person
from patient import Patient
from doctor import Doctor

class Hospital:
    def __init__(self):
        self.docs_wl = []   # The doctor waiting area.
        self.patients = []  # The patient waiting room.

    def on_doctor_called(self, doc):
        # This method adds a doctor to the list of available doctors or removes one when with patient.
        if (doc.is_with_patient() != True): 
            self.docs_wl.append(doc)
        else:
            self.docs_wl.remove(doc)

    def on_patient_visit(self, patient):
        # This method adds patients to the waiting room.
        self.patients.append(patient)

        # This method removes the patient in the list from the waiting room.
        self.patients.remove(patient)