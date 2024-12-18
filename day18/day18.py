# import sys
# sys.setrecursionlimit(1073741824)
#
# DIR4 = [[0,1],[1,0],[0,-1],[-1,0]]
#
# with open('input.txt') as f:
#     lines = [l.strip() for l in f.readlines()]
#     R = C = 71
#
#     cs = []
#     for l in lines:
#         x,y=map(int,l.split(','))
#         cs.append((y,x))
#
#     g = []
#     for i in range(R):
#         g.append(['.'] * C)
#
#     def bfs():
#         visited = set()
#         q = [((0,0), 0)]
#         while q:
#             cur, dist = q.pop(0)
#             if cur in visited:
#                 continue
#             visited.add(cur)
#             if cur == (R - 1, C - 1):
#                 print(dist)
#                 return True
#
#             x,y=cur
#             for d in range(4):
#                 dx,dy = DIR4[d]
#                 nx,ny = x+dx,y+dy
#                 if nx in range(R) and ny in range(C) and g[nx][ny] != '#':
#                     q.append(((nx, ny), dist+1))
#         return False
#
#     for i in range(1024):
#         g[cs[i][0]][cs[i][1]] = '#'
#
#     bfs()
#
import sys
sys.setrecursionlimit(1073741824)

DIR4 = [[0,1],[1,0],[0,-1],[-1,0]]

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    R = C = 71

    cs = []
    for l in lines:
        x,y=map(int,l.split(','))
        cs.append((y,x))

    g = []
    for i in range(R):
        g.append(['.'] * C)

    def bfs():
        visited = set()
        q = [((0,0), 0)]
        while q:
            cur, dist = q.pop(0)
            if cur in visited:
                continue
            visited.add(cur)
            if cur == (R - 1, C - 1):
                return True

            x,y=cur
            for d in range(4):
                dx,dy = DIR4[d]
                nx,ny = x+dx,y+dy
                if nx in range(R) and ny in range(C) and g[nx][ny] != '#':
                    q.append(((nx, ny), dist+1))
        return False

    for i in range(len(cs)):
        g[cs[i][0]][cs[i][1]] = '#'
        if not bfs():
            print(str(cs[i][1])+','+str(cs[i][0]))
            break
