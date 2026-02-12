num = int(input("enter how many number: "))
aray = []

for i in range(num):
    aray.append(int(input(f"enter a number {i+1}:")))
print("\n the number that need top arrange:", aray)

arrange = 1
for i in range(num - 1):
    print(f"itiration {i+1}:")
    for j in range(num - i - 1):
        if aray[j] < aray[j+1]:

            aray[j], aray[j+1] = aray[j+1], aray[j]
            print(f"arrange {arrange}, number {aray}")
            arrange += 1

print("\n arrange number:", aray)