class math_method:
    def prime_number(self,n):
        is_prime=True
        for i in range(2,int((n**0.5)+1)):
            if n % i ==0:
                is_prime=False
                break
        if is_prime and n>1:
            print(f"{n} is a prime number")
        else:
            print(f"{n} is not a prime number")
    def factorial (self,x):
        if x<0:
            print("Factorial is only defined for non-negative integers.")
        elif x==0 or x==1:
            return 1
        else:
            return x*self.factorial(x - 1)
        

num= int(input("Please enter a number to check if it is prime number or calculate factorial: "))
p=math_method()
p.prime_number(num)
p.factorial(num)
print(f"The factorial of {num} is {p.factorial(num)}")
