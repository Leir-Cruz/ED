class ArvoreBinaria:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None

def mostra_nivel(root, level):
    def build_array(root):
        if root is None:
            return "()"
        else:
            return f'({root.dado} {build_array(root.esq)} {build_array(root.dir)})'

    if level == 0:
        print(build_array(root))
        return 0
    if root.esq is not None:
        mostra_nivel(root.esq, level -1)
    if root.dir is not None:
        mostra_nivel(root.dir, level -1)
        












    tree = build_array(root)
    tree.replace("(", "[")
    tree.replace(")", "]")
    new_tree = list(tree)



                         0            A    
                                    /  \
                         1         B    C
                                 /  \  / \
                         2       D  E   F  G