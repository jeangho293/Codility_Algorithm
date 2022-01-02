def solution(A):
    for i, value in enumerate(sorted(A)):
        if i + 1 != value:
            return i + 1
    return len(A) + 1   # 만약 [1] 일 경우, 2가 빠져있다는 의미므로 이에 대한 예외처리
