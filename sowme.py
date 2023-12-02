Python is an 'Interpreter'
LEFT to RIGHT
Interprets compiles each line of source code one by one. in interpret source code is open (not safe)  Adv. -  Easy to debug. 
Compiler compiles the entire code by combining it as a package. If there is an error, it will just say it is an error rather than explaining about the type or location of the error.
In compiler source code is safe

Difference between Interpreter and Compiler --> Interpreter codes are risky. In compiler, codes are safe as it cannot be cracked easily.

Low level language - Machine readable
High level language - User readable 

Python is a high level language.
Python is CASE-SENSITIVE

LANGUAGE( 4 components)
  # alpha chars
  # dictionary(python modules) or also called "LEXIX"
  # syntax("eg:learning I python am")
  # symantics(sence/meaning)

MODULES:
Modules come from THREE different places
  # Python itself (from the installation)
  # Third-party modules (from Github, python repository etc) - Invoke third party modules using 'pip' command. connected from the internet.
  # From your own code

PEP: PYTHON ENHANCEMENT PROPOCALS
  --->style guide for python code.

#TO GO BACKWARDS FROM ONE FOLDER TO ANOTHER
---> cd..
#TO LIST FILES AND FOLDERS
--->dir
"git pull"---> the key word used to see the changes or updates what have they done.
#FOR CHANGING THE DRIVES
c: or d: or e: (enter)

Python extension .py

Code inside the text editor - Source code
File containing the source code - Source file 

To run a python program, in command prompt, type "python" followed by the absolute location of the source file.
  # Absolute path is the complete location of the file from the basic folder.
  # Relative path is the shorter file location path - which will be used in Linux

Comments can be differentiated from the source code by using # in front of each comment line.
Multi lines in a source code can be converted as comments by typing them between triple double quotes.

# PYTHON codes can be run in IDE's (Integrated Development Environment)
# PyCharm is one such IDE
----------------------------------------------------------------------------------------------------------------------------------------------------------
# DATA TYPES ( String,Integer,float,Boolean)

