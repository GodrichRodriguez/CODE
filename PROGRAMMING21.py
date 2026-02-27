mylist = []

print("----menu-----")
print("good morning mga broken !")

while True:
    print("1. show user\n2. add user\n3. update user\n4. delete user\n5. exit")
    user = input("enter og number:")
    match user:
        case '1':
            print(mylist)
        case '2':
            name = input("Enter a username: ")
            mylist.append(name)
        case '3':
            old_name = input("Enter username to update: ")
            if old_name in mylist:
                new_name = input("Enter new username: ")
                index = mylist.index(old_name)
                mylist[index] = new_name
                print("User updated.")
            else:
                print("User not found.")
        case '4':
            name = input("Enter a username to delete: ")
            if name in mylist:
                mylist.remove(name)
                print("User deleted.")
            else:
                print("User not found.")
        case '5':
            print("Exiting......")
            break
        case _:
            print("invalid try again!")

print(mylist)