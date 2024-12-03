import re
input = open("day3_input.txt", "r")
do = True
out = 0
#input = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
for line in input:
    instances = re.findall("(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)", line)
    for instance in instances:
        if instance[0] == "" and instance[1] == "":
            if do:
                out += int(instance[2]) * int(instance[3])
        if instance[0] != "":
            do = True
        if instance[1] != "":
            do = False

print(out)
