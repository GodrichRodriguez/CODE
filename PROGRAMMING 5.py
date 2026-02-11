# x = 3
# if x > 5:
#     print("Hello")

# num = int(input("Enter number: "))

# if num >= 10:
#     if num >= 50:
#         print("large")
#     else:
#         print("med")
# else:
#     print("small")
print("choose what subject that u need to compute ur final grade")

print("1.DSA")
print("2.CP2")
print("3.AP")
print("4.DM")
print("5.STS")
print("6.UTS")
print("7.ROTC/CWTS")
print("8.PATHFIT")

grade = input("Enter the number what subject: ")

if grade == "1":
    num1 = input("enter ur grade in midterm: ")
    num2 = input("enter ur grade in final term: ")
    sum = int(num1) + int(num2)
    final = sum / 2
    print("ur final grade in DSA is: ", final)
elif grade == "2":
    num1 = input("enter ur grade in midterm: ")
    num2 = input("enter ur grade in final term: ")
    sum = int(num1) + int(num2)
    final = sum / 2
    print("ur final grade in CP2 is: ", final)
elif grade == "3":
    num1 = input("enter ur grade in midterm: ")
    num2 = input("enter ur grade in final term: ")
    sum = int(num1) + int(num2)
    final = sum / 2
    print("ur final grade in AP is: ", final)
elif grade == "4":
    num1 = input("enter ur grade in midterm: ")
    num2 = input("enter ur grade in final term: ")
    sum = int(num1) + int(num2)
    final = sum / 2
    print("ur final grade in DM is: ", final)
elif grade == "5":
    num1 = input("enter ur grade in midterm: ")
    num2 = input("enter ur grade in final term: ")
    sum = int(num1) + int(num2)
    final = sum / 2
    print("ur final grade in STS is: ", final)
elif grade == "6":
    num1 = input("enter ur grade in midterm: ")
    num2 = input("enter ur grade in final term: ")
    sum = int(num1) + int(num2)
    final = sum / 2
    print("ur final grade in UTS is: ", final)
elif grade == "7":
    num1 = input("enter ur grade in midterm: ")
    num2 = input("enter ur grade in final term: ")
    sum = int(num1) + int(num2)
    final = sum / 2
    print("ur final grade in ROTC/CWTS is: ", final)
elif grade == "8":
    num1 = input("enter ur grade in midterm: ")
    num2 = input("enter ur grade in final term: ")
    sum = int(num1) + int(num2)
    final = sum / 2
    print("ur final grade in PATHFIT is: ", final)
else:
    print("invaled")
