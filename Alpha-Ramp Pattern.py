row = int(input("Enter the value: "))
for i in range(row):
    for j in range(i+1):
        print(chr(i+65), end='')
    print()
