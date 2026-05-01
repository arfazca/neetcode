class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.store.get(key, [])
        L, R = 0, len(values) - 1

        while (L<=R):
            M = L + ((R - L) // 2)
            if values[M][1] > timestamp:
                R = M - 1
            else:
                res = values[M][0]
                L = M + 1
        return res