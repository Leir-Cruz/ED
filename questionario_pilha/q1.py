class Slack:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        print(self.itens[0], end ="")
        self.itens.pop(0)


entrada, objeto = input(), Slack()
for l in entrada:
    if l != "*":
        objeto.enqueue(l)
    else:
        objeto.dequeue()
