D1 = eval(input("Enter a dictionary D1: "))
print("D1 =", D1) 

D2 = {}
for i in D1:
      num = sum(D1[i])
      D2[i] = num
print(D2)