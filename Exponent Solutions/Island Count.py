from typing import List

def get_number_of_islands(binaryMatrix: List[List[int]]) -> int:
    answer = 0
    R, C = len(binaryMatrix), len(binaryMatrix[0])

    def explore(r, c):
        if not (R > r >= 0 <= c < C) or binaryMatrix[r][c] == 0:
            return

        binaryMatrix[r][c] = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dr, dc in directions:
            new_row = r + dr
            new_col = c + dc
            explore(new_row, new_col)

    for r in range(R):
        for c in range(C):
            if binaryMatrix[r][c] == 1:
                answer += 1
                explore(r, c)

    return answer
    
# debug your code below
binaryMatrix = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
# answer = 1

print(get_number_of_islands(binaryMatrix))
