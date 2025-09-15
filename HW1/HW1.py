row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

nestedList = []

for x in range(row):
    print(f"\nRow {x+1}")
    innerList = []
    for y in range(col):
        num = float(input(f"Enter number {y+1}: "))
        innerList.append(num)
    nestedList.append(innerList)

print("\nThe numbers are:\n")
for x in range(len(nestedList)):
    for y in range(len(nestedList[x])):
        print(nestedList[x][y], end=" ")
    print()

search = float(input("\nSearch: "))

positions = {}

for x in range(len(nestedList)):
    for y in range(len(nestedList[x])):
        val = nestedList[x][y]
        if val not in positions:
            positions[val] = []
        positions[val].append((x, y))  # (row, col)

if search in positions:
    results = []
    for pos in positions[search]:
        rowIndex = pos[0]
        colIndex = pos[1]
        results.append(f"Row {rowIndex}, Col {colIndex}")
    print(f"Number {search} found at " + " and ".join(results))
else:
    print("Number not found.")
