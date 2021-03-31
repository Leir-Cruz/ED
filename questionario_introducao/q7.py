size, time = int(input()), 0
print(f"Transmitindo {size} bytes...")

while size > 0:
    transmitted = []
    initial = size
    for i in range(5):
        x = int(input())
        size -= x
        time += 1
        if size <= 0:
            print(f"Tempo total: {time} segundos.")
            break
        else:
            transmitted.append(x)
        speed = (sum(transmitted) / 5)
    if initial == size:
        print("Tempo restante: pendente...")
    elif size > 0 and (size/speed) // 1 != (size/speed):
        print(f"Tempo restante: {round((size/speed)+0.5)} segundos.")
    elif size > 0 and (size/speed) // 1 == (size/speed):
        print(f"Tempo restante: {int(size / speed)} segundos.")