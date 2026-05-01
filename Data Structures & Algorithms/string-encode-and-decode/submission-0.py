class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for n in strs:
            s+=str(len(n))+"#"+n
        return s
    def decode(self, s: str) -> List[str]:
        i, strs = 0, []
        
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            strs.append(s[j+1:j+1+length])
            i=j+length+1
        return strs
            