
row = int(input("Enter the value: "))
for i in range(row):
    for j in range(row-i-1):
        print(chr(j+65), end='')
    print()
