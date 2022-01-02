## Question

URL : https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/start/

## code
```python
def solution(X, Y, D):
    need_distance = Y - X
    if need_distance % D == 0:
        return need_distance // D
    else:
        return need_distance // D + 1
```

## Result

![image](https://user-images.githubusercontent.com/84619866/147865945-992aaa78-bba2-4723-a7b1-c62adfc7fb64.png)