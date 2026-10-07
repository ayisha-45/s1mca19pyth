n=int(input("Enter number of n Terms: "))
if n<=0:
    print("Fibonacci  series upto ",n," is not defined")
else:
    first=0
    second=1
    print("The first ",n," numbers in the fibonacci series = ")
    if n==1:
        print(first,end="")
    elif n==2:
        print(first,",",second,end="")
    else:
        print(first,",",second,end=",")
    for i in range(2,n):
        fib=first+second
        first=second
        second=fib
        if i==n-1:
            print(fib,end="")
        else:
                print(fib,end=",")
