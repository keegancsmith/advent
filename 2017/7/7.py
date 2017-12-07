#!/usr/bin/env python3

# this code sucks thanks minimal sleep (thanks Arto!), sorry.
# cleaned up, original part 2 I did via manual work and partial algorithmic
# solution. The implementation seen here is full algorithmic solution.
# See recording at https://asciinema.org/a/lqeMseXGLipzmXrUs4aYZSw6G

graph = {}
for l in open('input').readlines():
    p = l.strip().split(' ', 2)
    k = p[0]
    w = int(p[1][1:-1])
    e = ()
    if len(p) > 2:
        e = tuple(p[2][3:].split(', '))
    graph[k] = (w, e)

def solveA():
    candidate = set(graph)
    for k in graph:
        for e in graph[k][1]:
            if e in candidate:
                candidate.remove(e)
    return candidate.pop()

def solveB(k):
    # [(answer, weight)]
    children = [solveB(x) for x in graph[k][1]]
    
    if any(x[0] for x in children):
        answer = [x[0] for x in children if x[0]][0]
    else:
        answer = 0

    weights = [x[1] for x in children]
    if weights and not all(x == weights[0] for x in weights):
        # We will have atleast 3 weights, but only 2 distinct.
        s = sorted(weights)
        bad_weight, good_weight = s[0], s[-1]
        if s[0] == s[1]:
            bad_weight, good_weight = good_weight, bad_weight
        bad_k = graph[k][1][weights.index(bad_weight)]
        answer = answer or (graph[bad_k][0] - (bad_weight - good_weight))

    return (answer, graph[k][0] + sum(weights))

root = solveA()
print('A', root)
print('B', solveB(root)[0])
