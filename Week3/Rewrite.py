class Factorial:
    @staticmethod
    def factorial(input_number):
        result = 1
        for i in range(1, input_number + 1):
            result *= i
        return result

    @staticmethod
    def check_Prime(check_number):
        if check_number < 2:
            return False
        for i in range(2, int(check_number ** 0.5) + 1):
            if check_number % i == 0:
                return False
        return True

    @staticmethod
    def display(show_number):
        print("Factorial of", show_number, "is", Factorial.factorial(show_number))
        if Factorial.check_Prime(show_number):
            print(f"{show_number} is a prime number。")
        else:
            print(f"{show_number} is not a prime number。")
number=int(input("Please enter a number to check whether it is prime and output the factorial: "))
Factorial.display(number)