with open('day4.in') as file:
    data = [i for i in file.read().strip().split('\n')]

# print(data)

pairs1 = 0
for entry in data:
    first,second =entry.split(',')
    first = [int(i) for i in first.split('-')]
    second = [int(i) for i in second.split('-')]

    if first[0]<= second[0] and first[1] >= second[1]:
        pairs1 += 1

    elif first[0]>= second[0] and first[1] <= second[1]:
        pairs1 += 1

print("Answer for part 1 is :",pairs1)

pairs2 = 0
for entry in data:
    first,second =entry.split(',')
    first = [int(i) for i in first.split('-')]
    second = [int(i) for i in second.split('-')]

    if first[0] in range(second[0] , second[1]+1) or first[1] in range(second[0], second[1]+1):
        pairs2 += 1

    elif second[0] in range(first[0], first[1]+1) or second[1] in range(first[0], first[1]+1):
        pairs2 += 1

print("Answer for part 2 is :",pairs2)
