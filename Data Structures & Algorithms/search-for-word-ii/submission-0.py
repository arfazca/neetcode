class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        res, V = set(), set()
        for word in words: self.addWord(word)
        
        def init(r:int, c:int, node:TrieNode, word:str) -> None:
            if (
                r in range(len(board)) and
                c in range(len(board[0])) and
                (r,c) not in V and
                board[r][c] in node.children
            ):
                V.add((r,c))
                word += board[r][c]
                node = node.children[board[r][c]]
                if node.endOfWord: res.add(word)
                direc=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in direc:
                    init(r+dr, c+dc, node, word)
                V.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                init(r, c, self.root, "")
        return list(res)