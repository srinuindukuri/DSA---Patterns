row = int(input("Enter the value: "))
k = 1

for i in range(row+1):
    for j in range(i+1):
        print(k, end='')
        k = k+1
    print()
