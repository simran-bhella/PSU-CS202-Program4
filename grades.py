import list
import calc

#Simranjit Bhella
#5/27/2022
#CS202
#The purpose of this code is to set up the grade hierarchy.
#This file includes the grade base class with the assignment, exam, and demo derived classes.
#The grade class has pushed up data as well as edit and display functions, and operators
#The 3 derived classes all have their own extra data members as edit functions for them and display functions

#Base class
class grade:
    def __init__(self, name, score, date, comments):
        self.__name = name
        self.__score = score
        self.__date = date
        self.__comments = comments

    def edit_name(self, name):
        self.__name = name
        return

    def edit_score(self, score):
        self.__score = score
        return
    
    def edit_date(self, date):
        self.__date = date
        return

    def edit_comments(self, comments):
        self.__comments = comments
        return

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Score: {self.__score}")
        print(f"Date: {self.__date}")
        print(f"Comments: {self.__comments}")


    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    #will use operators for BST management, and score manipulation

    def __add__(self, other):
        score = self.__score + other
        return grade(self.__name, score, self.__date, self.__comments)
    
    def __sub__(self, other):
        score = self.__score - other
        return grade(self.__name, score, self.__date, self.__comments)

    def __eg__(self, other):
        if self.__score == other.get_score():
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.__score < other.get_score():
            return True
        else:
            return False
    
    def __gt__(self,other):
        if self.__score > other.get_score():
            return True
        else:
            return False

    def __le__(self, other):
        if self.__score <= other.get_score():
            return True
        else:
            return False

    def __ge__(self,other):
        if self.__score >= other.get_score():
            return True
        else:
            return False
        
    
#Derived classes with base class functions
class assignment(grade):
    type = "assignment"
    def __init__(self, name, score, date, comments, topic, submissions):
        grade.__init__(self, name, score, date, comments)
        self.__topic = topic
        self.__submissions = submissions #grade object

    def edit_topic (self, topic):
        self.__topic = topic
    
    def add_submission(self, submission):
        self.__submissions.append(submission)

    #remove by name
    def remove_submission(self, name):
        i = 0
        found = False
        for t in self.__submissions:
            if t.get_name() == name:
                found = True
                break
            i+= 1
        
        if found:
            del self.__submissions[i]
    
    def display(self):
        grade.display(self)
        print(f"Topic: {self.__topic}")

        print("Submissions: ")
        for t in self.__submissions:
            grade.display(t)
            print("\n")
        print("\n")


class exam(grade):
    type = "exam"
    def __init__(self, name, score, date, comments, topics, curve):
        grade.__init__(self, name, score, date, comments)
        self.__topics = topics
        self.__curve = curve
    
    def add_topics(self, topic):
        self.topics.append(topic) 
    
    def remove_topics(self, topic):
        self.topics.remove(topic)
    
    def edit_curve(self, curve):
        self.curve = curve

    def display(self):
        grade.display(self)

        print("Topics: ")
        for t in self.__topics:
            print(t)

        print(f"Curve: {self.__curve}")
        print("\n")
    

class demo(grade):
    type = "demo"
    def __init__(self, name, score, date, comments, prompt, time):
        grade.__init__(self, name, score, date, comments)
        self.__prompt = prompt
        self.__time = time

    def edit_prompt(self, prompt):
        self.__prompt = prompt
    
    def edit_time(self, time):
        self.__time = time

    def display(self):
        grade.display(self)
        print(f"Prompt: {self.__prompt}")
        print(f"Time: {self.__time}")
        print("\n")