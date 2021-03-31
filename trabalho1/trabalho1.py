class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque

d = Deque()

def adicionar_alfabeto(deque, alfabeto):
    for l in alfabeto:
        deque.add_front(l)

def decifrar(deque, texto_cifrado, chave):
    alfabeto, size_cifrado, decifrada = deque.__str__(), len(texto_cifrado), ''
    for i in range(len(texto_cifrado)):
        for j in range(len(alfabeto)):
            if texto_cifrado[i] == alfabeto[j]:
                if j - chave < 0:
                    negative = j - chave
                    new_letter = alfabeto[len(alfabeto) - (-negative)]
                    removed = deque.remove_rear()
                    deque.add_front(removed)
                    decifrada += new_letter
                    break
                else:
                    new_letter = alfabeto[j - chave]
                    removed = deque.remove_rear()
                    deque.add_front(removed)
                    decifrada += new_letter
                    break
    return decifrada

adicionar_alfabeto(d, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(decifrar(d, "DEFGHIJKLMNOPQRSTUVWXYZABC", 3))
print(d.__str__())

