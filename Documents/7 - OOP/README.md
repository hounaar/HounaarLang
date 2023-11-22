

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