# Practice Questions

1. What keys can you press if your Python program is stuck in an infinite loop?

**Answer**: `CTRL + C` in Windows or `CMD + C` in Mac

2. What is the difference between `break` and `continue`?

**Answer**:

- `break` is used to exit in the loop immediately
- `continue` is used to skip the current iteration of the loop

3. What is the difference between `range(10)`, `range(0, 10)` and `range(0, 10, 1)`

**Answer**: There is no difference between the three as they produce the same output

4. Write a short program that prints the numbers `1` to `10` using a `for` loop. Then, write an equivalent program that prints the numbers `1` to `10` using a `while` loop

**`for`** 
```python
for i in range(1, 11):
    print(i)
```

**`while`**
```python
counter = 1
while counter <= 10:
    print(counter)
    counter += 1
```

5. If you had a function named `bacon()` inside a module named `spam` how would call it after importing `spam`

```python
import spam

spam.bacon()
```

