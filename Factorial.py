def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n - 1)
x=int(input("Please enter a number to calculate factorial: "))
result=factorial(x)
print(result)
