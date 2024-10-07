class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to their corresponding integer values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Traverse the string from right to left
        for char in reversed(s):
            curr_value = roman_map[char]
            
            # If current value is less than the previous value, subtract it
            if curr_value < prev_value:
                total -= curr_value
            else:
                # Otherwise, add it to the total
                total += curr_value
            
            prev_value = curr_value
        
        return total
