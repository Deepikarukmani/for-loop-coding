#Nested for loop syntax:
for i in range(0,5):
    for j in range(1,3):
        print(j, "apple")

#Nested for loop syntax:
for i in range(1,3):
    print("Week:",i)
    for j in range(1,4):
        print("Day:",j)


#Print the square pattern with the number '1' in R*R form based on the given integer R.
# Sample Input :
# 5
# Sample Output :
# 11111
# 11111
# 11111
# 11111
# 11111
n= int(input())
for i in range(n):
        print("1" *n)

#pattern program:
for i in range(1,5):
    print()
    for j in range(1, i+1):
        print(j,end="")

#pattern program:
for i in range(1,5):
    print()
    for j in range(1, i+1):
        print("* " ,end="")

# Print the half pyramid pattern based on the given integer R.# Sample Input : 5
# Sample Output :
# 1
# 12
# 123
# 1234
# 12345
n = int(input())
for i in range(0,n+1):
    print()
    for j in range(1,i+1):
        print(j,end="")


# Print the rectangle using stars with R rows and C columns.
# Sample Input :
# 3 5
# Sample Output :
# * * * * *
# * * * * *
# * * * * *
n = int(input())
for i in range(n-2):
    for j in range(n):
        print("*", end=" ")
    print()




