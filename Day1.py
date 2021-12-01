with open('1.txt') as file:
    sub = file.readlines()
    sub = [line.strip() for line in sub]

# part1 #
count = 0
for i in range(len(sub)-1):
    prev = int(sub[i])
    nextOne = int(sub[i+1])
    if nextOne>prev:
        count += 1

print(count)

# part 2 #
count1 = 0
for i in range(len(sub)-3):
    first = int(sub[i]) + int(sub[i+1]) + int(sub[i+2])
    second = int(sub[i+1]) + int(sub[i+2]) + int(sub[i+3])
    if second > first:
        count1 += 1

print(count1)
