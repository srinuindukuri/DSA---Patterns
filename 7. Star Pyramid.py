num = int(input("Enter the Number: "))

for i in range(0, num):
    for j in range(0, num-i-1):  # Printing spaces
        print(" ", end="")
    for j in range(0, 2*i+1):    # Printing stars
        print("*", end="")
    print()
