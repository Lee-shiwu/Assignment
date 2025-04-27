class Prime:
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
        

num= int(input("Please enter a number to check if it is prime number: "))
p=Prime()
p.prime_number(num)
