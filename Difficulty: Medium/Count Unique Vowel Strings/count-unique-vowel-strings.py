from math import factorial
class Solution:
    def vowelCount(self, s):
        #code here
        vowels = {'a':0,'e':0,'i':0,'o':0,'u':0} # Created dictionary to count vowels occuring
        all_zero = True # flag to check whether string contains vowels or not
        unique_vowel = 0 # to calculate the factorial
        
        for char in s:
            if char in vowels:
                vowels[char] += 1
                all_zero = False
        
        if all_zero:
            return 0 # since the string does not contain vowels, it cannot be arranged
        
        for vowel in vowels: # to calculate the unique vowels
            if vowels[vowel] > 0:
                unique_vowel += 1
        factorial_val = factorial(unique_vowel) # calculate the multiplier
        result = factorial_val
        
        # since the unique vowels gave the types of arrangement we can make,
        # now we will be looking to the multiplier since each character have to considered
        # as a unique character
        for vowel in vowels: 
            if vowels[vowel] > 0:
                result *= vowels[vowel]
        
        return result