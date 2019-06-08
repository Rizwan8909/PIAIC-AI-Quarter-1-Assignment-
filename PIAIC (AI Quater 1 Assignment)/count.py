a = input("Enter Text: ")
e = 0
d = 0
c = 0
f = 0
for x in a:
    if int(ord(x)) >= 65 and int(ord(x)) <= 122:
        e += 1
    elif int(ord(x)) >= 48 and int(ord(x)) <= 57:
        d += 1
    elif x == " ":
        f += 1
    else:
        c += 1
print("Alphabets:          ",e)
print("Numbers:            ",d)
print("Special Characters: ",c)
print("Space:              ",f)