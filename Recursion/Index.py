# 79. Word Search
class Solution:
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def solution(self, board, word, x, y, cur):
        if(x < 0 or x >= len(board) or y < 0 or y >= len(board[x]) or board[x][y] == ' '):
            return False
        cur += board[x][y]

        if(len(cur) > len(word)):
            return False

        if(cur[len(cur)-1] != word[len(cur)-1]):
            return False
        if(cur == word):
            return True

        temp = board[x][y]
        board[x][y] = ' '

        for i in range(4):
            if(self.solution(board, word, x+self.dx[i], y+self.dy[i], cur)):
                return True

        board[x][y] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if(len(word) == 0):
            return True
        n = len(board)

        for i in range(n):
            m = len(board[i])
            for j in range(m):

                if(word[0] == board[i][j] and self.solution(board, word, i, j, "")):
                    return True
        return False

# 328. Odd Even Linked List

# 78. subset
# class Solution:

#     def solution(self, num, ans, cur, index):
#         if index > len(num):
#             return

#         ans.append(cur[:])
#         for i in range(index, len(num)):
#             if num[i] not in cur:
#                 cur.append(num[i])
#                 self.solution(num, ans, cur, i)
#                 cur.pop()
#         return

#     def subsets(self, num: List[int]) -> List[List[int]]:
#         ans = []
#         cur = []
#         self.solution(num, ans, cur, 0)
#         return ans

# print()
