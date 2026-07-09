def solution(B):
    N = len(B)

    # convert to 2D list
    board = [list(row) for row in B]

    # find staring position
    # 1. Find Jafar's starting position
    start_r, start_c = -1, -1
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'O':
                start_r, start_c = r, c
                break
        if start_r != -1:
            break
            
    # If Jafar is missing (shouldn't happen per constraints), return 0
    if start_r == -1:
        return 0

    # 2. DFS function to explore all jump chains
    def dfs(r, c):
        max_jumps = 0
        
        # --- Check Up-Left Jump ---
        # Destination is (r-2, c-2), jumped pawn is at (r-1, c-1)
        if r - 2 >= 0 and c - 2 >= 0:
            if board[r-1][c-1] == 'X' and board[r-2][c-2] == '.':
                
                # Make the move: remove Aladdin's pawn
                board[r-1][c-1] = '.'
                
                # Recurse from the new position, add 1 to the result
                jumps = 1 + dfs(r - 2, c - 2)
                max_jumps = max(max_jumps, jumps)
                
                # Backtrack: put the pawn back for other branch evaluations
                board[r-1][c-1] = 'X'
                
        # --- Check Up-Right Jump ---
        # Destination is (r-2, c+2), jumped pawn is at (r-1, c+1)
        if r - 2 >= 0 and c + 2 < N:
            if board[r-1][c+1] == 'X' and board[r-2][c+2] == '.':
                
                # Make the move
                board[r-1][c+1] = '.'
                
                # Recurse from the new position, add 1 to the result
                jumps = 1 + dfs(r - 2, c + 2)
                max_jumps = max(max_jumps, jumps)
                
                # Backtrack
                board[r-1][c+1] = 'X'
                
        return max_jumps

    # 3. Trigger the DFS from the starting position
    return dfs(start_r, start_c)

# --- Test Suite ---

def test_checkers_solution():
    # Test 1: No jumps possible (Target is out of bounds)
    B1 = [
        "...",
        "X.X",
        ".O."
    ]
    assert solution(B1) == 0, f"Test 1 Failed! Expected 0, got {solution(B1)}"

    # Test 2: Single valid jump
    B2 = [
        ".....",
        ".....",
        ".....",
        ".X...",
        "..O.."
    ]
    # Jumps up-left from (4,2) over (3,1) landing on (2,0)
    assert solution(B2) == 1, f"Test 2 Failed! Expected 1, got {solution(B2)}"

    # Test 3: Multiple jumps in a single chain
    B3 = [
        "........",
        "........",
        "...X....", # Jump 3 goes over this (2,3), lands at (1,4)
        "........", # Lands here at (3,2)
        "...X....", # Jump 2 goes over this (4,3)
        "........", # Lands here at (5,4)
        ".....X..", # Jump 1 goes over this (6,5)
        "......O."  # Starts at (7,6)
    ]
    assert solution(B3) == 3, f"Test 3 Failed! Expected 3, got {solution(B3)}"

    # Test 4: Branching paths (Must pick the longest)
    B4 = [
        "........",
        "........",
        "...X....", # Left path jump 2
        "........", # Left path lands at (3,2)
        "...X.X..", # Left path jump 1 (4,3) | Right path jump 1 (4,5)
        "....O..."  # Starts at (5,4)
    ]
    # Left path gives 2 jumps, right path gives 1 jump (out of bounds after). 
    # DFS should evaluate both and return 2.
    assert solution(B4) == 2, f"Test 4 Failed! Expected 2, got {solution(B4)}"
    
    # Test 5: Missing Jafar (Edge case)
    B5 = [
        "...",
        "...",
        "..."
    ]
    assert solution(B5) == 0, f"Test 5 Failed! Expected 0, got {solution(B5)}"

    print("All test cases passed successfully! 🎉")

if __name__ == "__main__":
    test_checkers_solution()