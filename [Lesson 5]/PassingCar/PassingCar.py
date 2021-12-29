def solution(A):
    cnt, result = 0, 0
    for i in A:
        if i == 0:
            cnt += 1
        else:
            result += cnt
    return result if result <= 1000000000 else -1