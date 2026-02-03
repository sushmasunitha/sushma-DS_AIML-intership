# Ask for the user's name
name = input("What is your name? ")

# Ask for the user's current age
current_age = input("How old are you right now? ")

# Convert age to an integer
current_age = int(current_age)

# Calculate age in 2030 (2026 → 2030 = 4 years)
age_in_2030 = current_age + 4

# Output the result
print(f"Hey {name}, you will be {age_in_2030} years old in 2030!")
