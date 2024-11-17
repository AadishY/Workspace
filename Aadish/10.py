# Dictionary to check
D1 = {'a': 10, 'b': 20, 'c': 10}
D2 = {'a': 10, 'b': 20, 'c': 30}

# Check for D1
print("Checking D1:")
values = list(D1.values())
if len(values) != len(set(values)):
    print("Two or more keys have the same value.")
else:
    print("No keys have the same values.")

# Check for D2
print("\nChecking D2:")
values = list(D2.values())
if len(values) != len(set(values)):
    print("Two or more keys have the same value.")
else:
    print("No keys have the same values.")
