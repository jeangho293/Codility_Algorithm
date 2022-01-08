def solution(number):
    cnt = 0
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            cnt += 2
    return cnt - 1 if number **0.5 == int(number **0.5) else cnt