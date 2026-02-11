print("choose the operation.")

print("1.add")
print("2.minus")
print("3.multiply")
print("4.devision")

operation = input("enter what operation: ")

if operation == "1":
    num1 = input("enter a first number: ")
    num2 = input("enter a second number: ")
    sum = int(num1) + int(num2)
    print("the answer is: ", sum)
elif operation == "2":
    num1 = input("enter a first number: ")
    num2 = input("enter a second number: ")
    sum = int(num1) - int(num2)
    print("the answer is: ", sum)
elif operation == "3":
    num1 = input("enter a first number: ")
    num2 = input("enter a second number: ")
    sum = int(num1) * int(num2)
    print("the answer is: ", sum)
elif operation == "4":
    num1 = input("enter a first number: ")
    num2 = input("enter a second number: ")
    sum = int(num1) / int(num2)
    print("the answer is: ", sum)
else:
    print("invaled")

