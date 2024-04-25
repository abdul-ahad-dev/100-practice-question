from datetime import date


class Person:

    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            age -= 1
        return age

    def get_info(self):
        print("Name : ", self.name)
        print("Country : ", self.country)
        print("Date of Brith : ", self.dob)
        print("Age : ", self.age())


person1 = Person("Abdul Ahad", "Pakistan", date(2003, 8, 25))
person2 = Person("Omar", "Iran", date(2001, 3, 9))
person3 = Person("Aslan", "Turkiye", date(2006, 12, 16))

person1.get_info()
print()
person2.get_info()
print()
person3.get_info()
