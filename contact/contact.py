

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def print_data(self):
        print("Nombre: {}, Telefono: {}, Email: {}\n\n".format(self.name, self.phone, self.email))

    def __str__(self):
        return self.name

