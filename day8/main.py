with open("day8.in") as file:
    data = [row.strip() for row in file.readlines()]

ROWS = len(data)
COLUMNS = len(data[0])

edges = (ROWS * 2) + ((COLUMNS - 2) * 2)
total = edges
foo = []

for row in range(1, ROWS - 1):
    for col in range(1, COLUMNS - 1):
        tree = data[row][col]

        left = [data[row][col - i] for i in range(1, col + 1)]
        right = [data[row][col + i] for i in range(1, COLUMNS - col)]
        up = [data[row - i][col] for i in range(1, row + 1)]
        down = [data[row + i][col] for i in range(1, ROWS - row)]

        if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
            total += 1

        grade = 1
        for list in (left, right, up, down):
            marker = 0
            for i in range(len(list)):
                if list[i] < tree:
                    marker += 1
                elif list[i] >= tree:
                    marker += 1
                    break

            grade *= marker

        foo.append(grade)

print(total)
print(max(foo))
