# Data Structure-Ch7 Graph
# Critical Path
# Liang
# 2019/6/14

import AVOnetwork

def critical_paths(graph):
    def events_earliest_time(vnum, graph, toposeq):
        ee = [0]*vnum
        for i in toposeq:
            for j, w in graph.out_edges(i):
                if ee[i] + w > ee[j]:
                    ee[j] = ee[i] + w
        return ee

    def event_latest_time(vnum, graph, toposeq, eelast):
        le = [eelast]*vnum
        for k in range(vnum-2, -1, -1):
            i = toposeq[k]
            for j, w in graph.out_edges(i):
                if le[j] - w < le[i]:
                    le[i] = le[j] - w
        return le

    def crt_paths(vnum, graph, ee, le):
        crt_actions = []
        for i in range(vnum):
            for j, w in graph.out_edges(i):
                if ee[i] == le[j] - w:
                    crt_actions.append((i, j, ee[i]))
        return crt_actions

    toposeq = toposort(graph)
    if not toposeq:
        return False
    vnum = graph.vertex_num()
    ee = events_earliest_time(vnum, graph, toposeq)
    le = event_latest_time(vnum, graph, toposeq, ee[vnum-1])
    return crt_paths(vnum, graph, ee, le)
