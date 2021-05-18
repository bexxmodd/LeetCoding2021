- When questions asks to find common elements in strings, lists etc. Good strategy is to user 
    `Counter` from collections and `&` the entities you want to compare.


Example for finding common characters in words:

```python
def commonChars(self, A: List[str]) -> List[str]:
        cntr = collections.Counter(A[0]) # count chars of first word
        for a in A:
            cntr &= collections.Counter(a) # & will keep common chars
        return list(cntr.elements())
```

- We can sort `Counter` by first using it's method `most_common()` and then running `.sort()` method after.

Example:
```python
count = Counter(nums).most_common()
count.sort(key = lambda x: x[0])
```

- To convert `Counter` results, which are tuples, into a list of values use following:

```python
res = []
for i in count:
    val, n = i
    res.extend([val] * i)
```

-----
**Stacks** are useful in certain recursive algorithms. Sometimes you need to push
temporary data onto a stack as you recurse, but then remove them as you backtrack (for example, because
the recursive check failed).

In breadth-first search, for example, we used a **queue** to store a list of the nodes that we need to process.
Each time we process a node, we add its adjacent nodes to the back of the queue. This allows us to process
nodes in the order in which they are viewed.