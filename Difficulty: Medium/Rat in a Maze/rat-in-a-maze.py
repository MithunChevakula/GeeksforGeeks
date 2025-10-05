class Solution:
    def ratInMaze(self, maze):
        hth=len(maze)
        wth=len(maze[0])
        ret=[]
        cur=[]
        def dfs(x=0,y=0):
            nonlocal maze,hth,wth,ret,cur
            if not 0<=x<wth or not 0<=y<hth or maze[y][x]==0:
                return
            if x==wth-1 and y==hth-1:
                ret.append(''.join(cur))
                return
            maze[y][x]=0
            for dir in 'UDLR':
                cur.append(dir)
                dfs(x+(1 if dir=='R' else -1 if dir=='L' else 0),
                    y+(1 if dir=='D' else -1 if dir=='U' else 0))
                cur.pop()
            maze[y][x]=1
        dfs()
        return sorted(ret)