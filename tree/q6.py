class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

def leia():
    #transformar o dado em arvore binaria
    #tranformar o dado de cada filho em arvore binaria
    #enquanto filhos != 0, nao parar
    #para isso a cada filho que ele tiver, ele tem chamar o próximo input e dividilo em 'filhos' partes de 2
    def auxiliadora(par_ordenado):
        tree = Arvore(par_ordenado[0])
        #print(par_ordenado)
        if par_ordenado[1] == '0':
            return tree
        entrada = input().split()
        refatorada = [entrada[i:i+2] for i in range(0,len(entrada), 2)]
        [tree.filhos.append(par) for par in refatorada]
        #print(tree.filhos)
        for i in range(len(tree.filhos)):
            tree.filhos[i] = auxiliadora(tree.filhos[i])
        return tree

    raiz = input().split()
    return auxiliadora(raiz)

a = leia()
print(a)
print(a.dado)
for item in a.filhos:
    print(item.dado)