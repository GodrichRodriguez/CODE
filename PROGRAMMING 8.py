x = 300

def number():

    num1 = int(input("enter a number: "))
    num2 = int(input("enter second number: "))
    num3 = int(input("enter a third number: "))

    largest = max(num1, num2, num3,)

    if largest <= x or largest >= x:

        print(f"the closest number of 300 is", largest)
        
number()