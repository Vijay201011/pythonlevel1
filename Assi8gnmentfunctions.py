"""1. Write a Python function to find the maximum of three numbers.


2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20

3. Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336


4. Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"  """


def find_max_of_three():
   
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    max_num = max(num1, num2, num3)
    print("The maximum number is:", max_num)




sum_of_list=input(int("type numbers"))
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)


multiply_of_list=input(int("type numbers"))
def multiply_of_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    print(result)


def reverse_string(s):
    return s[::-1]
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)