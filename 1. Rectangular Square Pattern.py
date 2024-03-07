# Patterns ---> Nested Loops

# (1) Run the outer loop, count the no.of lines
# (2) Run the inner loop, focus on the columns & connect them somehow to the rows.
# (3) Print the " * " inside the outer loop
# (4) Observe Symmetry [optional]

# Example 1:

# Input: 5

# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# Patter 1 - Rectangular Square Pattern

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

for i in range(rows):
    for j in range(cols):
        print("* ", end=" ")
    print()
