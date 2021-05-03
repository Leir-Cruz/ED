class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir
#procura as duas cartas nas arvores
#apos achar cada uma delas, vê o parente em comum mais próximo dos dois
def verificaPontuacao(root, card1, card2):
    if root is None:
        return None
    if root.dado == card1 or root.dado == card2:
        return root.dado
    left = verificaPontuacao(root.esq, card1, card2)
    right = verificaPontuacao(root.dir, card1, card2)
    if left is not None and right is not None:
        return root.dado
    else:
        return left if left is not None else right