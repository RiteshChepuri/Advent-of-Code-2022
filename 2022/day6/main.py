with open("day6.in") as file:
    input = file.read()

for i in range(4, len(input)):
    s = set(input[(i - 4) : i])
    if len(s) == 4:
        print("part 1 Answer: ", i)
        break

for i in range(14, len(input)):
    s = set(input[(i - 14) : i])
    if len(s) == 14:
        print("part 2 Answer: ", i)
        break
