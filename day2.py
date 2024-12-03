def checkValid(arr) -> bool:
    safe = True
    increasing = None
    for i in range(1, len(arr)):
            if int(arr[i-1]) - int(arr[i]) > 3:
                safe = False
                break
            elif int(arr[i-1]) - int(arr[i]) < -3:
                safe = False
                break
            elif int(arr[i-1]) - int(arr[i]) == 0:
                safe = False
                break
            else:
                if 0 < int(arr[i-1]) - int(arr[i]) < 4 and increasing is not None:
                    if not increasing:
                        safe = False
                        break
                elif -4 < int(arr[i-1]) - int(arr[i]) < 0 and increasing is not None:
                    if increasing:
                        safe = False
                        break
                else:
                    if int(arr[i-1]) - int(arr[i]) > 0:
                        increasing = True
                    else:
                        increasing = False
    return safe

input = open("day2_input.txt", "r")

#input = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"]

out = 0
for line in input:
    arr = line.split()
    safe = checkValid(arr)
    if safe:
        out += 1
    else: #try to remove one line
        print(f"bad: line = {line}")
        for i in range(0, len(arr)):
            temp = arr.copy()
            del temp[i]
            if checkValid(temp):
                out += 1
                print(f"works: temp = {temp}")
                break


print(out)