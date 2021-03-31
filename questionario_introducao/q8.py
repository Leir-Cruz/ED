for i in range(int(input())):
    entrada, arr, count = input(), [], -1
    for s in entrada:
        if s.isupper():
            arr.append([s, "0"])
            count += 1
        else:
            arr[count][1] += s
    for item in arr:
        print(item[0]*int(item[1]), end="")
    print()

