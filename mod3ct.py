# Write a program that calculates the total cost of a restaurant meal based on user input
# Input: Prompt the user to enter the charge for the food.
# Calculations: Calculate an 18% tip and 7% sales tax based on the food charge

food_charge = float(input("Enter the food charge: "))
tip = food_charge * 0.18
sales_tax = food_charge * 0.07
print(f"Food charge: ${food_charge:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${food_charge + tip + sales_tax:.2f}")
