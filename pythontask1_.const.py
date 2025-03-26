# Q-1. Check if a given number is positive, negative, or zero.
num = int(input("Enter the number: "))
if num > 0:
    print('The number is positive')
elif num == 0:
    print('Zero is neither positive nor negative')
else:
    print('The number is negative')

# Q-2. Check if a number is even or odd.
num = int(input("Enter the number: "))
if num % 2 == 0:
    print('It is an even number')
else:
    print('It is an odd number')

# Q-3. Check if a person is eligible to vote.
age = int(input("Enter the age: "))
if age < 18:
    print('You cannot vote')
else:
    print('You can vote')

# Q-4. Find the greatest of two numbers.
digit1 = int(input("Enter number 1: "))
digit2 = int(input("Enter number 2: "))
if digit1 > digit2:
    print('Number 1 is the greatest')
elif digit1 < digit2:
    print('Number 2 is the greatest')
else:
    print('Both numbers are equal')

# Q-5. Print "Pass" if a student scores more than 40 marks, otherwise print "Fail."
marks = int(input("Enter the marks: "))
if marks >= 40:
    print('Pass')
else:
    print('Fail')

# Q-6. Display the day of the week based on a number (1-7).
day = int(input("Enter a day number (1-7): "))
days_of_week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 
                5: "Friday", 6: "Saturday", 7: "Sunday"}

print(days_of_week.get(day, "Invalid input! Enter a number between 1 and 7."))

# Q-7. Implement a simple calculator.
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operator = input("Choose an operation (+, -, *, /): ")

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2 if number2 != 0 else "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print("Result:", result)

# Q-8. Display the month name based on the month number (1-12).
month = int(input("Enter the month number (1-12): "))
months_of_year = {1: "January", 2: "February", 3: "March", 4: "April", 
                  5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 
                  10: "October", 11: "November", 12: "December"}

print(months_of_year.get(month, "Invalid input! Enter a number between 1 and 12."))

# Q-9. Find the greatest of three numbers.
val1 = int(input("Enter the first number: "))
val2 = int(input("Enter the second number: "))
val3 = int(input("Enter the third number: "))

if val1 >= val2 and val1 >= val3:
    print("The greatest number is:", val1)
elif val2 >= val1 and val2 >= val3:
    print("The greatest number is:", val2)
else:
    print("The greatest number is:", val3)

# Q-10. Check if a year is a leap year.
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Q-11. Classify a character as a vowel, consonant, or neither.
char = input("Enter a character: ").lower()
if len(char) != 1 or not char.isalpha():
    print("Invalid input! Please enter a single alphabetic character.")
elif char in 'aeiou':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

# Q-12. Calculate the grade of a student based on their marks.
marks = int(input("Enter the marks: "))
if 90 <= marks <= 100:
    print('Grade A')
elif 80 <= marks < 90:
    print('Grade B')
elif 70 <= marks < 80:
    print('Grade C')
else:
    print('Fail')

# Q-13. Check if three side lengths form a valid triangle.
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if a + b > c and a + c > b and b + c > a:
    print("It forms a valid triangle")
else:
    print("The triangle is invalid")


#Program to find reverse of a number
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10 
    reverse = (reverse * 10) + digit 
    num = num // 10
print("Reversed number:", reverse)

#program to find sum of digits
number=int(input("Enter a number: "))
sum=0
while number>0:
    digit=number%10
    sum+=digit
    number=number//10
print("Sum of digits:", sum)

#program to find Number to digits
num2=int(input("Enter a number: "))
count=0
while num2>0:
    num2=num2//10
    count+=1
print("Number of digits:", count)

#program to print only digits that are multiples of 3
num = abs(int(input("Enter a number: ")))
result = []
while num > 0:
    digit = num % 10
    if digit % 3 == 0:
        result.append(str(digit))
    num //= 10 
if result:
    print("Digits that are multiples of 3:", ' '.join(result[::-1]))
else:
    print("No digits are multiples of 3.")
 



    