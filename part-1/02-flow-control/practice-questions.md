# Practice Questions

1. What are the two values of the Boolean data type? How do you write them?

**Answer:** The two values of the Boolean data type are `True` and `False`.

2. What are three Boolean operators?

**Answer:** The three Boolean operators in Python are `and`, `or` and `not`.

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

**Answer:** The Boolean operators truth table:

1. Logical Operators

**Logical AND (`and`)**

The `and` operator evaluates to `True` only if both operands are `True`. If the first operand is `False`, Python returns it immediately without evaluating the second operand (short-circuit evaluation).

| Operand 1 (`A`) | Operand 2 (`B`) | Expression (`A and B`) | Python Evaluation |
| :-------------- | :-------------- | :--------------------- | :---------------- |
| `True`          | `True`          | `True and True`        | `True`            |
| `True`          | `False`         | `True and False`       | `False`           |
| `False`         | `True`          | `False and True`       | `False`           |
| `False`         | `False`         | `False and False`      | `False`           |

**Logical OR (`or`)**

The `or` operator evaluates to `True` if at least one of the operands is `True`. If the first operand is `True`, Python returns it immediately without evaluating the second operand (short-circuit evaluation).

| Operand 1 (`A`) | Operand 2 (`B`) | Expression (`A or B`) | Python Evaluation |
| :-------------- | :-------------- | :-------------------- | :---------------- |
| `True`          | `True`          | `True or True`        | `True`            |
| `True`          | `False`         | `True or False`       | `True`            |
| `False`         | `True`          | `False or True`       | `True`            |
| `False`         | `False`         | `False or False`      | `False`           |

**Logical NOT (`not`)**
The `not` operator is a unary operator that inverts the Boolean value.

| Operand (`A`) | Expression (`not A`) | Python Evaluation |
| :------------ | :------------------- | :---------------- |
| `True`        | `not True`           | `False`           |
| `False`       | `not False`          | `True`            |

---

2. Comparison Operators (Identity & Equality)

When checking equality or identity between Boolean values, they can behave like logical operations (e.g., `==` acts as XNOR, while `!=` acts as XOR).

**Equality (`==`)**

Evaluates to `True` if both operands have the same truth value.

| Operand 1 (`A`) | Operand 2 (`B`) | Expression (`A == B`) | Python Evaluation |
| :-------------- | :-------------- | :-------------------- | :---------------- |
| `True`          | `True`          | `True == True`        | `True`            |
| `True`          | `False`         | `True == False`       | `False`           |
| `False`         | `True`          | `False == True`       | `False`           |
| `False`         | `False`         | `False == False`      | `True`            |

**Inequality (`!=`) / Logical XOR**
Evaluates to `True` if the operands have different truth values. This serves as Python's Logical XOR for Booleans.

| Operand 1 (`A`) | Operand 2 (`B`) | Expression (`A != B`) | Python Evaluation |
| :-------------- | :-------------- | :-------------------- | :---------------- |
| `True`          | `True`          | `True != True`        | `False`           |
| `True`          | `False`         | `True != False`       | `True`            |
| `False`         | `True`          | `False != True`       | `True`            |
| `False`         | `False`         | `False != False`      | `False`           |

---

3. Bitwise Operators on Booleans

In Python, `bool` is a subclass of `int` (`True` behaves like `1` and `False` behaves like `0`). Therefore, bitwise operators can be used on Booleans and will return a Boolean result.

**Bitwise AND (`&`)**
Unlike `and`, the `&` operator evaluates both sides completely (no short-circuiting).

| Operand 1 (`A`) | Operand 2 (`B`) | Expression (`A & B`) | Python Evaluation |
| :-------------- | :-------------- | :------------------- | :---------------- |
| `True`          | `True`          | `True & True`        | `True`            |
| `True`          | `False`         | `True & False`       | `False`           |
| `False`         | `True`          | `False & True`       | `False`           |
| `False`         | `False`         | `False & False`      | `False`           |

**Bitwise OR (`|`)**
Unlike `or`, the `|` operator evaluates both sides completely (no short-circuiting).

| Operand 1 (`A`) | Operand 2 (`B`) | Expression (`A | B`)    | Python Evaluation |
| :-------------- | :-------------- | :------------- | :----- | ----------------- |
| `True`          | `True`          | `True          | True`  | `True`            |
| `True`          | `False`         | `True          | False` | `True`            |
| `False`         | `True`          | `False         | True`  | `True`            |
| `False`         | `False`         | `False         | False` | `False`           |

**Bitwise XOR (`^`)**

Evaluates to `True` if exactly one operand is `True`.

| Operand 1 (`A`) | Operand 2 (`B`) | Expression (`A ^ B`) | Python Evaluation |
| :-------------- | :-------------- | :------------------- | :---------------- |
| `True`          | `True`          | `True ^ True`        | `False`           |
| `True`          | `False`         | `True ^ False`       | `True`            |
| `False`         | `True`          | `False ^ True`       | `True`            |
| `False`         | `False`         | `False ^ False`      | `False`           |

4. What do the following expression evaluate to?

```python
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
```

**Answer:** The following expression evaluates to:

- `False`
- `False`
- `True`
- `False`
- `False`
- `True`

5. What are the six comparison operators?

**Answer:** The six comparison operators are:

- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `>=` Greater than or equal to
- `<` Less than
- `<=` Less than or equal to

6. What is the difference between the equal to operator and the assignment operator?

**Answer:** The equal to operator takes in two values and evaluates to a Boolean result while assignment operator is a that takes in a value and store it in a variable

7. Explain what a condition is and where you would use one.

**Answer:** Condition is a way to control the flow of a program, and I would use it to execute some block of codes only when specific criteria are met

8. Identify the three blocks in this code:

```python
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else
        print('ham')
    print ('spam')

print('Done')
```

**Answer:** Thre three blocks in the code are

- First the `if` block that prints `eggs` when `spam` is equal to (`==`) `10` and lastly prints `spam` when the inside `if` block evaluation finishes
- Second one is the nested `if` block that further checks if the `spam` is greater than (`>`) `5` and will always be executed.
- Third is the nested `else` block that prints `spam` and will never be executed

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

```python

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

```
