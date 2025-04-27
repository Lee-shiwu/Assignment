class math_calculate:
    def factorial(self,n):
        if n<0:
            print("Factorial is only defined for non-negative integers.")
        elif n==0 or n==1:
            return 1
        else:
            return n*math_calculate.factorial(n - 1)
x=int(input("Please enter a number to calculate factorial: "))
result=math_calculate.factorial(x)
if result is None:
    pass
else:
    print(f"Factorial is {result}")
