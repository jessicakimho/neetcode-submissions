class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def backtrack(row, col, i):
            # base case
            if i == len(word):
                return True

            # choose
            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                (row, col) in visited or
                board[row][col] != word[i] 
            ):
                return False

            visited.add((row, col))

            # backtrack
            found = (
                backtrack(row + 1, col, i + 1) or # down
                backtrack(row - 1, col, i + 1) or # up
                backtrack(row, col + 1, i + 1) or # right
                backtrack(row, col - 1, i + 1)    # left
            )

            # undo
            visited.remove((row,col))

            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False

