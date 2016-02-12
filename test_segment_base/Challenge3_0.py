'''
Function answer(namess)
Input : A list of strings e.g. (string list) ["value 1", "value 2"]
Output: (string list) The list sorted by (primary == alphabetic sum, secondary == lexicographic) descending
alphabetic sum == "a=1 b=2 c=3 ..." "abc"==1+2+3==6
Method: Define a custom key function returning the primary and secondary keys. Then call sort(keyfunction)
Runtime: O(nlog(n) + m) m = total number of characters in the list
'''
def answer(names):
    #ensure that the original list is unchanged
    copied_names = copy.copy(names)
    #define out custom key function.
    #Input : A string
    #Output: A primary and secondary key (tuple)
    #Method: Sum up the character values and store that as primary. Keep the original string as secondary
    #Runtime: O(n) n = length of string
    def stringValue(string):
        running_sum = 0
        for character in string:
            running_sum += ord(character)-96
        return (running_sum,string)
    #call normal sort function with the custom key function and reverse=True for descending order
    copied_names.sort(key=stringValue, reverse=True)
    #retun the result
    return copied_names
    
