

### Hounaar Language

Hounaar is a beginner-friendly and minimalist programming language designed for ease of use and quick scripting.

### Installation

To run Hounaar, follow these steps:
1. Clone the Hounaar repository from GitHub.
    ```bash
    git clone https://github.com/username/Hounaar.git
    ```
2. Navigate to the cloned directory.
    ```bash
    cd Hounaar
    ```
3. Run the Hounaar interpreter.
    ```bash
    python interpreter.py your_code.ho
    ```

### Running Hounaar Code

To execute a Hounaar code file (e.g., `your_code.ho`), use the Hounaar interpreter as follows:
```bash
python interpreter.py your_code.ho
```

### Variables Definition

Variables in Hounaar are declared using a straightforward syntax:
```ho
Variable_Name = Initial_Value
```
Example:
```ho
name = "John"
age = 25
```



### Conditionals (if-else)

Hounaar supports basic conditional statements for decision-making. Here's how you use if-else in Hounaar:

Syntax:
```ho
if condition:
    code_block
else:
    code_block
```

Example:
```ho
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```
In Hounaar, the 'else if' condition is represented as 'elif'. Here's how it works:

### Conditional (if-elif-else)

Syntax:
```ho
if condition:
    code_block
elif condition:
    code_block
else:
    code_block
```

Example:
```ho
if score >= 90:
    print("A Grade")
elif score >= 80:
    print("B Grade")
elif score >= 70:
    print("C Grade")
else:
    print("Below C Grade")
```

Alright, for loops and while loops in Hounaar look like this:

### For Loop
Syntax:
```ho
for variable_name from start to end:
    code_block
```

Example:
```ho
for i from 1 to 5:
    print(i)
```

#### While Loop
Syntax:
```ho
variable = initial_value
while condition:
    code_block
    variable = variable + 1  # Increment or decrement the variable
```

Example:
```ho
num = 0
while num < 5:
    print(num)
    num = num + 1
```

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

To define an array in Hounaar, you can use square brackets `[ ]` to encapsulate a list of elements.

#### Array Definition
Syntax:
```ho
array_name = [element1, element2, element3, ...]
```

Example:
```ho
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed_array = [1, "hello", True, 3.14]
```
This creates an array `mixed_array` with elements of different data types: an integer, a string, a boolean, and a floating-point number.


```ho
empty_array = []
```
An empty array `empty_array` is created with no elements inside the square brackets.


```ho
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
This defines a matrix `matrix` where each element is an array itself, resulting in a 3x3 matrix structure.

Sure, here's an updated section focusing on functions:

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

Absolutely! Here's a guide on defining classes and understanding object-oriented programming (OOP) concepts in Hounaar:

### Object-Oriented Programming in Hounaar

Hounaar supports basic object-oriented programming principles through classes and objects.

#### Defining a Class

To define a class, use the `class` keyword followed by the class name:

```ho
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")
```

This creates a `Person` class with a constructor (`__init__`) and a `greet` method.

#### Creating Objects (Instances)

To create an instance of a class (an object), use the class name followed by parentheses:

```ho
alice = Person("Alice", 25)
bob = Person("Bob", 30)

alice.greet()  # Output: Hello, my name is Alice and I am 25 years old.
bob.greet()    # Output: Hello, my name is Bob and I am 30 years old.
```

This creates instances of the `Person` class for Alice and Bob and calls the `greet` method for each.

#### Inheritance

Hounaar also supports inheritance, allowing classes to inherit attributes and methods from other classes:

```ho
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(self.name + " with ID " + str(self.student_id) + " is studying.")
```

Here, the `Student` class inherits from the `Person` class and adds a `study` method.

#### Example Use Cases:

##### Creating Persons:
```ho
alice = Person("Alice", 25)
alice.greet()  # Output: Hello, my name is Alice and I am 25 years old.
```

##### Creating Students:
```ho
bob = Student("Bob", 20, 12345)
bob.greet()    # Output: Hello, my name is Bob and I am 20 years old.
bob.study()    # Output: Bob with ID 12345 is studying.
```

#### Encapsulation and Abstraction

Hounaar supports encapsulation by allowing attributes to be hidden or accessed through methods, enabling abstraction for better data security and code readability.


### Functions references

|Functions      | Description                                               |
|---------------|-----------------------------------------------------------|
| fprintf       | Formats and writes data to a file handle.                   |
| scanf         | Reads formatted data from the standard input.               |
| strcmp        | Compares two strings and returns their relationship.        |
| strcpy        | Copies a string to another.                                 |
| strlen        | Returns the length of a string.                             |
| round         | Rounds a floating-point number to the nearest integer.      |
| max           | Returns the maximum value among the provided arguments.    |
| min           | Returns the minimum value among the provided arguments.    |
| sum           | Computes the sum of elements in an array or iterable.      |
| sorted        | Returns a sorted list of elements from an iterable.        |
| pow           | Raises a number to a specified power.                      |
| format        | Formats a specified value according to the given format.   |
| any           | Returns True if any element in an iterable is True.         |
| all           | Returns True if all elements in an iterable are True.       |
| enumerate     | Returns an enumerate object, providing index-value pairs.  |
| isdigit       | Checks if a character is a numeric digit.                   |
| isalpha       | Checks if a character is an alphabetic character.           |
| islower       | Checks if a character is a lowercase letter.                |
| isupper       | Checks if a character is an uppercase letter.               |
| isspace       | Checks if a character is a whitespace character.            |
| abs           | Returns the absolute value of a number.                     |
| bin           | Converts an integer to a binary string.                     |
| hex           | Converts an integer to a hexadecimal string.                |
| oct           | Converts an integer to an octal string.                     |
| reversed      | Returns a reverse iterator of a sequence.                   |







