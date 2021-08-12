"""
TASK 1
Write a class to represent a Cash Register.
Your class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.
"""

class CashRegister:

    def __init__(self):

        self.total_items = dict()
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, value):

        self.total_items[item] = value

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, discount):
        self.discount = discount
        discounted_price = self.total_price - ((discount/100)*self.total_price)
        print("The total cost for this transaction with discount deducted is {}.".format(discounted_price))
        return discounted_price

    def get_total(self):
        for item in self.total_items:
            self.total_price += self.total_items[item]
        print("The amount to pay is £{}.".format(self.total_price))
        return self.total_price

    def show_items(self):
        for item in self.total_items:
            print("Item: {}, Price: {}".format(item, self.total_items[item]))

    def reset_register(self):
        self.total_items = {}
        self.total_price = 0
        self.discount = 0


# EXAMPLE code run:

#This line of code creates an instance of the class Cash Register.

transaction = CashRegister()

#In the following lines of code I add items to the register. These are added to a dictionary called total_items.

transaction.add_item("Tomatoes", 0.8)
transaction.add_item("Carrots", 0.65)
transaction.add_item("Red Pepper", 0.8)
transaction.add_item("Onion", 0.40)
transaction.add_item("Broccoli", 1.2)
transaction.add_item("Potatoes", 0.75)
transaction.add_item("Cauliflower", 1.2)

#This calls the remove item method, takes an argument of the item we want to remove and uses the pop() dictionary
# method to remove it from the dictionary.

transaction.remove_item("Broccoli")

#The following method totals the whole amount when each item price is added up.

transaction.get_total()

#The next method deducts the percentage off the total amount according to what percentage was passed as an argument.

transaction.apply_discount(10)

#This next line of code displays all the items which are currently inside the cash register

transaction.show_items()

#The following method sets the total_items and total_price back to zero.

transaction.reset_register()


"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""

class Student:

    def __init__(self, name, age, id, enrollment_year):
        self.name = name
        self.age = age
        self.id = id
        self.enrollment_year = enrollment_year
        self.subjects = dict()

#     create new methods that manage student's subects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

class SoftwareStudent(Student):

    def __repr__(self):
        return self.name

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade

    def remove_subject(self, subject):
        return self.subjects.pop(subject)

    def show_subjects(self):
        print("{} is enrolled in the following subjects: ".format(self.name))
        for subject in self.subjects:
            print(subject)

    def get_graduation_year(self, course_length):
        graduation_year = self.enrollment_year + course_length
        print("{} is due to graduate in {}".format(self.name, graduation_year))

    def get_overall_grade(self):
        count = 0
        score = 0
        for subject in self.subjects:
            count += 1
            score += self.subjects[subject]
        overall_grade = score/count
        print("{}'s overall grade is: {}".format(self.name, overall_grade))

# EXAMPLE code run:

student1 = SoftwareStudent("John Fitzgerald", 42, 4231, 2021)

student1.add_subject("Python 3", 72)
student1.add_subject("Java", 80)
student1.add_subject("Development Lifecycle", 89)
student1.add_subject("Debugging and Testing", 71)
student1.add_subject("SQL", 38)

print(student1)

student1.show_subjects()

student1.get_overall_grade()

student1.get_graduation_year(3)





