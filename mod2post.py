# Make a list for employee management that can initialize the list and store data.
employees = []

name = input("Enter employee name: ")
hire_date = input("Enter hire date (MM/DD/YYYY): ")
phone_number = input("Enter phone number: ")

employees.append({
    "Name": name,
    "Hire Date": hire_date,
    "Phone Number": phone_number,
})

print("\nEmployee List")
print("-------------")
for employee in employees:
    print(f"Name: {employee['Name']}")
    print(f"Hire Date: {employee['Hire Date']}")
    print(f"Phone Number: {employee['Phone Number']}")
