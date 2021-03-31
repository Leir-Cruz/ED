lista, nova_lista = list(input()), []
for l in lista:
    if l != "*":
        nova_lista.insert(0, l)
    else:
        print(nova_lista[0], end="")
        nova_lista.pop(0)
