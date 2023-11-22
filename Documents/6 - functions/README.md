### Functions in Hounaar

Functions in Hounaar allow you to encapsulate reusable blocks of code.

#### Defining a Function

To define a function, use the `function` keyword followed by the function name and its parameters:

```ho
function greet(name):
    print("Hello, " + name)
```

This defines a function named `greet` that takes a `name` parameter and prints a greeting.

#### Returning Values

Functions can return values using the `return` statement:

```ho
function add(a, b):
    return a + b
```

The `add` function takes two parameters (`a` and `b`) and returns their sum.

#### Conditional Logic in Functions

Functions can include conditional statements:

```ho
function absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num
```

This `absolute_value` function returns the absolute value of a number using an `if-else` statement.

#### Example Use Cases:

##### Greeting Example:
```ho
greet("Alice")  # Output: Hello, Alice
```

##### Addition Example:
```ho
result = add(5, 3)  # Result: 8
```

##### Absolute Value Example:
```ho
pos_value = absolute_value(10)  # Result: 10
neg_value = absolute_value(-7)  # Result: 7
```