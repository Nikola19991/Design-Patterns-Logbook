#!/usr/bin/env python
# coding: utf-8

# In[1]:


"Logbook 1"
msg = "Nikola's Shopping list"
print(msg)

shopping_list = ["milk", "eggs", "bread", "cheese", "tea", "coffee", "rice", "pasta", "milk", "tea"]
print ("This is my shopping list:", shopping_list)

shopping_tuple = ("milk", "eggs", "bread", "cheese", "tea", "coffee", "rice", "pasta", "milk", "tea")
print ("This is my shopping tuple:", shopping_tuple)

shopping_set = {"milk", "eggs", "bread", "cheese", "tea", "coffee", "rice", "pasta", "milk", "tea"}
print ("This is my Shopping_set with the duplicates removed:", set(shopping_list))

shopping_dict = {"milk": "£1.20", "eggs": "£0.87", "bread": "£0.64", "cheese": "£1.75", "tea": "£1.06", "coffee": "£2.15", "rice": "£1.60", "pasta": "£1.53"}
print ("This is my shopping_dict", shopping_dict)


# In[2]:


"Logbook 2"
list = ["USA","Mexico","Canada"]
list.append("Greenland")
print(list)

list.remove("Greenland")
print(list)

list.insert(0, "Greenland")
print(list)

print(list[:2])

print(list[-2])

print(list[1:3])


# In[78]:


"Logbook 3"
a=[0,1,2,3,4,5,6,7,8,9,10]
b=[0, 5, 10, 15, 20, 25]

topscores={"Jo":999, "Sue":987, "Tara":960, "Mike":870}

print("list a is...",a)
print("list b is...", b)
print("The type of a is now...", type(a))

a=set(a)
b=set(b)

print("set a is...",a)
print("set b is...",b)

print("The type of a is now", type(a))
print("The intersections of a and b is ", a.intersection(b))
print("The union of a and b is ", a.union(b))
print("Items unique to set b are ", b-a)

print("topscores dictionary keys are ", topscores.keys())
print("topscores dictionary values are ", topscores.values())


# In[79]:


"Logbook 4"
for name, street_address, town, postcode in zip(["T Cruise", "D Francis", "C White"], ["2 West St", "65 Deadend Cls", "15 Magdalen Rd"],
       ["Canterbury", "Reading", "Oxford"], ["CT8 23RD", "RG4 1FG", "OX4 3AS"]):

     print(name,",", street_address,",", town,",", postcode)


# In[90]:


"Logbook 5"
class Person:
    def __init__(self, first_name, second_name, age, uk_postcode):
        self.firstname = first_name
        self.secondname = second_name
        self.yr = age
        self.address = uk_postcode
    
    def greeting(self):
        print("Hello, my name is {0} {1}. I am {2} years old and my postcode is {3}.".format(self.firstname,
        self.secondname,
        self.yr,
        self.address))

person1 = Person("Freddy", "Jones", "22" , "HP6 7AJ")
person1.greeting()


class Student(Person):
    def __init__(self,
    first_name,
    second_name,
    age,
    uk_postcode,
    degree_subject,
    student_ID):

        super().__init__(first_name,
        second_name,
        age,
        uk_postcode,
        )

        self.Subject = degree_subject
        self.studentID = student_ID

    def getDegreeSubject(self):
        print("My student ID is {5} and I am reading {4}.".format(self.firstname,
        self.secondname,
        self.yr,
        self.address,
        self.Subject,
        self.studentID))

person2 = Student("Freddy", "Jones" , "22" , "HP67AJ" , "Computer Science", "SN123456")
person2.getDegreeSubject()
print()

student1 = Student("Dick" , "Turpin" , "32" , "HP11 2JZ" , "Highway Robbery" , "DT123456")
student2 = Student("Dorothy" , "Turpin", "25", "SO14 7AA" , "Law" , "DT123457")
student3 = Student("Oliver" , "Cromwell", "32" , "OX35 14RE" , "History" , "OC123456")
student4 = Student("Nikola" , "Georgiev" , "23" , "HP135NX" , "Dessign Patterns" , "21812898")

student_list = [student1, student2, student3, student4]
for i in student_list:
    print(i.greeting(), i.getDegreeSubject())
    


