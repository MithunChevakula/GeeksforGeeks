class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        # code here
        n=len(maze)
        res=[]
        def is_safe(nx,ny):
            return 0<=nx<n and 0<=ny<n and not visited[nx][ny] and maze[nx][ny]==1
            
        def backtracking(r,c,path):
            if r==n-1 and c==n-1:
                res.append(path)
                return
            visited[r][c]=True
            for x,y,dir in [(1,0,"D"),(0,-1,"L"),(0,1,"R"),(-1,0,"U")]:
                nx,ny=x+r,y+c
                if is_safe(nx,ny):
                    backtracking(nx,ny,path+dir)
            visited[r][c]=False
        visited=[[False]*n for i in range(n)]
        backtracking(0,0,"")
        return res