class CountSquares:

    def __init__(self):
        self.freq = {}
        self.points = []        

    def add(self, point: List[int]) -> None:
        px, py = point
        key = (px, py) # also key = tuple(point)

        if key in self.freq: self.freq[key] += 1
        else: self.freq[key] = 1

        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.points:
            if (abs(px-x) != abs(py-y)) or (px==x) or (py==y): continue
            count1 = self.freq.get((x, py), 0)
            count2 = self.freq.get((px, y), 0)
            res += count1 * count2
        return res
