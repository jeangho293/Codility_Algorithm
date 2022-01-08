def solution(number):
    for i in range(int(number ** 0.5), 0, -1):
        if number % i == 0:
            return 2 * (number // i + i)