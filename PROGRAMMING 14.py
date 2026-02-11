# Take input from the user
n = int(input("Enter a number: "))

# Check if the number is even
if n % 2 == 0:
    print("Invalid")
else:
    # Create a list of odd numbers from 1 to n
    odd_numbers = list(range(1, n+1, 2))
    
    # Calculate the sum of odd numbers
    sum_odd = sum(odd_numbers)
    
    # Print the list and the sum
    print("Odd numbers:", odd_numbers)
    print("Sum:", sum_odd)

