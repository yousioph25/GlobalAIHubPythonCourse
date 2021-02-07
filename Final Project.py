class Employee:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def employee_lang(self):
        print("Employee " + self.name + ":" +
              " They can speak " + self.language)


Employee1 = Employee("Oje", "20", "Arabic")
Employee1.employee_lang()

Employee2 = Employee("Adedeji", "22", "English")
Employee2.employee_lang()


class Manager:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def employee_lang(self):
        print("Manager " + self.name + ":" +
              " They can speak " + self.language)


Manager1 = Manager("Yusuf", "45", "French")
Manager1.employee_lang()

Manager2 = Manager("Ashamu", "25", "French")
Manager2.employee_lang()
