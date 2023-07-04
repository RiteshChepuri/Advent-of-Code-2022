from string import ascii_letters

with open('day3.in') as file:
    data = [i for i in file.read().strip().split("\n")]

# print(data)

sum = 0

for entry in data:
    half = len(entry)//2

    left = set(entry[:half])
    right = set(entry[half:])

    # print(entry,left,right)


    for priority, char in enumerate(ascii_letters):
        if char in left and char in right:
            sum += priority + 1            

print("part1 ",sum)

sum2 = 0
j = 3
for i in range(0, len(data), 3):
    data2 = data[i:j]
    j +=3
    
    # print(data2)
    for priority, char in enumerate(ascii_letters):
        if char in data2[0] and char in data2[1] and char in data2[2]:
            sum2 += priority + 1            

print("part2", sum2)
