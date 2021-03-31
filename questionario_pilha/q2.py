class Slack:
    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        self.items.pop(0)