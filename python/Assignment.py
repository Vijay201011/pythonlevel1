#Write a Python program that accepts a word from the user(take input from user)and reverses it.. after  reverseingcheck if previous word and original word same same. if two words are same then print its palindrom else print its palindrom0.
#Write a python program take input from user a number. if number is divisible by 3 and divisible by 5 then print its multiple of both 3 andn5 else its not multiple of bith 3 and 5.
#Hint : number % 3==0 and same for 5)
#Write a program take input from user his country. if country is equal to india print its good elif country is equal to UK then print its excellent else print its bad.

word=input("write a word")
word1=word[::-1]
if word1==word:
    print("The word is palindrom")
else:
    print("The word is not palindrom")

number=input("enter a number")
if number%3==0 and number%5==0:
    print("The number is a multiple of 3 and 5")
else:
    print("The number is not a multiple of 3 and 5")

country=input("enter a country")
if country=="India":
    print("It's good")
elif country=="UK":
    print("It's excellent")
else:
    print("It's not good")
