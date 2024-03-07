# Pattern 2 - Right angle triangle

n = int(input("Enter row number:\n"))

for i in range(0, n):
    for j in range(i+1):
        print("* ", end='')
    print()
