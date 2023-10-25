"""
 Author: Dilbekkhon
 Date: 25-10-2023
 Name: Long arithmetics
"""


import random

def generate_100_digit_number():
    
    return random.randint(10**(99), 10**(100)-1)


a = int(input("Enter number A: "))

b = generate_100_digit_number()

result = b / a

print(f"Generated 100-digit number: {b}")
print(f"Result of the division ({b} / {a}): {result}")
