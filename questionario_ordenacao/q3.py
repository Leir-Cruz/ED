num, contador, duplicados = int(input()), 0, []
lista = [item for item in input().split()]
for item in lista:
    x = lista.count(item)
    if lista.count(item) > 1:
        for i in range(x - 1):
            lista.remove(item)
            contador += 1
print(contador)
