
a = input("Enter Text: ")
c = a.lower()
d = 0
f = 0
for x in c:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        d += 1
    else:
        f += 1
print("Vowels: ",d)
print("Consonants: ",f)