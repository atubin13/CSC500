# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.

# Input: Ask the user for the number of years.

# Logic: * An outer loop will iterate once for each year.

# An inner loop will iterate twelve times, once for each month.

# Each iteration of the inner loop will ask the user for the inches of rainfall for that specific month.

# Output: Display the total number of months, the total inches of rainfall, and the average rainfall per month for the
# entire period.

num_years = int(input("Enter the number of years: "))
total_rainfall = 0.0

for year in range(1, num_years + 1):
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for Year {year}, Month {month}: "))
        total_rainfall += rainfall

total_months = num_years * 12
average_rainfall = total_rainfall / total_months if total_months > 0 else 0.0

print(f"\nTotal number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")