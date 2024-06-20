def sumd(n):
    if n==0:
        return 0
    else:
        return n%10 + sumd(n//10)
    
n=int(input("Enter the Number:"))
print(sumd(n))