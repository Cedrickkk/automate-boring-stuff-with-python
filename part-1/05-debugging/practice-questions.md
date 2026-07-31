# Practice Questions

1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

**Answer**: 

```python
assert spam >= 10
```


2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different. (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'.)

**Answer**: 

```python
assert eggs.lower() != bacon.lower()
```

3. Write an assert statement that always triggers an AssertionError.

**Answer**: 

```python
assert False
```

4. What two lines must your program have to be able to call logging.debug()?

**Answer**:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

5. What two lines must your program have to make logging.debug() send a logging message to a file named program_log.txt?

**Answer**: 

```python
import logging

logging.basicConfig(filename="program_log.txt", level=logging.DEBUG)
```


6. What are the five logging levels?

**Answer**: The five logging levels are:

- `DEBUG`: Low-level details used for diagnosing problems (e.g., "Variables x is currently 5")
- `INFO`: General confirmation that things are working as expected (e.g., "Database connection successful")
- `WARNING`: An indication that something unexpected happened, but the program is still working (e.g., "Disk space low").
- `ERROR`: A serious problem occurred, and the program was unable to perform a specific function (e.g., "Failed to save file")
- `CRITICAL`: A fatal error indicating that the program itself may be unable to continue running (e.g., "Out of memory / Application crash")

7. What line of code can you add to disable all logging messages in your program?

**Answer**: 

```python
logging.disable()
```

8. Why is using logging messages better than using print() to display the same message?

**Answer**: Because it is easy to disable or change the severity of all logging messages with one line of code, without manually deleting individual `print()` statements.

9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

**Answer**: 

- **Step In**: moves into the next line of code, entering functions to inspect them.
- **Step Over** executes the next line of code normally without entering into functions.
- **Step Out** runs the remainder of the current function quickly and returns to the caller.

10. After you click Continue, when will the debugger stop?

**Answer**: The debugger will stop only when it hits a breakpoint, encounters an unhandled error, or the program reaches its end.

11. What is a breakpoint?

**Answer**: A breakpoint is an intentional stopping point set on a specific line of code that pauses program execution for debugging.

12. How do you set a breakpoint on a line of code in Mu?

**Answer**: To set a breakpoint in Mu, click the margin area directly to the left of the line number where you want the code to pause.