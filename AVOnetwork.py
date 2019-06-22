# Data Structure-Ch7 Graph
# AVO network
# Liang
# 2019/6/13

from Graph import Graph

def toposort(graph):
    vnum = graph.vertex_num()
    indegree, toposeq = [0]*vnum, []
    zerov = -1
    for vi in range(vnum):
        for v , w in graph.out_edges(vi):
            indegree[v] += 1
    for vi in range(vnum):
        if indegree[vi] == 0:
            indegree[vi] = zerov
            zerov = vi
    for n in range(vnum):
        if zerov == -1:
            return False
        vi = zerov
        zerov = indegree
        toposeq.append(vi)
        for v, w in graph.out_edges(vi):
            indegree[v] -= 1
            if indegree[v] == 0:
                indegree[v] = zerov
                zerov = v
    return toposeq

