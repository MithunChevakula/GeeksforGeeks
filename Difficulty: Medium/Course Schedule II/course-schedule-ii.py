class Solution:
    def findOrder(self, n, prerequisites):
        from collections import defaultdict
        adj=defaultdict(set)
        idg=defaultdict(int)
        for sto,sta in prerequisites:
            adj[sta].add(sto)
            idg[sto]+=1
        ret=[]
        q=[x for x in range(n) if idg[x]==0]
        while q:
            cur=q.pop()
            ret.append(cur)
            for nxt in adj[cur]:
                idg[nxt]-=1
                if idg[nxt]==0:
                    q.append(nxt)
        return ret if len(ret)==n else []