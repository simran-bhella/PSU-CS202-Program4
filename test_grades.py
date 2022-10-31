import grades
import calc
import list
import BST
import pytest

#Simranjit Bhella
#5/27/2022
#CS202
#The purpose of this code is to set up the pytest testing suite for the gradebook program. Below are sever different tests sorted into relvent catagories.
#These catagories (not including fixtures) are object creation testing, operator testing, data edit testing, and calc functions testing
#Two tests below are designed to fail, those being the ones that test negtaive numbers as they raise errors.


#
#Fixtures for pytest testing
#
@pytest.fixture
def grade_setup():
    this_grade = grades.grade("Generic Grade", 50, "1/1", "Generic Comments")
    return this_grade

@pytest.fixture
def assignment_setup():
    this_assignment = grades.assignment("Program #1", 60, "6/20", "Well done", "Recursion", [grades.grade("Progress Submission #1", 90, "6/10", "Good first submission"), grades.grade("Progress Submission #2", 40, "6/16", "Could use some work")])
    return this_assignment

@pytest.fixture
def exam_setup():
    this_exam = grades.exam("Midterm #1", 90, "7/11", "Great work on this one!", ["Recursion", "Python"], 91)
    return this_exam

@pytest.fixture
def demo_setup():
    this_demo = grades.demo("Midterm Proficiency Demo", 10, "12/14", "Needs improvement", "Delete largest node", "1 hour")
    return this_demo

@pytest.fixture
def student_setup():
    this_student = list.Student("John")
    return this_student

@pytest.fixture
def calc_setup():
    this_calc = calc.gradecalc()
    return this_calc

@pytest.fixture
def bst_setup():
    this_bst = BST.BSTNode()
    return this_bst

#
#Object creation testing:
#
def test_gradeCreation_success(grade_setup):
    assert grade_setup.get_name() == "Generic Grade"
    assert grade_setup.get_score() == 50

def test_assignmentCreation_success(assignment_setup):
    assert assignment_setup.get_name() == "Program #1"
    assert assignment_setup.get_score() == 60
    
def test_examCreation_success(exam_setup):
    assert exam_setup.get_name() == "Midterm #1"
    assert exam_setup.get_score() == 90

def test_demoCreation_success(demo_setup):
    assert demo_setup.get_name() == "Midterm Proficiency Demo"
    assert demo_setup.get_score() == 10

def test_studentCreation_success(student_setup):
    assert student_setup.name == "John"

def test_calcCreation_success(calc_setup):
    assert calc_setup.this_student == None

def test_BSTCreation_success(bst_setup):
    assert bst_setup.data == None

#
#Operator testing:
#
def test_gradeOperator_Plus(grade_setup):

    new_grade = grade_setup + 10
    assert new_grade.get_score() == 60

def test_gradeOperator_Minus(grade_setup):

    new_grade = grade_setup - 10
    assert new_grade.get_score() == 40

def test_gradeOperator_Gt(grade_setup, demo_setup):

    assert grade_setup > demo_setup

def test_gradeOperator_Ge(grade_setup, demo_setup):

    assert grade_setup >= demo_setup

def test_gradeOperator_Lt(grade_setup, demo_setup):

    assert demo_setup < grade_setup

def test_gradeOperator_Le(grade_setup, demo_setup):

    assert demo_setup <= grade_setup

#
#Data edit testing:
#
def test_gradeEdit(grade_setup):
    grade_setup.edit_name("New Generic Grade Name")
    assert grade_setup.get_name() == "New Generic Grade Name"

    grade_setup.edit_score(60)
    assert grade_setup.get_score() == 60

#
#Student linked list function testing:
#
def test_gradeInsert(assignment_setup, exam_setup, demo_setup, student_setup):

    student_setup.insert(assignment_setup)
    assert student_setup.head.data == assignment_setup

    student_setup.insert(exam_setup)
    assert student_setup.head.next.data == exam_setup

    student_setup.insert(demo_setup)
    assert student_setup.head.next.next.data == demo_setup



def test_gradeRemove(demo_setup, student_setup):
    student_setup.insert(demo_setup)

    student_setup.remove(demo_setup)
    assert student_setup.head == None




#
#Calc functions testing:
#
def test_importStudent(assignment_setup, exam_setup, demo_setup, student_setup, calc_setup):
    student_setup.insert(assignment_setup)
    student_setup.insert(exam_setup)
    student_setup.insert(demo_setup)

    calc_setup.import_student(student_setup)

    assert calc_setup.this_student == student_setup

def test_setWeights(calc_setup):
    calc_setup.set_weights(.60, .30, .10)
    assert calc_setup.assignment_weight == .60
    assert calc_setup.exam_weight == .30
    assert calc_setup.demo_weight == .10

#this one should fail
def test_setWeights_negative(calc_setup):
    calc_setup.set_weights(-.60, -.30, -.10)
    assert calc_setup.assignment_weight == -.60
    assert calc_setup.exam_weight == -.30
    assert calc_setup.demo_weight == -.10

def test_setPassing(calc_setup):
    calc_setup.set_passing(80)
    assert calc_setup.passing_score == 80

#this one should also fail
def test_setPassing_negative(calc_setup):
    calc_setup.set_passing(-80)
    assert calc_setup.passing_score == -80


def test_totalGrades(assignment_setup, exam_setup, demo_setup, student_setup, calc_setup):
    student_setup.insert(assignment_setup)
    student_setup.insert(exam_setup)
    student_setup.insert(demo_setup)

    calc_setup.import_student(student_setup)

    calc_setup.set_weights(.60, .30, .10)
    calc_setup.set_passing(80)

    assert calc_setup.total_grades() == 64

def test_ifPassing(assignment_setup, exam_setup, demo_setup, student_setup, calc_setup):
    student_setup.insert(assignment_setup)
    student_setup.insert(exam_setup)
    student_setup.insert(demo_setup)

    calc_setup.import_student(student_setup)

    calc_setup.set_weights(.60, .30, .10)
    calc_setup.set_passing(63)

    calc_setup.total_grades()

    assert calc_setup.check_passed() == True


#
#BST functions testing:
#
def test_BSTInsert(bst_setup, student_setup):
    bst_setup.insert(student_setup)
    assert bst_setup.data == student_setup

def test_BSTDelete(bst_setup, student_setup):
    bst_setup.insert(student_setup)
    bst_setup.insert(student_setup)
    bst_setup.delete(student_setup)
    assert bst_setup.right == None and bst_setup.left == None

def test_BSTFind(bst_setup, student_setup):
    bst_setup.insert(student_setup)
    found = bst_setup.find("John")

    assert found == student_setup

    



