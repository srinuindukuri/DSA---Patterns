def BinaryNumber(row):
    start = 1

    for i in range(row):
        for j in range(0, i+1):
            if j % 2 == 0:
                print(1, end="")
            else:
                print(0, end="")
        start = start - 1      # Flips 1 -> 0 and 0 -> 1
        print()


n = int(input("Enter the value: "))
BinaryNumber(n)
