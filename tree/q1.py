class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []


def mostra(raiz, prefixo):
    def addPrefixo(node, prefix):
        if node.filhos != None:
            for son in node.filhos:
                son.dado = prefix + str(son.dado)
                addPrefixo(son, prefix)
    
    addPrefixo(raiz, prefixo)
    print(raiz.dado)
    if raiz.filhos != None:
        [mostra(x, prefixo) for x in raiz.filhos]





