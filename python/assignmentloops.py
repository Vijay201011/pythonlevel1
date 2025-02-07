#1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
#2.  Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.
#3. Write a Python program to check whether an alphabet is a vowel or consonant.

#-----------------------------------------
for i in range(100, 400):
    s=str(i) # beause string has index value and with that we get very number seperately and check seperately if its is divisible by 2 
    if(int(s[0]) %2==0 and int(s[1]) %2==0 and int(s[2]) %2==0):
        print(s)

#-----------------------------------
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)


#-------------------------------------------
alphabet = input("Enter an alphabet: ").lower()
if alphabet.isalpha() and len(alphabet) == 1:
   
    if alphabet in 'aeiou':
        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
else:
    print("Please enter a valid single alphabet.")



"""Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant."""
#-------------------------------------------------------------
#4. Write a Python program to check if a triangle is equilateral, isosceles or scalene.


side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))


if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("The sides of a triangle must be positive numbers.")
else:
    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    # Check if two sides are equal
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is Isosceles.")
    
    else:
        print("The triangle is Scalene.")
"""Take 3 input from user and apply if then on it.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:

Input lengths of the triangle sides:                                    
x: 6                                                                    
y: 8                                                                    
z: 12                                                                   
Scalene triangle """ 