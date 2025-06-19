class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self._index = 0

    def __iter__(self):
        self._index = 0  # reset for each new iteration
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {"length": self.length}
        elif self._index == 1:
            self._index += 1
            return {"width": self.width}
        else:
            raise StopIteration
'''_____________________________________________________'''

rect = Rectangle(5, 10)
for val in rect:
    print(val)
