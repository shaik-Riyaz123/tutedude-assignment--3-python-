def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a number: "))
fact = factorial(num)
print(f"\nFactorial of {num} is: {fact}")
