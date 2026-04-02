import math

def geometric_median(points, eps=1e-7):
    x = sum(p[0] for p in points) / len(points)
    y = sum(p[1] for p in points) / len(points)

    while True:
        num_x = num_y = denom = 0.0

        for px, py in points:
            dx = x - px
            dy = y - py
            dist = math.hypot(dx, dy)

            if dist < eps:
                return px, py

            w = 1.0 / dist
            num_x += px * w
            num_y += py * w
            denom += w

        new_x = num_x / denom
        new_y = num_y / denom

        if math.hypot(new_x - x, new_y - y) < eps:
            return new_x, new_y

        x, y = new_x, new_y


def solve():
    n = int(input())
    points = [tuple(map(float, input().split())) for _ in range(n)]
    hx, hy = geometric_median(points)

    total = sum(math.hypot(hx - x, hy - y) for x, y in points)
    print(f"{total:.6f}")


solve()