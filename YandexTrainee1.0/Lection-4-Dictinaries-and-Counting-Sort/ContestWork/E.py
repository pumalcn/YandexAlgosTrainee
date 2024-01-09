def get_pyramid_max_height() -> int:
    pyramid_blocks = {}
    for i in range(int(input())):
        width, height = map(int, input().split())
        pyramid_blocks[width] = max(pyramid_blocks.get(width, height), height)

    return sum(pyramid_blocks.values())
