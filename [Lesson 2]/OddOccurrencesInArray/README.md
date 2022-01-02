## Question

https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/start/

## code
```python
from collections import Counter

def solution(array):
    array = Counter(array)
    for i in array.keys():
        if array[i] % 2 != 0:
            return i
```

## Result

![image](https://user-images.githubusercontent.com/84619866/147865859-340064dd-be9c-4582-8722-fb36a3885381.png)
