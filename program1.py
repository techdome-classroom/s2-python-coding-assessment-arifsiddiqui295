def isValid(s: str) -> bool:
    # Dictionary to store matching pairs
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    # Traverse each character in the string
    for char in s:
        if char in bracket_map:
            # Pop the top element from the stack if it's not empty; else assign a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the top element doesn't match the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            
            stack.append(char)
    
   
    return not stack


print(isValid("()"))       # Output: True
print(isValid("()[]{}"))   # Output: True
print(isValid("(]"))       # Output: False
