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

--------

You can check if one string is a subset of another by turning them into `set` and doing equal or less comparison:

```python
s1 = set(s1)
s2 = set(s2)
if s1 <= s2: # if looking for proper subset use '<'
    print('s1 is substring of s2')
```

------
When asked to find a missing number in a list of consecutive integers, we need to find the difference of sum of _n_ consecutive numbers and sum of given list and return the difference. Formula to find sum of _n_ consecutive numbers is _n(n+1) // 2_. Example:

```python
def missingNumber(self, nums: List[int]) -> int:
    S = len(nums) * (len(nums) + 1) // 2 # expected sum
    return S - sum(nums)
```

------
when asked to find a number that appears only ones in a list good approaches are to use `Counter` and return value which has counter == 0, or append items to set on first iteration and remove it if we encounter same item again. This will leave only numbers that appear ones. Example:

```python
def singleNumber(nums: List[int]) -> List[int]:
    count = Counter(nums)
    return [x for x in count if count[x] == 1]
```

--------
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

The points of interest are the peaks and valleys in the given graph. We need to find the largest peak following the smallest valley. We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.

```python
def maxProfit(self, prices: List[int]) -> int:
    maxprofit = 0;
    minprice = sys.maxsize
    for p in prices:
        if p < minprice:
            minprice = p
        elif p - minprice > maxprofit:
            maxprofit = p - minprice
    return maxprofit
```