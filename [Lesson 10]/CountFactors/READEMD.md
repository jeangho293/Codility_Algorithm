## Question

URL : https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/start/

## code
```python
def solution(number):
    cnt = 0
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            cnt += 2
    return cnt - 1 if number **0.5 == int(number **0.5) else cnt
```

## Result

![image](https://user-images.githubusercontent.com/84619866/148629434-851ab130-a9d0-47a8-b445-e2f8592fa28e.png)
