def nivel(raiz,dado):
    def levelNode(root, dado, level = 0):
        if root == None:
            return -1
        if root.dado == dado:
            return level
        left = levelNode(root.esq, dado, level + 1)
        if left != - 1:
            return left
        return levelNode(root.dir, dado, level + 1)

    l = levelNode(raiz, dado)
    return l if l >= 0 else - 1

