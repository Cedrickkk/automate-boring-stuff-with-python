# Practice Questions

**1. Why are functions advantageous to have in your programs?**

Functions are like modular building blocks of your program. They:

* Reuse code without duplicating it
* Improve readability and maintainability by keeping related code together
* Reduce repetition and increase productivity
* Make it easier to test, debug, and extend individual pieces of functionality

Think of a function like a recipe: each time you make that dish, you repeat the steps in the same order. A function does the same thing. You can call it multiple times with different inputs, and it'll always behave the same way.

**2. When does the code in a function execute: when the function is defined or when the function is called?**

The code inside a function executes **only when the function is called**. Define the function as many times as you want; create a variable with the same value every time, and even use a loop to create similar functions. None of this execution happens until the `function_name()` part (or just the function name followed by parentheses) appears in your code.

For example:
```
def my_function():
    print("Hello!")

my_function()  # This is where the code inside my_function() executes
```

**3. What statement creates a function?**

The statement that creates a function is `def function_name(parameters):`. Here, `function_name` is the name of your function, and `parameters` are any inputs you want to accept when calling that function.

For example:
```python
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")  # This calls the function with input name='Alice'
```

**4. What is the difference between a function and a function call?**

A function is a block of code that performs a specific task. A **function call**, on the other hand, is when you execute that code by using its name followed by parentheses.

Think of a function like a recipe and "calling it" to cook that dish: "I want to make my favorite apple pie!" vs. "Give me a slice of this pie."

**5. How many global scopes are there in a Python program? How many local scopes are there?**

In Python, there's only **one global scope**, which applies throughout the entire program. However, each function call has its own **local scope**. This means that within a single function call:

- Variables defined **outside of any function** have access to both the global and local scopes.
- Variables defined **within a function** have only **local scope**.

Think of variables like labeled boxes: you can store something in the global "house" (defined outside any function), or create an entirely separate box within a function.

**6. What happens to variables in a local scope when the function call returns?**

When a function finishes executing, its local scope disappears **completely**, taking all its defined variables with it. The values stored in those variables remain within their original "scope," but it's as if nothing ever existed inside that local scope.

Here's an example:
```python
def my_function():
    x = 10

my_function()
print(x)  # Raised NameError, because 'x' is no longer in scope!
```

**7. What is a return value? Can a return value be part of an expression?**

A **return value** (or result) is what your function outputs or "gives back" when called.

A `return` statement can indeed be the last line of a function, so you're technically including it in an expression that includes the variable or expression returned from that function. For example:
```python
def my_function():
    return 5

result = my_function()
print(2 * result)  # Prints "15" (correct!)
```

**8. If a function does not have a return statement, what is the return value of a call to that function?**

In Python, if you omit an explicit `return` statement from the end of your function, it will:

- **Default to returning `None`**.
- If you want a different value (a pseudo "non-return") in such cases, explicitly include a `raise Exception()` or similar within that scope.

Think of it like a recipe: if you leave off the final step of serving food, the dish won't magically appear on your plate!

Here's an example:
```python
def my_function():
    pass  # No return statement

result = my_function()
print(result)  # Prints "None"
```

**9. How can you force a variable in a function to refer to the global variable?**

You can create the same variable name in both your local scope within the function and in the global scope **outside the function**, or instead use the `global` keyword before defining that variable as part of its assignment.

Here's an example:
```python
x = 10  # Global variable

def foo():
    x = 100  # Creates a new, local 'x' within foo() -> don't use this!
    global x   # Force reference to the original, glocal variable

foo()
print(x)  # Prints "10", not "100"
```

Or, as an alternative:
```python
x = 10  # Global variable

def foo():
    nonlocal x  # Tell Python: while this function is a local name,
               # still treat it like the global variable's name.
    x = 100

foo()
print(x)  # Prints "100"
```

**10. What is the data type of None?**

In Python, `None` has a special data type all its own: **`NoneType`** (which doesn't appear anywhere in your code editor!). Use `'None'` to represent the absence of any data object.

Here's an example:
```python
x = None  # x is now NoneType

print(isinstance(x, NoneType))  # True!
```

**11. What does the import areallyourpetsnamederic statement do?**

Python has no built-in `import areallyourpetsnamederic`. It seems like a random Python-related question!

If you meant something else (e.g., related to naming conventions or importing specific modules), be sure let me know, and I'll help clarify!




Let me provide answers to the last four questions.

**12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?**

If `spam` is your Python file:

```python
import spam

spam.bacon()
```

Or, if you really wanted an `areallyourpetsnamederic` statement (which is almost undoubtedly a joke), I'd say that statement doesn't do anything:


```python
# or is this what I mean?
import areallyourpetsnamederic as aprn # import with a module name!

aprn.bacon()
```

**13. How can you prevent a program from crashing when it gets an error?**

When writing Python programs, always remember to **wrap code in try/except blocks**, where try catches (for expected conditions) and excepts handle errors:

```python
try:
    # Some part of the program may raise errors here.
except YourSpecificError:
    print("Try again or use a different option")
```

Or:

```python
def my_function():
    try:
        do_something()
    except Exception as e:
        error_handling_process(e)

my_function()
```
Here, replace your "some part of the program" with actual code.

Also keep this pattern in mind when using Python's async/await syntax for awaiting non-blocking requests or functions.

Here’s a general example of writing basic exception handling practices:

```python
try:
    # some execution that may raise errors
except Exception as e:
    print(f'The execution failed because: {e}')
    # You could use the same approach to ask what your user inputs so you can recover.
elif OtherException:
    # handle another type of error
else:
    # everything went well, happy dance?
```
 
**14. What goes in the try clause? What goes in the except clause?**

* Go in the **try clause**: The lines that explicitly make your Python program do stuff and risk raising errors. Code within a `try` block is "executing." Try to focus on execution inside this part.
	+ This line might not get executed because it could fail somewhere down the road (either immediately or eventually).
* Go in the **except clause**: The lines that take care of what happens when stuff like, well, fails above does.

By using an `else` block after a try, you'll be able to ensure code is only executed if the previous part was successful; otherwise, they both remain empty.

For example:

```python
def func():
    try:
        variable = 'some valid value'
        other_value = 5 / 0
    except ZeroDivisionError:
        pass
    else:
        print('Value retrieved with success')
    
func()

```

Note that `else` is used to define cleanup, error handling without a specified type of exception; however you can use it for more flexibility.



**15. Why might a function return the same number every time it is called if pseudo-randomness or hardcoded values are involved?**

A function returns **the same number** because it has either:

a) Pseudo-randomness

or b) hardcoded values.

When you do something like: 

```python
import random as r


def calculate_pi():
    num_samples = 1000000
    pi_estimate = 0.0

    for i in range(num_samples):
        x, y = r.uniform(-1, 1), r.uniform(-1, 1)
        if (x * x) + (y * y) <= 1:
            pi_estimate += 4

    return pi_estimate / num_samples
```
Then every time it’s called, because you used uniform between `-1` and `+1`, the results won’t be random but predictable.

It works like this: 
- For a given pair of numbers that fall under an input defined interval,
  (`x, y`) that satisfies `(x * x) + (y * y) <= 1`
  you're incrementing a counter. When those numbers satisfy the inequality in order to be within a one unit wide circle
   centered on your current origin (0,0).

Since those increments don't vary, they all end at the same sum over “num_samples”

In another case where this function is hard coded, like for example returning 5:

```python
def calculate_pi():
    return 5

```

Then it just does not call its own logic. It simply returns predefined number instead of asking itself questions to solve what needs to be solved (with a calculated guess)
