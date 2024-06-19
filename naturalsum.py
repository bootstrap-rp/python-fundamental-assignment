# def naturalsum(n):
#     sum=0
#     if n==1:
#         print(1)
#     else:
#         for i in range(1,n+1):
#             sum=sum+i
#         print(sum)   

# n=int(input("Enter the Number:"))
# naturalsum(n)




def sum(n):
    if n==1:
        return 1
    else:
        return 1+ sum(n)
    
print(sum(8))    