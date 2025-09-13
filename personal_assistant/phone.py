from field import Field


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must have 10 digits.")
        super().__init__(value)