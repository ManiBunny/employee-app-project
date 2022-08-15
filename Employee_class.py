

class Employee(object):
    """class Employee initializes the object with a name, id, age, phone.
     for comport our default variables are zeros for integers and  ~ for strings."""
    id = 0
    name = "~"
    phone = 0
    age = 0

    def __init__(self, name, id, age, phone):
        self.name = name
        self.id = id
        self.age = age
        self.phone = phone

