class Queue:
    def __init__(self):
        self.itens = []

    def __str__(self):
        return str(self.itens)
        
    def isEmpty(self):
        return self.itens == []

    def enqueue(self, item):
        self.itens.append(item) # self.itens.insert(0, item)

    def dequeue(self):
        return self.itens.pop(0) # return self.itens.pop()

    def size(self):
        return len(self.itens)

    def __len__(self):
        return len(self.itens)
