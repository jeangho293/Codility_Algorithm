## Question

URL : https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/start/

## code
```python
def solution(A):
    for i, value in enumerate(sorted(A)):
        if i + 1 != value:
            return i + 1
    return len(A) + 1   # 만약 [1] 일 경우, 2가 빠져있다는 의미므로 이에 대한 예외처리
```

## Result

![image](https://user-images.githubusercontent.com/84619866/147880060-7d640fb4-b72a-4344-b64f-3475434f514d.png)
