import os

os.system("cls" if os.name == "nt" else "clear")

print("-------------------------------------")
# print("hello world!")
#! #############################################
#!Topics to be Covered:

#* Everything in Python is class
#? Defining class
#* Defining class attributes
#? Difference between class attributes and instance attributes
#* SELF keyword
#? Static methods
#* Special methods (init, str)
#? 4 pillars of OOP:
#     Encapsulation
#     Abstraction
#     Inheritance
#        Multiple inheritance
#     Polymorphism
#        Overriding methods
#* Inner class
#! #############################################



#! Defining class

# class Person:
#     company="clarusway"
#     department="IT"

# person1=Person()
# person2=Person()

# print(person1.company)

# Person.job="developer"
# print(person1.job)

# person2.location="Germany"
# print(person1.location)

#! SELF keyword

# class Person:
#     company="clarusway"
#     department="IT"

#     def test(self):
#         print("test")

#     def set_details(self,name,age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name,self.age)

#     #! static methods
#     @staticmethod
#     def salute():
#         print("Hi there!")


# person1=Person()
# person2=Person()
# # person1.test()

# person1.set_details("barry",40)
# person2.set_details("henry",35)

# person2.get_details()
# person1.salute()


#! Special methods (init, str)
#! Encapsulation


class Person:
    company = "clarusway"
    department = "IT"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  #instance cagirildiginda gosterilecek bilgiler icin olusturulan metod
        return f"{self.name} - {self.age}"


person1 = Person("hasan", 20)
print(person1)












print("-------------------------------------")
