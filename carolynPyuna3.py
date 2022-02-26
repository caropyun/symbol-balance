###
# CS 3C Advanced Data Structures and Algorithms in Python
# Description:  This program is the test driver for checking if symbol is balanced.
#               User input: String comprising of ([{ and their counterparts
#               Returns 0 if unbalanced, 1 if balanced
# Time and Space Complexity: O(n)
# Solution File: carolynPyuna3.py
# Date:  1/25/22
#

from carolynPyunstack import Stack


def main():
    S = Stack.create_stack()  # Create stack

    user_input = ""
    print("Enter 'end' to stop")
    matches = {")": "(", "]": "[", "}": "{"}  # dictionary to match

    while user_input != "end":
        # Take in user input until "end"
        user_input = input("Symbols: ").lower().replace(" ", "")
        if user_input == "end":
            break

        is_balanced = 0
        error = False
        if len(user_input) % 2 == 1:  # If odd length, not balanced
            is_balanced = 0
        else:
            for char in user_input:
                if char in "({[":
                    S.push(char)
                elif char in ")}]":
                    if S.pop() == matches[char]:  # If matches pair
                        is_balanced = 1
                    else:
                        is_balanced = 0
                        break
                else:  # Error if not symbols
                    error = True
                    is_balanced = 0
                    break

        print(f"Output {is_balanced}")
        S.delete_stack()


if __name__ == '__main__':
    main()

'''
Enter 'end' to stop
Symbols: ([|)]
Output 0
Symbols: () (() [()])
Output 1
Symbols: {{([][])}()}
Output 1
Symbols: hello
Output 0
Symbols: alla
Output 0
Symbols: [[[[[[[[}}}}}}}}
Output 0
Symbols: end
'''
