given an array of integers and value `x` find if sum of two numbers equal `x` in O(n) runtime.

```
arr = [4, 2, 3, 4, 5, 9, 1]
x = 9
```

```python
res = {}
for i, n in enumarte(arr):
    diff = x - n
    if diff in res.keys():
        return [i, res[diff]] # diff goes as key cur index as val
    else:
        res[diff] = i
return None
```