X = [-1, 0, 1, 0]
Y = [0, -1, 0, 1]


def walk(maze, S, G):
    que = []
    ln = {}
    que.append(S)
    ln[S] = 0
    while len(que) > 0:
        y, x = que.pop()
        for i in range(4):
            ny, nx = y + Y[i], x + X[i]
            if nx >= 0 and ny >= 0 and ny < len(maze) and nx < len(maze[0]) and\
                    maze[ny][nx] != "#" and not (ny, nx) in ln:
                que.append((ny, nx))
                ln[(ny, nx)] = ln[(y, x)] + 1

    return ln[G]


def solve(N, M, maze):
    ans = []
    S = ()
    G = ()
    for y in range(N):
        for x in range(M):
            if maze[y][x] == 'S':
                S = (y, x)
            if maze[y][x] == 'G':
                G = (y, x)

    ans = walk(maze, S, G)
    return ans

maze = [
    list("#S########"),
    list("......#..#"),
    list(".#.##.##.#"),
    list(".#........"),
    list("##.##.####"),
    list("....#....#"),
    list(".#######.#"),
    list("....#....."),
    list(".####.###."),
    list("....#...G#"),
]
print solve(10, 10, maze)
