num, diferencas = int(input()), []
lista = [int(item) for item in input().split()]

for i in range(len(lista) - 1):
    if lista[i] - lista[i + 1] > 1 or lista[i] - lista[i + 1] < 1:
        lista.insert(i + 1, lista[i] + 1)

for i in range()