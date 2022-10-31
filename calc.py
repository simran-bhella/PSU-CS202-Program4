import grades
import list

#Simranjit Bhella
#5/27/2022
#CS202
#The purpose of this code is to set up the gradecalc class which is used for managing the grade objects from grades.py.
#The gradecalc class holds a lot of data but it pertains to one student per gradecalc object (this may change with program #5).
#The gradecalc class includes the import student function, the set weights function, the set passing function, the total grades function, and the check passed function

class gradecalc:
    def __init__(self):
        self.this_student = None
        self.assignments = []
        self.exams = []
        self.demos = []

        self.assignment_weight = 0
        self.exam_weight = 0
        self.demo_weight = 0
        self.passing_score = 0

        self.total_grade = 0

    #This function takes in and stores a Student (linked list) object as well as sorts the grades out by type into lists
    def import_student(self, student):

        self.this_student = student

        tmp = student.head

        while tmp:
            
            if tmp.data.type == "assignment":
                self.assignments.append(tmp.data)

            if tmp.data.type == "exam":
                self.exams.append(tmp.data)

            if tmp.data.type == "demo":
                self.demos.append(tmp.data)

            tmp = tmp.next

    #This function allows for the weights of the 3 grade types to be set
    def set_weights(self, assignment_weight, exam_weight, demo_weight):

        #Raises an error if value is negative
        if assignment_weight < 0 or exam_weight < 0 or demo_weight < 0:
            raise ValueError("Weight can't be negative!")

        else:
            self.assignment_weight = assignment_weight
            self.exam_weight = exam_weight
            self.demo_weight = demo_weight

    #This function allows for the score required to pass to be set.
    def set_passing(self, score):

        #Raises an error if value is negative
        if score < 0:
            raise ValueError("Passing score can't be negative!")

        else:
            self.passing_score = score

    #This function takes in the different scores from the grade objects and the weights to determine the total grade
    #expecting decimals for weight and percent as integer for grades
    def total_grades(self):

        total = 0

        #not super positive on the actual logic for calculating total score based on weight, but this is what my research found for the calculation
        for t in self.assignments:
            total += t.get_score()*self.assignment_weight

        for t in self.exams:
            total += t.get_score()*self.exam_weight

        for t in self.demos:
            total += t.get_score()*self.demo_weight

        self.total_grade = total

        return total


    #This function checks if the total grade is greater than or equal to the score required to pass
    def check_passed(self):

        if self.total_grade >= self.passing_score:
            return True

        else:
            return False


#This is extra code that does not fit in with the current requirments, but parts may be relvent/useful for Program #5's BST...
# Anyways, just holding onto it for right now.
#             
# class gradebook:
#     def __init__(self):
#         self.grades = {"assignment":[],"exam":[],"demo":[]}
#         self.assignment_weight = 0
#         self.exam_weight = 0
#         self.demo_weight = 0

#     def add_grade(self, grade):

#         self.grades.get(grade._type).append(grade)

#     def remove_grade(self, _type, name):

#         _list = self.grades.get(_type)
#         i = 0
#         found = False
#         for t in _list:
#             if t.get_name() == name:
#                 found = True
#                 break
#             i+= 1
#         if found:
#             del _list[i]

#     def set_weights(self, assignment_weight, exam_weight, demo_weight):

#         self.assignment_weight = assignment_weight
#         self.exam_weight = exam_weight
#         self.demo_weight = demo_weight

#     def average_grades(grade):
#         return

#     def display():
#         return


