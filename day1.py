input = open("day1_input.txt", "r")

left = []
right = []
temp = []


for line in input:
    temp = line.split()
    left.append(temp[0])
    right.append(temp[1])

out = 0
for i in range(len(left)):
    out += int(left[i]) * int(right.count(left[i]))

print(out)