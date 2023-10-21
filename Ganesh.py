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


income = float(input("What is your income? "))
if income < 85528:
    tax = (income*0.18) - 555.98
    if tax <=0:
        print("Zero tax")
    else:
    print(f"The tax is : {round(tax, 0)} Thalers")
else:
    tax = 14839.02 + ((85528 - income) * 0.32)
    if tax <= 0:
    print("The tax is 0.0 Thalers")
    else:
    print(f"The tax is : {round(tax,0)} Thalers")

# a='111222'
# b='Yay'
# c=len(a)//2
# print(a[:c]+b+a[c:])

# a = input('Enter the year to check: ')
# if int(a) < 1582:
#     print(f'{a} is not within the Gregorian Calendar period')
# elif int(a) % 4 == 0 + int(a) % 100 != 0:
#     print("Leap year")
# elif int(a) % 400 != 0:
#     print("Common year")
# else:
#     print("Leap year")



