class Bts:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def pre_order(root):
    if root is None:
        return -1
    print(root.key, end=" ")
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if root is None:
        return -1
    in_order(root.left)
    print(root.key, end=" ")
    in_order(root.right)
    
def pos_order(root):
    if root is None:
        return -1
    pos_order(root.left)
    pos_order(root.right)
    print(root.key, end=" ")

def insert(root, node):
    if root is None:
        return node
    elif root.key > node.key:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)

count = 0

while True:
    x = input()
    if x == "quack":
        break
    elif x == "pre":
        if count > 0:
            pre_order(my_tree)
        print()
    elif x == "in":
        if count > 0:
            in_order(my_tree)
        print()
    elif x == "pos":
        if count > 0:
            pos_order(my_tree)
        print()
    elif count == 0:
        my_tree = Bts(int(x))
        count += 1
    else:
        new_node = Bts(int(x))
        insert(my_tree, new_node)