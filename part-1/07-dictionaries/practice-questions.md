# Practice Questions

1. What does the code for an empty dictionary look like?

**Answer**: The code for an empty dictionary in Python looks like this `{}`

2. What does a dictionary value with a key `'foo'` and value `42` look like?

**Answer**: It looks like this in Python

```python
bar = {"foo": 42}
```

3. What is the main difference between a dictionary and a list?

**Answer**: The main difference is that a dictionary stores data as key-value pairs accessed by unique keys, while a list stores an ordered collection of elements accessed by their zero-based numerical index. 


4. What happens if you try to access a `spam['foo']` if `spam` is `{'bar': 100}`?

**Answer**: It will throw a `KeyError`

5. If a dictionary is stored in `spam`, what is the difference between the expressions `"cat" in spam` and `"cat" in spam.keys()`

**Answer**: There is no functional difference as they will evaluate to the same exact result.

6. If a dicitonary is stored in `spam`, what is is the difference between the expressions `"cat" in spam` and `"cat" in spam.values()`

**Answer**: The first expression checks if `"cat"` is a key in the dictionary, while the latter checks if `"cat"` is one of the value in the dictionary.

7. What is a shortcut for the following code?

```python
if "color" not in spam:
    spam["color"] = black
```

**Answer**: The shortcut for the following code is

```python
spam.setdefault("color", "black")
```

8. What module and function can be used to "pretty-print" dictionary values?

**Answer** The `pprint` module and its `pprint()` function

```python
from pprint import pprint

foo: dict[str, str] = {"foo": "bar"}

pprint(foo)
```