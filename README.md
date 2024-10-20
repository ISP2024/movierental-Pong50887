## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.


## Rationale

### 2.1 What refactoring signs (code smells) suggest this refactoring?

1. **Middle Man**: The `Movie` class was acting as a middleman by exposing methods like `get_price` and `get_rental_points`, which just delegated the logic to the `price_code`. Since only the `Rental` class needs these methods, the middleman should be eliminated by allowing `Rental` to handle the logic directly.

2. **Inappropriate Intimacy**: The `Movie` class had too much knowledge about the `price_code` logic, which is specific to the rental process. By separating them, the system has better cohesion and reduces unnecessary dependencies.

### 2.2 What design principle suggests this refactoring? Why?

The **Single Responsibility Principle (SRP)** suggests this refactoring. SRP states that a class should have only one reason to change.
