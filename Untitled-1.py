# Author: Vivi Du
# This program demonstrates the concept of operator precedence in Python.

def main():
    """Main function to demonstrate operator precedence."""
    print("Welcome to the Operator Precedence Demo!")

    # Example 1: Without parentheses
    result1 = 3 + 4 * 2
    print("Example 1: 3 + 4 * 2 = ", result1)
    # Explanation: Multiplication (*) has higher precedence than addition (+)
    # So, the expression is evaluated as 3 + (4 * 2) = 11

    # Example 2: With parentheses
    result2 = (3 + 4) * 2
    print("Example 2: (3 + 4) * 2 = ", result2)
    # Explanation: Parentheses take the highest precedence.
    # The expression is evaluated as (3 + 4) * 2 = 14

    # Example 3: Exponentiation and multiplication
    result3 = 2 ** 3 * 4
    print("Example 3: 2 ** 3 * 4 = ", result3)
    # Explanation: Exponentiation (**) has higher precedence than multiplication (*)
    # The expression is evaluated as (2 ** 3) * 4 = 8 * 4 = 32

    # Example 4: Division, addition, and subtraction
    result4 = 10 - 4 + 2 / 2
    print("Example 4: 10 - 4 + 2 / 2 = ", result4)
    # Explanation: Division (/) is evaluated first, then addition (+) and subtraction (-) left to right
    # The expression is evaluated as 10 - 4 + (2 / 2) = 10 - 4 + 1 = 7

    # Example 5: Logical operators
    result5 = True or False and False
    print("Example 5: True or False and False = ", result5)
    # Explanation: Logical AND (and) has higher precedence than OR (or)
    # The expression is evaluated as True or (False and False) = True or False = True

    # Example 6: Mixing comparison and logical operators
    result6 = 5 > 3 and 2 < 4 or 3 == 5
    print("Example 6: 5 > 3 and 2 < 4 or 3 == 5 = ", result6)
    # Explanation: Comparison operators (>, <, ==) are evaluated first
    # Then AND is evaluated, and finally OR
    # The expression is evaluated as (True and True) or False = True or False = True

    print("\nThank you for exploring operator precedence!")

if __name__ == "__main__":
    main()
