# Si hou zi, what is the correct way to define static class variable?
letter_list = ['', '*', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

class Solution(object):
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
    
        if len(digits) == 0:
            return []
        if len(digits) == 1:  # Two ifs seems ugly. Any way to avoid this if?
            return list(letter_list[int(digits[0])])

    
        digits_length = len(digits)
        previous_result = self.letterCombinations(digits[:(digits_length - 1)])
        current_str = letter_list[int(digits[digits_length - 1])]
    
        result = []
        for previous in previous_result:
            for current in current_str:
                result.append(previous + current)
    
        return result
