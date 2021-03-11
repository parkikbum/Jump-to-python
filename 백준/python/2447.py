n = int(input())
stars = [[' ' for _ in range(n)]for _ in range(n)]
def star(size, x, y):
    if size == 1:
        stars[y][x] = '*'
    else:
        next_size = size//3
        for dy in range(3):
            for dx in range(3):
                if dy != 1 or dx != 1:
                    stars(next_size,x+dx*next_size, y+dy*next_size)
stars(n,0,0)
for k in stars:
    print(''.join(k))
