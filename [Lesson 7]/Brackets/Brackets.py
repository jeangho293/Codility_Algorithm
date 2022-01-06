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