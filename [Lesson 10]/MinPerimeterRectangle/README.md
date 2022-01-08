## Question

URL : https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/start/

## code
```python
def solution(number):
    for i in range(int(number ** 0.5), 0, -1):
        if number % i == 0:
            return 2 * (number // i + i)
```

## Result

![image](https://user-images.githubusercontent.com/84619866/148629671-1c4f0c33-f449-4de3-a599-9c17d7731635.png)
