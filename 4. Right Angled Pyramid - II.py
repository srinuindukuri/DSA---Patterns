# Pattern 4 - Right Angled Number Pyramid - II

rows = int(input("Enter number of rows: "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print(" ")
