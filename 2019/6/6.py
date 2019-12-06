import collections

def solveA(M):
    answer = {}
    def dfs(n):
        if n not in M:
            return 0
        if n not in answer:
            answer[n] = len(M[n]) + sum(dfs(n2) for n2 in M[n])
        return answer[n]
    return sum(dfs(n) for n in M.keys())

def solveB(M):
    # make undirected
    M2 = collections.defaultdict(set)
    for a, vs in M.items():
        for b in vs:
            M2[a].add(b)
            M2[b].add(a)
    M = M2

    seen = set()
    def dfs(n):
        if n == 'SAN':
            return -2
        if n in seen:
            return None
        seen.add(n)
        for n2 in M[n]:
            dist = dfs(n2)
            if dist is not None:
                return dist + 1
        return None
    return dfs('YOU')

M = collections.defaultdict(list)
for line in open('input'):
    a, b = line.strip().split(')')
    M[b].append(a)

print('A', solveA(M))
print('B', solveB(M))
