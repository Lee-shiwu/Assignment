class Factorial:
    @staticmethod
    def factorial(num1):
        result = 1
        for i in range(1, num1 + 1):
            result *= i
        return result

    @staticmethod
    def check_Prime(num1):
        if num1 < 2:
            return False
        for i in range(2, int(num1 ** 0.5) + 1):
            if num1 % i == 0:
                return False
        return True

    @staticmethod
    def display(num1):
        print("Factorial of", num1, "is", Factorial.factorial(num1))
        if Factorial.check_Prime(num1):
            print(f"{num1} is a prime number。")
        else:
            print(f"{num1} is not a prime number。")
number=int(input("Please enter a number to check whether it is prime and output the factorial: "))
Factorial.display(number)