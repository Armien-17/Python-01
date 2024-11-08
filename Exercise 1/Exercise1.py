# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input ("Please enter your name:")
# TODO: Ask the user for their age and store it in a variable
age = input ("Please enter your age:")
# TODO: Print a greeting using the name and age variables
print("Yo"+ " " + name+" "+ "age "+age)
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length= int(input("enter the length of a rectangle:"))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width=int(input("enter the width of a rectangle:"))
# TODO: Calculate the area of the rectangle
area= length * width
# TODO: Print the result
print(area)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
temperature= float(input ("please enter the temperature in celcius"))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
fahrenheit=(temperature * 9/5) +32
# TODO: Print the result rounded to two decimal places
print("the celcius in Fehrenheit is"+  str(round(fahrenheit, 2)))
