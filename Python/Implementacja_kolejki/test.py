for i in range(self.size * 2):
    if i < self.odczyt:
        continue
    elif (i >= self.odczyt) and (i < self.size):
        self.elements[i + self.size] = self.elements[i]
        self.elements[i] = None
self.odczyt += self.size
self.size = self.size * 2