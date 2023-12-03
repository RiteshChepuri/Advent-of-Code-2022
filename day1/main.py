with open('day1.in') as file:
    data = [i for i in file.read().strip().split("\n")]

# print(data)

max = 0
count = 0
max2 = 0 # 2nd highest calories
max3 =0 # 3rd highest calories

for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num

    if count > max :
        max3 = max2
        max2 = max
        max = count
    elif count > max2:
        max3 = max2
        max2 = count
    elif count > max3:
        max3 = count

print("answer for part 1:", max)
print("answer for part 2:", max+max2+max3)
