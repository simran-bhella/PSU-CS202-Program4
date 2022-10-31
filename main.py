import list
import grades
import calc
import BST

#Simranjit Bhella
#5/27/2022
#CS202
#The purpose of this code is to simply test some of the functions during development. With the pytest testing suite this is now irrelvent but I thought I'd go ahead and include it in the program anyways.

def Main():
    print("-- Start --")

    d = grades.demo("Name", 10, "12/14", "Well done", "Remove Last", 60)

    e = grades.exam("Name", 60, "3213", "Not bad", ["Recursion", "Python"], 4)

    a = grades.assignment("Name", 70, "1412", "Good Work", "Gaming", [grades.grade("Name", 4, "321", "Good first"), grades.grade("Name", 12, "4234", "Great work on second")])

    john = list.Student("John")
    baron = list.Student("Baron")
    danny = list.Student("Danny")

    john.insert(d)
    john.insert(e)
    john.insert(a)
    john.insert(a)

    baron.insert(d)
    baron.insert(e)
    baron.insert(a)
    baron.insert(a)

    danny.insert(d)
    danny.insert(e)
    danny.insert(a)
    danny.insert(a)


    g = calc.gradecalc()

    g.import_student(john)

    g.set_weights(.30,.60,.10)

    g.set_passing(80)

    g.total_grades()

    is_passing = g.check_passed()

    print(f"Total grade: {g.total_grade}")
    print(f"Passing: {is_passing}")

    b = BST.BSTNode()
    print("\n")
    print("BST Work:")

    b.insert(john)
    b.insert(baron)
    b.insert(danny)


    b.display([])

    b.delete(baron)

 

    print("\n")
    print("After deleting:")

    b.display([])

    print("After finding: ")
    found = b.find("John")

    found.display()


Main()