class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            if char == 'I':
                val = 1
            elif char == 'V':
                val = 5
            elif char == 'X':
                val = 10
            elif char == 'L':
                val = 50
            elif char == 'C':
                val = 100
            elif char == 'D':
                val = 500
            else:
                val = 1000
            
            total += val if val >= prev_value else -val
            prev_value = val
        
        return total