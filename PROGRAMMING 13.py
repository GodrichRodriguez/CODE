num = int(input("enter a number: "))

if num % 2 == 0:
    print("please enter a odd number")
else:

    total = 0
    for i in range(1, num+1, 2):
        total += i
    print("the total is", total)


7