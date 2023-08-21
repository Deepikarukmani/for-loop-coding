#Nested for loop syntax:
for i in range(0,5):
    for j in range(1,3):
        print(j, "apple")

#Nested for loop syntax:
for i in range(1,3):
    print("Week:",i)
    for j in range(1,4):
        print("Day:",j)

#pattern program:
n= int(input())
for i in range(n):
        print("1" *n)

#pattern program:
for i in range(1,5):
    print()
    for j in range(1, i+1):
        print(j,end="")
