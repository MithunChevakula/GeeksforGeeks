class Solution:
    def minConnect(self, V, edges):
        E=len(edges)
        if E<V-1:
            return -1
        pr=[*range(V)]
        sz=[1]*V
        def find(a):
            nonlocal pr
            ori=a
            while a!=pr[a]:
                a=pr[a]
            pr[ori]=a
            return a
        def union(a,b):
            nonlocal pr,sz
            a=find(a)
            b=find(b)
            if a==b:
                return False
            if sz[a]<sz[b]:
                a,b=b,a
            pr[b]=a
            sz[a]+=sz[b]
            return True
        surplus=0
        for sta,sto in edges:
            if find(sta)==find(sto):
                surplus+=1
                continue
            union(sta,sto)
        seen=set([find(x) for x in range(V)])
        lth=len(seen)
        if surplus>=lth-1:
            return lth-1
        return -1