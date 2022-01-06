## Question

URL : https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/start/

## code
```python
from collections import deque


bracket = {'{': '}', '(': ')', '[': ']'}    # 괄호 dictionary
def solution(array):
    queue, stack = deque(array), []
    while queue:
        if not stack:
            stack.append(queue.popleft())
        try:
            if bracket[stack[-1]] == queue[0]:
                stack.pop()
                queue.popleft()
            else:
                stack.append(queue.popleft())
        except:
            break
    return 0 if stack else 1
```

## Result

![image](https://user-images.githubusercontent.com/84619866/148425786-a6c652c6-e1f8-47c3-b2e7-12cddc1555e7.png)
