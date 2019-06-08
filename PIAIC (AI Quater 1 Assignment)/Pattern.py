//Pattern1
f = 1
i = 0
while i <= 9:
    d = '*'
    print(d * f)
    f += 1
    i += 1

//Pattern2
i = 6
d = 0
for x in range(1,i):
    for y in range(1, x + 1):
        print (y , end = " ")
    print(" ")
for r in range(4,d,-1):
    for c in range(1, r + 1):
        print (c , end = " ")
    print(" ")

//Pattern3
for i in range(10):
    for f in range(i):
        print(i, end = ' ')
    print(" ")