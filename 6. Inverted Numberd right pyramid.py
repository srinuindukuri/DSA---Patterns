# Print the inverted half pyramid using numbers

rows = int(input("Enter the number of rows: \n"))

for i in range(1, rows+1):
    for j in range(rows, i-1, -1):
        print(rows-j+1, end="")
    print()
