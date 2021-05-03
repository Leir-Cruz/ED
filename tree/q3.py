def mostra(raiz):
    def helper(node):
        if node == None:
            return '()'
        else:
            return f'({node.dado} {helper(node.esq)} {helper(node.dir)})'
        
    print(helper(raiz))