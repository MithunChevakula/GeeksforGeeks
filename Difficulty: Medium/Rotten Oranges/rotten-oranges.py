from collections import deque

class Solution:
    def isSafe(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m

    def orangesRotting(self, mat):
        n = len(mat)
        m = len(mat[0])
        queue = deque()
        fresh = 0
        
        # Initialize the queue with all initially rotten oranges and count fresh ones
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif mat[i][j] == 1:
                    fresh += 1
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        elapsedTime = 0
        
        while queue:
            i, j, time = queue.popleft()
            elapsedTime = max(elapsedTime, time)
            
            for dir in directions:
                x, y = i + dir[0], j + dir[1]
                if self.isSafe(x, y, n, m) and mat[x][y] == 1:
                    mat[x][y] = 2  # Rotten now
                    fresh -= 1
                    queue.append((x, y, time + 1))
        
        return -1 if fresh > 0 else elapsedTime

#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends