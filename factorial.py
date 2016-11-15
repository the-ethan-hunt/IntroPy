#Finding factorial of a number
num=input("enter a number")
num=int(num)
factorial=1
if num<0:
    print("Sorry,the factorial of this number does not exist. Try another number!")
elif num == 0:
        print(" The factorial of zero is 1")
else:
            for i in range(1,num+1):
                factorial=factorial*i
                print("The factorial of" ,num,"is",factorial)
    