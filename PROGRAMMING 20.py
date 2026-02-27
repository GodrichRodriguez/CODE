def find_largest():
    num1 = int(input("enter a number: "))
    num2 = int(input("enter second number: "))
    num3 = int(input("enter third number: "))

    if num1 >= num2 and num1 >= num3:
        then = ("num1", num1)
    elif num2 >= num1 and num2 >= num3:
        then = ("num2", num2)
    else:
        then = ("num3", num3)
    
    print(f"the number {then[0]} is the largest value of {then[1]}")
    
find_largest()
