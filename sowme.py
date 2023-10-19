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

