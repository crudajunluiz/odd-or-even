# Even or Odd Detector

num1 = int(input("Enter a number: ")) # Asks for an input to detect if it is an odd or even number.

if num1 % 2 == 0: # Checks if it is even
  print(f"{num1} is an even number") # Inputs the message if the number was even
else: # Checks if it is not even
  print(f"{num1} is an odd number") # Inputs the message if the number was odd
