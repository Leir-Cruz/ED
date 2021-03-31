def sou_primo(num):
    count = 0
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False

def primos_gemeos(count):
    arr, num = [], 3
    while len(arr) < count:
        if(sou_primo(num) and sou_primo(num + 2)):
            arr.append((num, num + 2))
        num += 1
    return arr

print(primos_gemeos(int(input())))