# In[5]:


"Logbook 6"
from tkinter import *

 
class MyController():
    def __init__(self,parent):
        self.parent = parent
        self.model = MyModel(self)   
        self.view = MyView(self)  
        self.view.setEntry_text('Add to Label') 
        self.view.setLabel_text('Ready')
    
    def quitButtonPressed(self):
        self.parent.destroy()
    def addButtonPressed(self):
        self.view.setLabel_text(self.view.entry_text.get())
        self.model.addToList(self.view.entry_text.get())
    def removeButtonPressed(self):
        self.view.setLabel_text(self.view.destroy_text.remove())
        self.model.removeFromList(self.view.destroy_text.remove())
    
    def listChangedDelegate(self):
        print(self.model.getList())
 
class MyView(Frame):
    
    def __init__(self,vc):
        self.frame=Frame()
        self.frame.grid(row = 0,column=0)
        self.vc = vc
        self.entry_text = StringVar()
        self.entry_text.set('nil')
        self.label_text = StringVar()
        self.label_text.set('nil')
        self.loadView()

    def loadView(self):
        quitButton = Button(self.frame,text = 'Quit', command= self.vc.quitButtonPressed).grid(row = 0,column = 0)
        addButton = Button(self.frame,text = "Add", command = self.vc.addButtonPressed).grid(row = 0, column = 1)
        removeButton = Button(self.frame,text = "Remove", command = self.vc.removeButtonPressed).grid(row = 0, column = 2)
        entry = Entry(self.frame,textvariable = self.entry_text).grid(row = 1, column = 0, columnspan = 3, sticky = EW)
        label = Label(self.frame,textvariable = self.label_text).grid(row = 2, column = 0, columnspan = 3, sticky = EW)

    def getEntry_text(self):
        return self.entry_text.get()
    def setEntry_text(self,text):
        self.entry_text.set(text)
    def getLabel_text(self):
        return self.label_text.get()
    def setLabel_text(self,text):
        self.label_text.set(text)
 
class MyModel():
    def __init__(self,vc):
        self.vc = vc
        self.myList = ['duck','duck','goose']
        self.count = 0
    def listChanged(self):
        self.vc.listChangedDelegate()
    def getList(self):
        return self.myList
    def initListWithList(self, aList):
        self.myList = aList
    def addToList(self,item):
        print("returned")
        myList = self.myList
        myList.append(item)
        self.myList=myList
        self.listChanged()
 
