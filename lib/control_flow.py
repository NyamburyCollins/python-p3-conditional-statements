#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username.lower() == "admin" or username == "ADMIN") and password == "12345":
    return "Access granted":
   else :
    return "Access denied"
  

def hows_the_weather(temperature):
    # your code here
  if temperature < 40:
    return = "brisk"
   else if temperature >= 40:
    return = "a little chilly"
    else if temperature <= 65:
        return = "Its chilly outside"
   else if temperature > 85 
    return = "too dang hot"
   else 
    return = "perfect out there!"
  
  return `It's perfect out there!`



def fizzbuzz(num):
    # your code here
    if num % 3 === 0 and num % 5 === 0 :
    return "FizzBuzz"
   else if num % 3 === 0:
    return "Fizz"
   else if num % 5 === 0: 
    return "Buzz"
   else 
    return num
  



def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:  # Check for division by zero
            return num1 / num2
        else:
            print("Division by zero is not allowed!")
            return None
    else:
        print("Invalid operation!")
        return None
