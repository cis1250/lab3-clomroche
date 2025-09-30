#!/usr/bin/env python3

# Fibonacci Sequence Exercise

# Function to calculate the Fibonacci number
def fibonacci(depth):
    if depth == 0:
        return 0
    if depth == 1:
        return 1
    else:
        return fibonacci(depth - 1) + fibonacci(depth - 2)

# Loop until the user inputs a valid, positive integer
while(True):
  depth = input("Enter your desired depth: ")
  if depth.lstrip('-').isdigit() and int(depth) >= 0:
    depth = int(depth)
    break
  else:
    print("Invalid Input")

# Actually print everything out
counter = 0
while(counter<=depth):
  print(fibonacci(counter), end = " ")
  counter = counter + 1
