## Question

https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/start/

## code

```python
from collections import deque


def solution(A, K):
    queue = deque(A)
    if not queue:   # 해당 리스트가 비어 있을 경우, 빈 배열 출력
        return []
    # K가 A의 길이보다 클수도 있으니 나머지만큼만 구함.
    for i in range(len(A) - (K % len(A))):
        queue.append(queue.popleft())
    return list(map(int, queue))
```

## Result

![image](https://user-images.githubusercontent.com/84619866/147849471-c2cba789-1992-4b5d-8d36-0603fe63861b.png)
