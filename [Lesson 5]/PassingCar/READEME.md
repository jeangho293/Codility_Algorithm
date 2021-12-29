## Question

URL : https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

## code
```python
def solution(A):
    cnt, result = 0, 0  # cnt는 서로 겹칠 수 있는 차의 수, result는  총 교차 횟수
    for i in A:
        if i == 0:
            cnt += 1
        else:
            result += cnt
    return result if result <= 1000000000 else -1   # 예외 케이스
```

## Result

![image](https://user-images.githubusercontent.com/84619866/147669446-4c7ebf2b-ac9e-49c7-ac8e-1079b59fba7c.png)
