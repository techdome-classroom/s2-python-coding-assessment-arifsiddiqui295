def isValid(s: str) -> bool:
    # Dictionary to store matching pairs
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    # Traverse each character in the string
    for char in s:
        if char in bracket_map:
            
            top_element = stack.pop() if stack else '#'
            
            
            if bracket_map[char] != top_element:
                return False
        else:
            
            stack.append(char)
    
   
    return not stack


print(isValid("()"))       # Output: True
print(isValid("()[]{}"))   # Output: True
print(isValid("(]"))       # Output: False
