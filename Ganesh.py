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


##Find if a number is prime or not


