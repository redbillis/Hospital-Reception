from person import Person

class Patient(Person):
    def __init__(self, name, condition, insurance=True):
        super().__init__(name, occupation="Unknown!")
        self.condition = condition
        self.insured = insurance

    # Return the medical condition of this patient as a string.
    def get_condition(self):
        return self.condition

    def is_insured(self):
        if (self.insured == True):
            return True
        else:
            return False