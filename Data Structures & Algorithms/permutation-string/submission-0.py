class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap, window = Counter(s1), len(s1)

        for i in range(len(s2)):
            if (s2[i] in hashmap):
                hashmap[i] -= 1
            if (i >= window) and (s2[i-window] in hashmap):
                hashmap[i-window] += 1
            if all ([hashmap[e]==0 for e in hashmap]):
                return True
        return False