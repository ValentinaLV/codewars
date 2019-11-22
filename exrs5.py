def draw_stairs_full_stairs(n):
    for i in range(1, n + 1):
        print(('I' * i).ljust(n))


def draw_stairs(n):
    return '\n'.join(' ' * i + 'I' for i in range(n))


draw_stairs_full_stairs(7)
print(draw_stairs(7))
