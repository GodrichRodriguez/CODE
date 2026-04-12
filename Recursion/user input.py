def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)
num = int(input("Enter a number: "))
result = sum_numbers(num)
print("the sum of numbers from 1 to", num, "is:", result)