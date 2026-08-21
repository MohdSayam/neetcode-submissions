class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create 9 tracking sets for rows, 9 for columns, and 9 for 3x3 blocks
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                    
                # Formula to map a 2D cell (r, c) to one of the nine 3x3 blocks (0-8)
                block_idx = (r // 3) * 3 + (c // 3)
                
                # If the value is already tracked in this row, column, or block
                if val in rows[r] or val in cols[c] or val in blocks[block_idx]:
                    return False
                    
                # Record the value
                rows[r].add(val)
                cols[c].add(val)
                blocks[block_idx].add(val)
                
        return True


        