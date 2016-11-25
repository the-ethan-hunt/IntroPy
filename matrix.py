#To find the sum of two matrices
print("Enter the value of row:")
x=int(input())
print("Enter the value of column:")
y=int(input())
a=[[0 for row in range(0,x)] for col in range(0,y)]
b=[[0 for row in range(0,x)] for col in range(0,y)]
result=[[0 for row in range(0,x)] for col in range(0,y)]
print("Enter the elements of first matrix:")
for i in range(x):
    for j in range(y):
        a[i][j]=int(input())
print("Enter the elements of second matrix:")
for i in range(x):
    for j in range(y):
        b[i][j]=int(input())
print
print("Elements of first matrix is:")
for row in a:
    print(row)
print
print("Elements of second matrix is:")
for row in b:
    print(row)
#iterate throguh rows
for i in range(len(a)):
    #iterate through columns
    for j in range(len(a[0])):
        result[i][j]=a[i][j]+b[i][j]

print
#print the sum of the two matrix
print("Sum of first two matrix is:")
for r in result:
    print(r)