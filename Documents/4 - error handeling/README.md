In Hounaar, error handling using try-except blocks can be done as follows:

#### Try-Except Block
Syntax:
```ho
try:
    # Code that might raise an exception
except ExceptionType as e:
    # Code to handle the exception
```

Example:
```ho
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Error:", e)
```