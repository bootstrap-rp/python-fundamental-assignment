def fact(n):
    fact=1
    if n==0:
        print("The factorial of 0 is 1")
    elif n<0:
        print("The factorial is not possible for the negative numbers.")

    else:
        for i in range(1,n+1):
            fact=fact*i
        print("The factorial of ",n,"is",fact)

n=int(input("Enter the number:"))
fact(n)            


