# Practice Questions

1. What is `[]`?

**Answer**: A `list`, specifically empty list.

2. How would you assign the value `'hello'` as the third value in a list stored in a variable named `spam`? (Assume `spam` contains `[2, 4, 6, 8, 10]`.) 

**Answer**: 

```python
spam[2] = "hello"
spam.insert(2, "hello")
```

For the following three questions, assume spam `contains` the list `['a', 'b', 'c', 'd']`.

3. What does `spam[int(int('3' * 2) // 11)]` evaluate to?

**Answer**: `spam[3]` would be `d` 

4. What does `spam[-1]` evaluate to?

**Answer**: `spam[-1]` would be `d`

5. What does `spam[:2]` evaluate to? 

**Answer**: `spam[:2]` would be `["a", "b"]`

For the following three questions, assume `bacon` contains the list `[3.14, 'cat', 11, 'cat', True]`.

6. What does `bacon.index('cat')` evaluate to?

**Answer**: `bacon.index['cat']` would evaluate to `1`

7. What does `bacon.append(99)` make the list value in `bacon` look like?

**Answer**: 

```python
bacon = [3.14, "cat", 11, "cat", True, 99]
```

8. What does `bacon.remove('cat')` make the list value in `bacon` look like?

**Answer**:

```python
bacon = [3.14, 11, "cat", True, 99]
```

9. What are the operators for list concatenation and list replication?

**Answer**: The operators for list concatenation is `+` and the operator for replication is `*`

10. What is the difference between the `append()` and `insert()` list methods?

**Answer**: The `append()` method adds a value to the end of the list, while `insert()` allows for flexibility and add the value at a given index

11. What are two ways to remove values from a list?

**Answer**: The two ways to remove values from a list is by index with `del` keyword that removes by index or `remove()` method that accepts a given value and removes by value.

12. Name a few ways that list values are similar to string values.

**Answer**: Both support indexing, slicing, negative indexing, `len()`, `for` loops, and the `in`/`not in` operators. They also both support concatenation (`+`) and replication (`*`).

13. What is the difference between lists and tuples?

**Answer**: Lists are mutable (can be changed after creation), while tuples are immutable (cannot be changed once created). Lists use square brackets `[]`, tuples use parentheses `()`.

14. How do you write the tuple value that has just the integer value `42` in it?

**Answer**: `(42,)` — the trailing comma is required, otherwise `(42)` is just the integer `42` in parentheses.

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

**Answer**: Use `tuple(list_value)` to convert a list to a tuple, and `list(tuple_value)` to convert a tuple to a list.

16. Variables that "contain" list values don't actually contain lists directly. What do they contain instead?

**Answer**: They contain a reference (a memory address pointing to where the list actually lives), not the list itself.

17. What is the difference between `copy.copy()` and `copy.deepcopy()`?

**Answer**: `copy.copy()` makes a shallow copy — it copies the outer list but any nested mutable objects inside are still shared with the original. `copy.deepcopy()` makes a full copy — nested objects are copied too, so nothing is shared with the original.