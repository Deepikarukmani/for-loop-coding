#for loop syntax:
for i in "apple":
    print(i)

#for loop syntax:
for python in "coding":
    print(python)

#for loop syntax:
for i in range(5):
    print(i)


#pattern program
a = [1, 2, 3, 4, 5]
for i in a:
    print(i *" *")


#for loop using "2" tables:
for i in range(1, 11):
    print(i,"x2 =", i*2)


#for loop using "3" tables:
for i in range(1, 21):
    print(i, "x3 =", i*3)


# Find even
a = [1,2,3,4,5,6,7,8,9]
for i in a:
    if i%2 ==0:
        print(i)


#get the input from user between numbersa A and B: print the number between A and B:
a = int(input())
b = int(input())
for i in range(a,b):
    print(i)


#print even numbers using for loop:
for i in range(0,15):
    if i%2==0:
        print(i)


#count the numbers of odd numbers between 1 to 10 using for loop:
count=0
for i in range(1,10):
    if i%2!=0:
        count=+1
print(count)


#count the numbers of even numbers and odd numbers between 1 to 10 using for loop:
even_count=0
odd_count=0
for i in range(1,10):
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print(even_count)
print(odd_count)


#count the numbers which are divisible by 3 and 5 between the range of 1 to 100 using for loop:
count=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        count=count+1
print(count)


#write a program to compute the sum of first 5 natural numbers:
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)


# write a program to find its cube :
for i in range(1,6):
    print("Number is:", i, "the cube of the", i, "is :", i ** 3)
    

#write a program to read 10 numbers from the keyboard and to find the sum and average
a = []
for i in range(5):
    num=int(input())
    a.append(num)
print(a)
sum=0
for i in a:
    sum=sum+i
print(sum)
average= sum/i
print(average)












# Find even using range function
for i in range(1, 11):
    if i%2 ==0:
        print(i)
