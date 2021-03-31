for string in range(int(input())):
    string, arr_of_ones, num = input(), [], 0
    for s in range(len(string)):
        if string[s] == '1':
            arr_of_ones.append(s)
    if len(arr_of_ones) <= 1:
        print(0)
    else:
        for i in range(len(arr_of_ones) - 1):
            num += arr_of_ones[i + 1] - arr_of_ones[i] - 1
        print(num)