#STRING:-
   *anything which is under the double(") or single codes(')
example
  #print("hello")---->argument
  #print("897655578")

#POSITIONAL ARGUMENTS:-
  print ("Hello","World") will give the output "Hello World"
  "Hello" is the first argument' "World" is the second argument

#KEYWORD ARGUMENTS:-
  *print("hello","world",sep='')
         #sep= used to seperate multiple arguments
  *print("hello"."world",end='')
         #end= how much ever arguments present in it , #end decides how the code as to end.

#SPECIAL CHARACTER:-
  *print("hello \t world")
  *print("hello \n world")
\t---> used for tab space
\n---> used for next line

#ESCAPE CHAR:=
Escapte Character - Used to break that character as an ending syntax character
"\"
  *print ("I'm learning Python") --> I'm learning Python
  *rint ('I\'m learnig "Python") --> I'm learning "Python"

1)---> print("\"I'm\"", "\"\"learning\"\"", "\"\"\"Python\"\"\"", sep='\n')
       print('"' + "I'm" + '"', '""' + "learning" + '""', sep='\n')
       output:=
              "I'm"
           ""learning""
           """Python""" 

# Integer
  print(55555)

# Float
  print(555.55)
  print(55.)
  print(.5)

# Boolean
  print(True, False)
  print(5 > 9)
  print(5/9)

# Variable
  x = 5
  y = 9
  result = x * y
  print('Multiplication of', x, 'and', y, 'is', result)

# Operators (7) & Comparison Operators (6)
# BODMAS
  print(5 + 9)
  print(5 - 9)
  print(5 / 9)
  print(5 * 9)
  print(5 ** 9 ** 2)  # Exponential
  print(5 % 9 % 2)  # Modulus
  print(26 // 9)  # Floor division

# Comparison Operators (6)
  print(5 > 9)
  print(5 < 9)
  print(5 >= 9)
  print(5 <= 9)
  print(5 == 9)  # Compare
  print(5 != 9)  # not equal to

# input (Always string)
  a = input('Enter first no: ')
  b = input('Enter second no: ')
  print(int(a) + int(b))
  print(float(a) + float(b))
  print(str(a) + str(b))
  print(bool(a > b) + bool(a < b))

name = 'Bob'
print("Hello", name + '!')
print(f"Hello {name}!")

a = 5
b = 8

print(f"Sum of {a} and {b} is {a + b}.")

# Conditions
a = int(input('Enter any no: '))

if a < 0:
    print(f"{a} is a negative no.")
elif a >= 0 and a <= 100:
    print(f"{a} is between 0 and 100.")
elif 101 <= a <= 200:
    print(f"{a} is between 101 and 200.")
else:
    print(f"{a} is greater than 200.")

if a < 50 or a > 100:
    print('')

# If the no is even and less than 100,
# If the no is even and divisible by 5,
# if the no is odd and greater than 100,

word = input('Enter a word: ')

if word == "Spathiphyllum":
    pass
elif word == "spathiphyllum":
    pass
else:
    pass

a = 50000 / 0.7
result = round(a, 2)
print(a, result)

# Index no and Slicing
  a = 'asdasfsdgdfgdfhdfhg'
  print(a[1])
  # a[start:stop:step]
  print(a[3] == 'i')
  print(len(a))
  print(a[:len(a)//2])

28/10/2023
  #END TIME PRLM
# hours=int(input("starting time(hours):"))
# mins=int(input("starting time(mins):"))
# dura=int(input("event duration:"))
# # time_hour=(hours+dura//60+(mins+dura%60)//60)%24
# # time_min=(mins+dura%60)%60
# # print("it will end at"+str(time_hour)+":"+str(time_min))
#
# left=((hours*60+mins+dura)//60)%24
# right=(mins+dura)%60
# print(left,right,sep=':')

# while true:
#     uname=input("enter ur username:")
#     if uname=='admin':
#         passwrd=input("enter ur passwrd:")
#         if passwrd=='admin':
#             otp=input("enter otp:")
#             if otp=="1234":
#                 print("login sucessful")
#                 break
#             else:
#                 print("incorrect otp.try again")
#         else:
#             print("incorrect password.try again")
#     else:
#         print("incorrect uname.try again")
#
# #GUESSING GAME EXAMPLE
# no=777
# while true:
#     answer=input('guess')
#     if int(answer)==no:
#         print('correctly guessed')
#         break
#     else:
#         print('incorrectly guessed.Try again')
#
# no=0
# while no<100:
#     no=no+1

# no=0
# while no<24:
#     no=no+1
#     if no%2==0:


# no=0
# while no<12:
#     no=no+1
#     print(f"2 x {no}= {no*2}")

# word='mississppi'
# count=0
# start=0
# stop=len(word)
# while start < stop:
#     if word[start]=='s':
#         count=count+1
#     start=start+1
# print(count)

count=0
while count<3:
    count=count+1
    uname=input('username:')
    if name=='admin':
        count=0
        count_passwrd=0
        while count_passwrd<3:
            count_passwrd=count_passwrd+1
            passwrd=input('passwrd')
            if passwrd=='admin':
                print("login sucessfully")

nos_tuple=(1,2,3) #cannot be modified-immutable
nos_list[1,2,3] #mutable
nos_dict={
'subject':'python'
'dept':'it'
'roll.no':229
'marks':[88,89,78,78,90]
'x':{3,4,5,6}
}
#key:values pairs

#iterate_one by one
name='I am learning python'
no=0
while true:
print(name[no])
no=no+1
if no>len(name)-1
break

#for loop
for i in name:
print(i)

example1:
nos=[]
for i in range(51):
    if i % 2==0:
        nos.append(i)
print(nos)

example2:
nos=[]
for i in range(5,51,5):
    nos.append(i)
print(nos)

example3:
name='I am learning python'
for i in name:
    if i==' ':
         continue
    else:
         print(i,end='')
#output:
Iamlearningpython

example4:
# count=0
# nos=[]
# while True:
#     count=count+1
#     nos.append(count)
#     if count==50:
#         break
# print(nos)

example5:
# count=0
# nos=[]
# while True:
#     count=count+5
#     nos.append(count)
#     if count==50:
#         break
# print(nos)

example6:
word='the'
for i in word:
    print(i*2,end='')
    #output
    tthhee

example7:    
#Program to count the word python
word='I Python am learning Python'
count=0
for i in range(len(word)-5):
     a= word[i] + word[i+1] + word[i+2] + word[i+3] + word[i+4] + word[i+5]
     if a=='Python':
        count=count+1
print(count)

example8: count even number from the list
count=0
count_evens=[2,1,2,3,4]
for i in count_evens:
      if i%2==0:
          count=count+1
print(count)
#output:3
-------------------------------------------------------------------------------------------------------------------------------------------------------------
FUNCTIONS
#def a keyword - definition
#we can reuse the code by functions
EXAMPLE
def adding(a,b,d):
   c=a+b+d
   print(c)
adding(6,8,9)

def greeting(name):
    print("welcome",name+'.')
greeting(sowme)

def uname_gen(fname,lname):
  print(fname+'.'+lname)
  print(fname+'.'+lname[0])
  print(fname[0]+'.'+lname)
  print(fname[0]+lname)
  print(fname+lname[0])

def greeting(name):
  return 'welcome'+ name+'.'
print(greeting('kamal'))
#OUTPUT
welcome kamal.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
SIMPLE WAY TO HANDLE A FILE:-
for i in range(1,10):
              #write-w , read=r , append=a
with open('notes.txt','a')-->#file name# as file:
file.write(str(i)='\n')

TO READ A FILE
data=[]
with open('notes.txt','r')as file:
a=file.read()
print(a)
OUTPUT: will be in list

for i in a 
b=i.strip()
print(b)
OUTPUT: will be in string

b=i.strip()
data.append(int(b))
print(data)
OUTPUT:will be in integer

with open('notes.txt','r')as file:
a=file.readline()
data=list(map(int,a))
print(data)
OUTPUT:[1,2,3,4,........,100]

#CRUD--> create,read,update,delete

def file_read():
    try:
        with open('data.csv','r')as file:
            a=file.read()
            print(a)
    except FileNotFoundError:
        print("error 0*001:input file doesn't exit")
def file_write(data):
    with open('data,csv','w')as file:
        file.write(data)
def file_append(data):
    with open('data.csv','a')as file:
        file.write(data)
def read_from_a_file(file):
    with open('file','r')as file:
        a=file.readlines()
        data=list(map(int a))
        return data
file_write('this is the first line')
file_read()
file_append('\n this is the second line')
file_read()
data=read_from_a_file(file path)
for i in data:
    file_append('\n'+str(i))
file_read()
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CLASS:-
  #To reduce the repeatation of code in fucntions---->class
  #In class we have to use camel case
  #Eg:- Class ReportCard
  # A copy of a class is called instance
  # class is a blueprint

  class Student:
    # A fuction inside a class is called 'METHOD'
    def name(self,name):
        return name
    def course(self,course):
        return course
    def phone(self,phone):
        return phone
    def email(self,email):
        return email
    def student_contact(self):
        return self.name,self.phone


#instance
student1=student()
student1.name='rajini'
student1.course='python'
student1.phone=99990009999
student1.email='rajini12@gmail.com'

student2=student()
student2.name='kamal'
student2.course='python'
student2.phone=77777888888
student2.email='kamal34@gmail.com'

print(student1.student_contact())
print(student2.student_contact())
--------------------------------------------
class Students:
#contructors,magic methods
    def __init__(self,name):
        self.name=name
        self.email=email
        self.phone=phone
    def username(self):
        return self.name+self.email[0:4]
#instance
student1=students('rajini', 'rajini@gmail.com', 7777777777)
student2=student('kamal', 'kamal@gmail.com', 8888888888)

print(student1.name)
print(student1.username())
print(student2.name)
print(student2.username())
-------------------------------------
class Products:
    all=[]
    discount=0.8
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

        Products.all.append(self.name)

    def total_price(self):
        return self.price+self.quntity
    def discounted_price(self):
        return run Products.total_price(self)*Products.discount
    #Another magic keyword used to create ur own representation on how ur products what to display
    def __repr__(self):
        return f"Products('{self.name},{self.price},{self.quantity})"

mobiles=Products('samsung',10000,3)
computers=Products('apple',30000,4)
laptops=Products('lenovo',8000,7)
for i in Products.all:
    print(i)

print(mobiles.discounted_price())
----------------------------------------------
class Products:
    all=[]
    discount=0.8
    def __init__(self,name,price,quantity):
       * assert price>=0,f"{price}is less than 0"
       *assert quantity>=0 f"{quantity}is less than 0"
       *assert len(name)>2 f"{name}is less than 0"
        self.name=name
        self.price=price
        self.quantity=quantity

        Products.all.append(self.name)

    def total_price(self):
        return self.price+self.quntity
    def discounted_price(self):
        return run Products.total_price(self)*self.discount
    #Another magic keyword used to create ur own representation on how ur products what to display
    def __repr__(self):
        return f"Products('{self.name},{self.price},{self.quantity})"

mobiles=Products('samsung',10000,3)
computers=Products('apple',30000,4)
laptops=Products('lenovo',8000,7)

  



















  


