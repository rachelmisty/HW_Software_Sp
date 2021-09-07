"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""

import random

class CFGStudent:

    def __init__(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = id

    @staticmethod
    def generate_id():
            self.student_id = random.randint(1000, 10000)
            return str(self.student_id)
        # 'create a random new id, which is any number between 1,000 and 10,000'
        # 'return id as a string'
        # "Example '8754' "

    def get_id(self):
        print(self.student_id)

    def get_fullname(self):
        print(self.name + " " + self.surname)


class NanoStudent(CFGStudent):

    def __init__(self, name, surname, age, email, student_id, specialization):
        super().__init__(self, name, surname, age, email, student_id)
        self.specialization = specialization
        self.course_grades = dict()

    @staticmethod
    def generate_id():
            self.student_id = random.randomint(1000, 10000)
            return "NANO" + str(self.student_id)

    def add_new_grade(self, course, grade):
        self.course_grades[course] = grade

    def get_course_grades(self):
        print(self.course_grades)




############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""

#I don't remember how to generate Fibonacci numbers! I remember we had an example of a
#recursive function. Would this question require a recursive function?


def find_fibonacci_numbers():
    pass


# here I have assumed that I"ve generated the list above and I will pass this to the function below which
# sums up the even numbers:

fibonacci_numbers = [0,1,1,2,3,5,8,13,34]

def even_fibonacci_sum(lst):
    sum = 0
    for num in lst:
        if num % 2 == 0:
            sum += num
    return sum

print(even_fibonacci_sum(fibonacci_numbers))


##### TESTS ####

# print(even_fibonacci_sum(limit=10))  # should be 44
# print(even_fibonacci_sum(limit=15))  # should be 188
# print(even_fibonacci_sum(limit=1))   # should be 0


"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""

#I know this is not the correct answer at all even though the output is correct. I've had a complete mental blank over how I would store the positions of the
#numbers in the sequence and how I would compare this against the array. I've therefore only narrowed down the possibilities in my function.

def is_valid_subsequence(array, nums):
    count = 0
    index = []
    for i in array:
        for j in nums:
            if j not in array:
                return False # if any of the numbers aren't in array then the answer will be False
            elif i == j:
                count +- 1
    if count > len(nums): # if the number of times the values appear in the array is less than the sequence then it is necessarily false.
        return False
    return True


#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)


The class Employee breaks the Single Responsibility Principle as it has many responsibilities and is trying to do
too many things. It also breaks the Interface Segregation Principle because there are methods in the class
which do not need to be called when the class is instantiated and would be redundant within the object. For example:

the update_department method. I would create a class "Department" that would be separate from the Employee 
class. An Employee object would never necessarily need to call this method as it is not something which concerns
the Employee per se. 

print_employee_report. Again I would create a separate class for Report as this is something which could interact
with class Employee. A report method which opens a file could be a method which could be called on several different
types of objects, not just an employee. Eg a departmental report or database report.  

In terms of readability of the code the update_status method isn't clear. What is new_is_active? Does this mean
the Employee recently joined the company? for how long would this status remain active? Also if it does mean
that the Employee recently joined the company shouldn't this automatically be generated when an instance of the
Employee is created? I would write the code so this is clearer.

I would also put save_employee and Remove_employee methods into different classes. I would keep the saveemployee
method in this class and make it the sole responsibility of the class and then create a separate RemoveEmployee 
class as in general the less methods per class the better. 

Once a class has been created you don't want to have any further reasons to modify that class. You should only
wish to extend it's capabilities through concepts such as inheritance. 

"""






