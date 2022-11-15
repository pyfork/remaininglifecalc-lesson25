# Get current age
age = input("What is your current age?\n")

# Maximum age
max_age = 90

# Remaining life in years
rem_age_in_years = max_age - int(age)
# print(rem_age)

rem_age_in_days = rem_age_in_years * 365

rem_age_in_weeks = rem_age_in_years * 52

rem_age_in_months = rem_age_in_years * 12

print(f"You have {rem_age_in_days} days, {rem_age_in_weeks} weeks, or precisely {rem_age_in_months} months left")

# print(type(int(2.6)))