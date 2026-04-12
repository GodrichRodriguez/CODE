def factorial(n):
    if n == 1:        # base case
        return 1
    else:
        return n + factorial(n - 1)   # recursive case

num = int(input("Enter a number: "))
print("sum is:", factorial(num))

# 4 + 3 + 2 + 1 = 10