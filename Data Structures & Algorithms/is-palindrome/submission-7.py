class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=[char.lower() for char in s if char.isalnum()]
        # print("st\t", st, " ", len(st))
        ss=[char.lower() for char in st[0:len(st)//2]]
        tt = [char.lower() for char in st[len(st)//2:][::-1]]
        # print("ss\t", ss)
        # print("tt\t", tt)
        for i, char in enumerate(tt):
            if (i<len(ss)) and (char != ss[i]):
                return False
        return True
        