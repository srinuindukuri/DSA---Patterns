
num = int(input("Enter the number of rows: \n"))

for i in range(num):
    for j in range(i):
        print(" ", end="")
    for j in range(2*num-(2*i+1)):
        print("*", end="")
    print()
