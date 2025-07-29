class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        l = []
        ind = {}

        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                if s not in ind:
                    ind[s] = []
                ind[s].append((i, j))

        v = set()
        for k in range(n):
            m = -arr[k]
            if m in ind:
                for i, j in ind[m]:
                    if i != k and j != k:
                        triplet = tuple(sorted([i, j, k]))
                        if triplet not in v:
                            v.add(triplet)
                            l.append(list(triplet))

        return l