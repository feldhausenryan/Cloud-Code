'''
Function answer(n)
Input : An integer ex. 1, 8, 1000
Output: An integer representing the the minimum number of squares that sum to the input.
ex. 24 = 16(4*4) + 4(2*2) + 4(2*2) ::: which is three numbers  16, 4, 4 -> 1+1+1 = 3
Method: Take the square root of the number using pow(number, .5). Then the result is rounded to obtain the largest pad size for the coins_remaining. Repeat this until there are no more coins.
Runtime: O(log(pow)) Logarithmic calls to the power function.
Constraints: Behavior is only defined for 1 <= n <= 10000. The function may not work outside of this bound.
'''
def answer(n):
    #Declare helper variables
    pad_count = 0
    coins_left = n

    #While we still have coins left...
    while(coins_left != 0):
        #Buy the largest pad we can...
        coins_left -= pow(int(pow(coins_left, .5)), 2)
        #Increment the pad count
        pad_count += 1

    #Return answer
    return pad_count
