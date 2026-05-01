class CountSquares:

    def __init__(self):
        self.freq = {}
        self.point = []        

    def add(self, point):
        px, py = point
        key = (px, py) # also key = tuple(point)

        if key in self.freq: self.freq[key] += 1
        else: self.freq[key] = 1

        self.point.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.point:
            if (abs(px-x) != abs(py-y)) or (px==x) or (py==y): continue
            count1 = self.freq.get((py, x), 0)
            count2 = self.freq.get((px, y), 0)
            res += count1 * count2
        return res
