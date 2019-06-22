# Data Structure-Ch5 Stack and Queue
# Recursive solution, retrospective method of maze
# Liang
# 2019/4/19

# Recursive solution
dirs = [(0,1), (1,0), (0,-1), (-1,0)]

def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2

def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print(pos, end=" ")
        return True
    for i in range(4):
        nextp = pos[0]+dirs[i][0], pos[1]+dirs[i][1]
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                print(pos, end=" ")
                return True
    return False

# Retrospective method
from SStack import SStack

def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))
    while not st.is_empty():
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])
            if nextp == end:
                print_path(end, pos, st)
                return
            if passable(maze, nextp):
                st.push((pos, i+1))
                mark(maze, nextp)
                st.push((nextp, 0))
                break
    print("No path found.")

def pring_path(end, pos, st):
    pass

# Based queue
from SQueue import SQueue

def maze_solver_queue(maze, start, end):
    if start == end:
        print("Path finds.")
        return None
    qu = SQueue()
    mark(maze, start)
    qu.enqueue(start)
    while not qu.is_empty():
        pos = qu.dequeue()
        for i in range(4):
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])
            if passable(maze, nextp):
                if nextp == end:
                    print("Path find.")
                    return None
                mark(maze, nextp)
                qu.enqueue(nextp)
    print("No path.")
