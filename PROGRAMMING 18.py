while True:
    password = input("enter a password: ")

    letter = False
    number = False

    for char in password:
        if char.isalpha():
            letter = True
        if char.isdigit():
            number = True
   
            
    if letter and number and len(password) >= 8:
        print("password accepted!")
        break
    else:
        print("invaled passwords butangig letter or number blehhh!!!!")
        break

