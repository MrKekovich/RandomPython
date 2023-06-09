points_in = [
    [20, 25],
    [20, 15],
    [25, 20],
    [15, 20],
    [20, 20],
]
points_out = [
    [30, 20],
    [20, 30],
    [10, 20],
]
o = [20, 20]
r = 5


def check(a, o, r):
    if (a[0] <= o[0] + r and a[0] >= o[0] - r) and (a[1] <= o[1] + r and a[1] >= o[1] - r):
        print('Точка принадлежит окружности')
    else:
        print('Точка не принадлежит окружности')

# подходят
for point in points_in:
    check(point, o, r)

# не подходят
for point in points_out:
    check(point, o, r)

