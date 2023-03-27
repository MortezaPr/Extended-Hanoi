moves = []


def hanoi(source, auxiliary, destination, n):
    global moves
    if n == 1:
        moves.append((source, destination))
        return
    hanoi(source, destination, auxiliary, n - 1)
    moves.append((source, destination))
    hanoi(auxiliary, source, destination, n - 1)


def extended_hanoi(a, b, c, n):
    global moves
    if n == 1:
        moves.append((c, b))
        moves.append((a, c))
        moves.append((b, a))
        moves.append((b, c))
        moves.append((a, c))
    else:
        extended_hanoi(a, b, c, n - 1)
        hanoi(c, a, b, 3 * n - 2)
        moves.append((a, c))
        hanoi(b, a, c, 3 * n - 1)
    return moves
