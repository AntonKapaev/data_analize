def summa(a, b):
    c = a + b
    print(c)


def summa1(a, b):
    c = a + b
    return c


summa(4, 3)
d = summa1(4, 3)
print(d)


s = "hello"
s.replace("h", "H")
print(s)
a = [3, 4, 5.5, "Hello"]
a.append(9)
print(a)
a[0] = 6
print(a)
d = {112: "Иванов", 113: "Сидоров"}
d[114] = "Никифоров"
print(d[112])
print(d)
f = 2
if f % 2 == 0:
    print("четное")
    if f % 3 == 1:
        print("3")
elif f % 4 == 0:
    print("4")
else:
    print("нечетное")

for i in range(1, 6, 2):
    print(i)

i = 1
while i <= 5:
    print(i)
    i = i + 1

a = [3, 2, 5, 1, 7]
min = a[0]
for i in range(1, len(a)):
    if a[i] < min:
        min = a[i]
print(min)

b = 0
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        b = b + 1
print(b)

max = 0
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        b = a[i] + a[j]
        if b > max:
            max = b
print(max)