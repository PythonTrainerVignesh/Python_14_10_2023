# n = input("Enter your name ")
# print('Hello'+" "+n+"!")

# a= input('Enter A: ')
# b= input('Enter B: ')
# print(a+b+b+a)

# tag= input("Enter the tag: ")
# word= input("Enter the word: ")
# print(f'<{tag}>{word}</{tag}>')

# n = input("Enter a number: ")
# if int(n) % 2 == 0:
#     print (f"{n} is an Even number")
# else:
#     print (f"{n} is an Odd number")


# a = input("Enter a plant: ")
# b = "Spathiphyllum"
# c = "spathiphyllum"
# if(a == b):
#     print(f"Yes - {a.capitalize()} is the best plant ever!")
# elif(a ==c):
#     print(f"No, I want a big {a.capitalize()}!")
# else:
#     print(f"{c.capitalize()}! Not {a}")

# a = input("Enter a plant: ")
# if a == "Spathiphyllum":
#     print(f"Yes - {a} is the best plant ever!")
# elif a == "spathiphyllum":
#     print(f"No, I want a big Spathiphyllum")
# else:
#     print(f"Spathiphyllum! Not {a}!")


# income = float(input("What is your income? "))
# if income < 85528:
#    tax = (income*0.18) - 555.98
#    if tax <=0:
#        print("Zero tax")
#    else:
#    print(f"The tax is : {round(tax, 0)} Thalers")
# else:
#    print('High income')
# else:
#     tax = 14839.02 + ((85528 - income) * 0.32)
#     if tax <= 0:
#     print("The tax is 0.0 Thalers")
#     else:
#     print(f"The tax is : {round(tax,0)} Thalers")

# a='111222'
# b='Yay'
# c=len(a)//2
# print(a[:c]+b+a[c:])


# john = 3
# mary = 5
# adam = 6
# print(f'{john},{mary},{adam}')
# total_apples = john + mary + adam
# print(f'Total number of apples: {total_apples}')


# year = 1996
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is a common year")
#
# year = input("Enter a year: ")
# if (int(year) % 4 == 0 + int(year) % 100 != 0) or (int(year) % 400 == 0):
#     print("leap year")
# else:
#     print("common year")


# if float(income) <= 85528:
#     tax = (flot(income) * 0.18) - 556.02
# else:
#     tax = 14839.02 + (0.32 * (float(income) - 85528))
#     income = input("Enter your income in thalers: ")
# if tax < 0:
#     tax = 0whe
# print(f"The tax is: {round(tax)}.0 thalers")

# h = int(input("Enter hrs: "))
# m = int(input("Enter mins: "))
# d = int(input("Enter duration: "))
# # time = (h*60) + m + d
# # if time >= 1440:
# #     time = time - 1440
# #     print (f"{(time//60)}:{time%60}")
# # else:
# #     print (f"{round(time/60)}:{time%60}")
#
# #Alternate Code
# left = ((h * 60 + m + d) // 60) % 24
# right = (m + d) % 60
# print(left,right,sep =':')


# Qn: If user name is 'admin', password is 'admin' and otp is '1234' print "Login Successful" if any of it fails,
# return error msg

# while True:
#     uname = input("Enter your username: ")
#     if uname == 'admin':
#         pwd = input("Enter your password: ")
#         else:
#         print('Incorrect username')
#         if pwd == 'admin':
#             otp = input("Enter your OTP: ")
#             if otp == '1234':
#                 print('Login Successful')
#                 break
#             else:
#                 print('Incorrect OTP')
#         else:
#             print('Incorrect password')

# no = 777
# while True:
#     answer = input('Guess: ')
#     if int(answer) == no:
#         print('Correct answer')
#         break
#     else:
#         print('Try again')

# Print multiplication table of 2
# i = 1
# while i <13:
#     print(f'2 x {i} = {2*i}')
#     i += 1


# c0 = int(input('Enter a number: '))
# steps = 0
# while c0 != 1:
#     if c0 % 2 == 0:
#         c0 = c0 // 2
#     else:
#         c0 = 3 * c0 + 1
#     print(c0)
#     steps +=1
# print(f'Number of steps = {steps}')

# Find number of similar characters in a string

# a = 'Mississippi'
# b = len(a)
# i = 0
# c = 0
# while i < b:
#     if a[i] == 'p':
#         c += 1
#     i += 1
# print(f'Number of "p" in {a} = {c}')


##Find all prime numbers from 1 to 100

# a = 2
# i = 2
# c = 0
# while a < 100:
#     print(a)
#     while i < a:
#         if a % i == 0:
#             break
#         i += 1
#     print(a)
#     a +=1


# Remove dupes from list1 and create a new list2
# list1 = [3,6,2,1,4,3,6,4,3,7]
# list2 = []
# for i in list1:
#     if i in list2:
#         continue
#     list2.append(i)
# print(list2)

# Sort the numbers in a list in descending order
# Bubble sort technique - Swap the values between two variables or two positions in a list.

# list1 = [1,2,5,6,7]
# for j in list1:
#     for i in range(len(list1)-1):
#         if list1[i] < list1[i+1]:
#             list1[i+1], list1[i] = list1[i], list1[i+1]
# print(list1)

# If input is AAbb, output should be "AAAAbbbb" - each character to be printed twice
# a = 'AAbb'
# for i in a:
#     print(i*2,end='')


# Find number of instances 'hi' is present in a word

# a = 'abcihhi hohi'
# c = 0
# for i in range(len(a)):
#     if a[i] == 'h' and a[i + 1] == 'i':
#         c += 1
# print(c)

# Find number of times 'cat' and dog' in a string and return 'True' if their number is same

# a = 'catdogzzzdogcat'
# c = 0
# d = 0
# for i in range(len(a)):
#     if a[i] == 'c' and a[i+1] == 'a' and a[i+2] == 't':
#         c += 1
#     if a[i] == 'd' and a[i+1] == 'o' and a[i+2] == 'g':
#         d += 1
# if c == d:
#     print("True")
# else:
#     print("False")
#
#
# a = 'Hiabc'
# b = 'aBc'
#
# a.lower()
# b.lower()
#
# print(a)
# print(b)
#

# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0
#
# ls = [1,2,3,4,5,6,7,8,9,10]
# c = 0
# for i in ls:
#     if i%2 == 0:
#         c +=1
# print(c)
#
#
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
#
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8

# ls = [7,2,10,9]
# for i in range(len(ls)-1):
#     if ls[i] < ls[i+1]:
#         continue
#     else:
#         ls[i+1],ls[i] = ls[i],ls[i+1]
# print(ls)
# print(ls[len(ls)-1]-ls[0])

#Open file, read, process, add processed data
#
# import csv
# with open('data.csv','r') as f:
#     x = csv.DictReader(f)
#     with open('data.csv','w',newline='') as file:
#         for i in x:
#             price, quantity = i.get('price'), i.get('quantity')
#             total_price = int(price)* int(quantity)
#             a = csv.DictWriter(file,['name','price','quantity','total_price'])
#             a.writerow({
#                 'name':i['name'],
#                 'price':i['price'],
#                 'quantity': i['quantity'],
#                 'total_price': str(total_price)
#             })






