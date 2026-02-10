n = int(input("enter no.of student marks:"))
m = [0] * n
for i in range(n):
    m[i] = int(input(f"enter marks of student in subject {i + 1}:"))
num=int(input("Enter your registration number last digit: "))

if num%2==0:
    for i in range(n):
        m[i] -= 1
else:
    for i in range(n):
        m[i] += 1
print("marks after updation:",m)
validstudents = 0
failstudents = 0
for i in range(n):
    if m[i] < 0 or m[i] > 100:
        print(m[i], "->invalid")
    else:
        validstudents += 1
        if m[i] >= 90:
            print(m[i], "->excellent")
        elif m[i] >= 75:
            print(m[i], "->verygood")
        elif m[i] >= 60:
            print(m[i], "->good")
        elif m[i] >= 40:
            print(m[i], "->average")
        else:
            failstudents += 1
            print(m[i], "->fail")
print("total valid students are :", validstudents)
print("total fail students are:", failstudents)