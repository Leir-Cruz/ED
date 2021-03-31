slow, normal, fast = [], [], []
for i in range(int(input())):
    i = int(input())
    if i < 10:
        slow.append(i)
    elif i < 20:
        normal.append(i)
    else:
        fast.append(i)

def identify_higher(arr):
    if len(arr) == 0:
        return 0
    else:
        x = arr[0]
        for i in arr:
            if x < i:
                x = i
        return x

print(identify_higher(slow), end=" ")
print(identify_higher(normal), end=" ")
print(identify_higher(fast))
