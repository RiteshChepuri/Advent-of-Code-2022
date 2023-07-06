# from string import ascii_uppercase

with open('day5.in') as file:
    whole_stack, instructions = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))

stacks = {int(digit):[] for digit in whole_stack[-1].replace(" ","")}
# here stacks is used for storing stacks number and char in stacks

# print(stacks)

indexes = [index for index, char in enumerate(whole_stack[-1]) if char != " "]
# Indexes are used to store the indexes of chars that need to be filled in

# print(instructions)

# To display the stacks
def displayStacks():
    print("Stacks :")
    for stack in stacks:
        print(stack, stacks[stack])


# To load the stacks
def loadStacks():
    for string in whole_stack[:-1]:
        stack_no = 1
        for index in indexes:
            if string[index] == " ":
                pass
            else:
                stacks[stack_no].insert(0, string[index])
            stack_no += 1

# To clear the stacks
def clearStacks():
    for stack_no in stacks:
        stacks[stack_no].clear()

# To get the end char at the stacks
def endStacks():
    ans = ""
    for stack in stacks:
        ans += stacks[stack][-1]
    return ans


# part 1
loadStacks()
for instruction in instructions:
    instruction = instruction.replace("move ","").replace("from ","").replace("to ","").strip().split(" ")
    # print(instruction)
    instruction = [int(i) for i in instruction]


    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    # print(crates,from_stack,to_stack)

    for crate in range(crates):
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)

print("Answer for part 1 is :", endStacks())


clearStacks()
loadStacks()

for instruction in instructions:
    instruction = instruction.replace("move ","").replace("from ","").replace("to ","").strip().split(" ")
    # print(instruction)
    instruction = [int(i) for i in instruction]


    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]
    
    crates_to_remove = stacks[from_stack][-crates:]
    stacks[from_stack]= stacks[from_stack][:-crates]

    for crate in crates_to_remove:
        stacks[to_stack].append(crate)


print("Answer for part 2 is :", endStacks())
