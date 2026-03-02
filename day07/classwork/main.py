#დავალება1
#type() ფუნქცია აბრუნებს იმ ტიპს,რომელსაც გადავცემტ არგუმენტად.
#int
print(type(5))
#float
print(type(3,14))
#str 
print(type("hello"))
#bool
print(type(True))
#დავალება2
name = "anna"
surname = "gvianishvili"
age = 16

#დავალება4
num1 = float(input("enter number 1: "))
num2 = float(input("enter number 2: "))
num3 = float(input("enrer number 3: "))
num4 = float(input("enter number 3: "))
num5 = float(input("enter number 5: "))
sum_numbers = num1 + num2 + num3 + num4 + num5
average = sum_numbers / 5
print("avarage:")
#დავალება3
num1 = float(input("enter first desimal number: "))
num2 = float(input("enter second decimal number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
print("addition")
print("subtraction")
print("multiplication")
print("division")
#დავალება5
celsius = float(input("enter temperature in celsius"))
fahrenheit = celsius * 9/5 + 32
print("temperature in fahrenheit:")
#დავალება6
fahrenheit = float(input("enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("temperature in celsius: ")
