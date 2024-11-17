days_in_months = {
    "january":31,
    "february":28,
    "march":31,
    "april":30,
    "may":31,
    "june":30,
    "july":31,
    "august":31,
    "september":30,
    "october":31,
    "november":30,
    "december":31
}

m = input("Enter name of month: ")
print("There are", days_in_months[m], "days in", m)

print("Months in alphabetical order are:", sorted(days_in_months))

print("Months with 31 days:")
for i in days_in_months:
    if days_in_months[i] == 31:
        print(i, end=" ")