'''
Function answer(heights)
Input : A list of integers ex. [1, 3, 5, 4, 5, 1]
Output: A integer representing the amount of water built up if it rained.
Method: Find the max height and its index and approach that index from both sides, filling in water as possible.
Runtime: O(n) Linear
Constraints: len(Input) must be between 1 and 9000. The value of each element in the input must be between 1 and 100000. Behavior may be undefined outside of this zone.
'''
def answer(heights):

    #Find index of max. We don't care about duplicate values of the max. We just care about what direction to approach it from.
    index_max = heights.index(max(heights))

    retained_water = 0
    levee_height = 0
    length_of_input = len(heights)
    
    #Approach the max from both sides, filling in water as we go.
    #From the left to the right
    for x in range(0, index_max):
        #If the current levee_height is lower than the value...
        if (levee_height < heights[x]):
            #Establish a new levee
            levee_height = heights[x]
            continue
        #If the current levee_height is above the value...
        else:
            #Fill this area in up to the height of the levee
            retained_water += levee_height - heights[x]
            continue

    #Reset the levee_height
    levee_height = 0
    
    #From the right to the left. See previous loop for comments
    for x in range(length_of_input-1, index_max, -1):
        if (levee_height < heights[x]):
            levee_height = heights[x]
            continue
        else:
            retained_water += levee_height - heights[x]
            continue

    return retained_water          
    
