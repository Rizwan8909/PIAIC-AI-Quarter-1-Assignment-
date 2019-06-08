a = int(input("Please Enter Principle Amount: "))
b = float(input("Please Enter rate of interest in %: "))
c = int(input("Enter Number of years for Investment: "))
e = 0
f = a * b
while e < c:
    f += f * b 
    e += 1
print(f)