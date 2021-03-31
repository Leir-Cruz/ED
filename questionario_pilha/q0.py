class Slack:
    def __init__(self):
        self.itens = []

    def isEmpty(self):
        return self.itens == []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        self.itens.pop()

    def peek(self):
        if not self.itens == []:
            return self.itens[len(self.itens) - 1]
        else:
            return "Error, slack is empty"

    def size(self):
        return len(self.itens)