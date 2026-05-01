class DynamicArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [0] * self.capacity
        self.length = 0

    def get(self, i: int) -> int:
        # if (i < self.getSize()):
            # self.resize()
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if (i <= self.getCapacity()):
            self.array[i-1] = n
    def pushback(self, n: int) -> None:
        self.incSize()
        if (self.getCapacity() < self.getSize()):
            self.resize()
        self.array[self.getSize()-1] = n

    def popback(self) -> int:
        self.array[self.getSize()-1]=0
        self.decSize()

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        newArr = [0] * self.capacity
        for i in range(self.getSize()-1):
            newArr[i] = self.array[i]
        self.array = newArr

    def incSize(self) -> None:
        self.length += 1

    def decSize(self) -> None:
        self.length -= 1

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity