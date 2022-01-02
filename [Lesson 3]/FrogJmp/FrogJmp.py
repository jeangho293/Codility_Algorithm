def solution(X, Y, D):
    need_distance = Y - X
    if need_distance % D == 0:
        return need_distance // D
    else:
        return need_distance // D + 1