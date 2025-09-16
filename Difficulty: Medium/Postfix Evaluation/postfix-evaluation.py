class Solution:
    def evaluatePostfix(self, arr):
        n = []
        for i in range(len(arr)):
            if arr[i] == '+':
                k = int(n[-2]) + int(n[-1])
                n.pop()
                n.pop()
                n.append(k)
            elif arr[i] == '-':
                k = int(n[-2]) - int(n[-1])
                n.pop()
                n.pop()
                n.append(k)
            elif arr[i] == '*':
                k = int(n[-2]) * int(n[-1])
                n.pop()
                n.pop()
                n.append(k)
            elif arr[i] == '/':
                k = int(n[-2]) // int(n[-1])
                n.pop()
                n.pop()
                n.append(k)
            elif arr[i] == '^':
                k = int(n[-2]) ** int(n[-1])
                n.pop()
                n.pop()
                n.append(k)
            else:
                n.append(arr[i])
        return int(n[-1])