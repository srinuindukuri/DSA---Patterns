# Print the inverted half pyramid using '*'

row = int(input("Enter the number of rows: \n"))

for i in range(1, row+1):
    for i in range(row, i-1, -1):
        print("* ", end='')
    print()
