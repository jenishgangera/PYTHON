# Fundamental Booster - Personal Data Collector

print("Welcome to the Interactive Personal Data Collector!")
print()

# Collect Information
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))

print()
print("Thank you! Here is the information we collected:")
print()

# Display value, data type and memory address
print("Name:", name)
print("Type:", type(name))
print("Memory Address:", id(name))
print()

print("Age:", age)
print("Type:", type(age))
print("Memory Address:", id(age))
print()

print("Height:", height)
print("Type:", type(height))
print("Memory Address:", id(height))
print()

print("Favourite Number:", favourite_number)
print("Type:", type(favourite_number))
print("Memory Address:", id(favourite_number))
print()

# Calculate Birth Year
from datetime import datetime

current_year = datetime.now().year
birth_year = current_year - age

print("Your birth year is approximately:", birth_year)
print()

# Exit Message
print("Thank you for using the Personal Data Collector. Goodbye!")