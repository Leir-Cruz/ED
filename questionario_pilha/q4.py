class Peso:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.insert(0, item)

    def pop(self):
        self.itens.pop(0)

weight = Peso()
while 1:
    x = int(input())
    if x != 0:
        weight.push(x)
    else:
        break
desired_weight, count, moved = int(input()), 0, 0
while 1:
    print(f"Peso retirado: {weight.itens[0]}")
    count += 1
    if weight.itens[0] != desired_weight:
        moved += weight.itens[0]
        weight.pop()
    else:
        moved += weight.itens[0]
        print(f"Anilhas retiradas: {count}")
        print(f"Peso total movimentado: {moved}")
        break



