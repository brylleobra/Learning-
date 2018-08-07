#Recursion method of Fibonacci Sequence

def Fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return Fib(x-1)+Fib(x-2)


Input=int(input("enter number:"))

for numIn in range(0,Input):
    print(Fib(numIn))
