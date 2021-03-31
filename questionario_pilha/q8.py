class Nos:
    def __init__(self):
        self.chaves = []

    def insercao(self, chave):
        self.chaves.append(chave)

    def remocao(self, chave):
        self.chaves.remove(chave)

lista = Nos()

while 1:
    x = input().split()
    if x[0] == "f":
        break
    elif x[0] == "i":
        lista.insercao(x[1])
    elif x[0] == "r":
        lista.remocao(x[1])

