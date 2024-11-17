d1 = eval(input("Enter first dictionary: "))
d2 = eval(input("Enter second dictionary: "))

print("First dictionary: ", d1)
print("Second dictionary: ", d2)


print("overlapping keys in the two dictionaries are:", end=' ')
for i in d1:
    if i in d2:
        print(i, end=' ')