def main():
    root = Tk()
    frame = Frame(root )
    root.title('Hello TEST')
    app = MyController(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()  


# In[20]:


"Logbook 8"
import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class TextFactory():
    def createText(self, type_):
        return textTypes[type_]()

class TextBase():
    textvariable = 'black'
    background = 'white'
    def getTextConfig(self):
        return self.textvariable, self.background

class TextRed(TextBase):
    textvariable = 'red'
    background = 'red'

class TextGreen(TextBase):
    textvariable = 'green'
    background = 'green'
    
class TextBlue(TextBase):
    textvariable = 'blue'
    background = 'blue'

textTypes = [TextRed, TextGreen, TextBlue]


class ButtonFactory():
    def createButton(self, type_):
        return buttonTypes[type_]()

    
class ButtonBase():     
    relief     ='flat'
    foreground ='white'
    def getButtonConfig(self):
        return self.relief, self.foreground
    
    
class ButtonRidge(ButtonBase):
    relief     ='ridge'
    foreground ='red'        
    
    
class ButtonSunken(ButtonBase):
    relief     ='sunken'
    foreground ='Green'        

class ButtonGroove(ButtonBase):
    relief     ='groove'
    foreground ='Blue'        

buttonTypes = [ButtonRidge, ButtonSunken, ButtonGroove]
    
class OOP():
    def __init__(self): 
        self.win = tk.Tk()         
        self.win.title("Python GUI")      
        self.createWidgets()

    def createWidgets(self):    
        self.widgetFactory = ttk.LabelFrame(text=' Widget Factory ')
        self.widgetFactory.grid(column=0, row=0, padx=8, pady=4)        
        self.createTextFields()
        self.createButtons()
    
    def createTextFields(self):
               
        factory = TextFactory()
        
        sv=tk.StringVar()
        
        col = factory.createText(0).getTextConfig()[0]
        sv.set(col)
        
        bkg = factory.createText(0).getTextConfig()[1]
      
        action = tk.Entry(self.widgetFactory, textvariable=sv, background=bkg, foreground="white")
        action.grid(column=1, row=1)
        
        sv=tk.StringVar()
        
        col = factory.createText(1).getTextConfig()[0]
        sv.set(col)
        
        bkg = factory.createText(1).getTextConfig()[1]
        
        action = tk.Entry(self.widgetFactory, textvariable=sv, background=bkg, foreground="white")
        action.grid(column=1, row=2)
        
        sv=tk.StringVar()
        
        col = factory.createText(2).getTextConfig()[0]
        sv.set(col)
        
        bkg = factory.createText(2).getTextConfig()[1]
        
        action = tk.Entry(self.widgetFactory, textvariable=sv, background=bkg, foreground="white")
        action.grid(column=1, row=3)
        
    def createButtons(self):
            
        factory = ButtonFactory()

        rel = factory.createButton(0).getButtonConfig()[0]
        fg  = factory.createButton(0).getButtonConfig()[1]
        
        action = tk.Button(self.widgetFactory, text="Button "+str(0+1), relief=rel, foreground=fg)   
        action.grid(column=0, row=1)  

        rel = factory.createButton(1).getButtonConfig()[0]
        fg  = factory.createButton(1).getButtonConfig()[1]
        
        action = tk.Button(self.widgetFactory, text="Button "+str(1+1), relief=rel, foreground=fg)   
        action.grid(column=0, row=2)  
        
        rel = factory.createButton(2).getButtonConfig()[0]
        fg  = factory.createButton(2).getButtonConfig()[1]
        
        action = tk.Button(self.widgetFactory, text="Button "+str(2+1), relief=rel, foreground=fg)   
        action.grid(column=0, row=3)
        
oop = OOP()
oop.win.mainloop()


# In[19]:


"Logbook 9"
class Animal:
    def speak(self):
        pass
    
    
class AnimalFactory:
    def createAnimal(self, type_):
        return animaltypes[type_]()
    
    
class Dog:
    def speak(self):
        return "Woof!"
    def __str__(self):
        return "Dog"


class DogFactory(AnimalFactory):
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "Dog Food!"
      
    
class Cat:
    def speak(self):
        return "Meeoowww!"
    def __str__(self):
        return "Cat"
    
    

class CatFactory(AnimalFactory):
    def get_pet(self):
        return Cat()
    def get_food(self):
        return "Cat Food!"
    
animaltypes = [Dog, Cat]


class PetStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory
    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))


#Create a Concrete Factory
factory = DogFactory()
#Create a pet store housing our Abstract Factory
shop = PetStore(factory)
#Invoke the utility method to show the details of our pet
shop.show_pet()
factory = CatFactory()
shop = PetStore(factory)
shop.show_pet()


# In[22]:


"Logbook 11"
import sys

#list with the first four items of top4books
top4books=["Anna Karenina by Leo Tolstoy", "Madame Bovary by Gustave Flaubert", "War and Peace by Leo Tolstoy", 
           "Lolita by Vladimir Nabokov"]
iter_listBooks = iter(top4books)

try:
    print ( next(iter_listBooks))
    print ( next(iter_listBooks))
    print ( next(iter_listBooks))
    print ( next(iter_listBooks))
    print ( next(iter_listBooks))
except Exception as e:
    print(e)
    print(sys.exc_info())


# In[26]:


"logbook 13"
def docStringDecorator(f):
    def decorator():
        '''Decorator that automatically reports name and docstring for a decorated function'''
        print("<<< Name of the 'decorated' function ... ",f.__name__," >>> ")
        print("<<< Docstring for the 'decorated' function is ... ",f.__doc__," >>>")
    return decorator

@docStringDecorator
def aTestMethod():
    '''This is a method to test the docStringDecorator'''
    nm = input("What is your name? ... ")
    msg = "Hello ... " + nm
    return msg

print (aTestMethod())


# In[ ]:




