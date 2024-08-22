#check if a number is odd or even
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")


#generate multiplication table
num = int(input("Enter a number to generate its multiplication table: "))

print(f"Multiplication Table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#Find largest number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: ")) 

if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}.")

#Count number of vowels
string = input("Enter a string: ")
count = 0
vowels = "aeiouAEIOU"

for char in string:
    if char in vowels:
        count += 1

print(f"The number of vowels in the string is {count}.")
