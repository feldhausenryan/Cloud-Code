#Function answer(x, y, n)
#Input 1: Integer x from 1 to n
#Input 2: Integer y from 1 to n
#Input 3: Integer n from 3 to 40
#Output : String representing the number of combinations of ordering a list of range(0, n),
#such that the ascending numbers from one side sum to x, while the other side sums to y.
#Example : answer(2, 2, 4). range = [0, 1, 2, 3] some valid lists could be [0, 3, 1, 2] or [1, 3, 0, 2] Output here would be 6
#Example2: answer(1, 10, 10). range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] the only valid list is [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] Output here would be 1
#Method  : using a base_table (the solutions to answer(x, y, 3). The table for answer(x, y, 3 + 1...)
#can be quickly derived. First sum the rows in the n table to obtain the first row/column for the n+1 table
#After obtaining the first row there exists a diagonal relation from (x, y, n) to (x-1, y+1, n) which is a scalar based off
#of the x and y values. Using these two rules the tables for n can be progressively filled until the table for the desired n is reached.
#at that point just query the table for the desired x and y.
#Runtime : O(n^3) for Input 3 = n.
#Performance can be increased to linear O(n) by caching the ~800 initial row values for n from 3 to 40. Marginal improvements can also be made because x and y can be flipped
#Constraints: Output may not work for inputs outside of listed bounds
def answer(x, y, n):
    #We can't see more than is physically possible
    if (x + y > n + 1):
        return 0
    #We can't see less than is physically possible
    if (x + y < 3):
        return 0
    #Solutions for all anser(x, y, n=3). The remaining solutions are built off of this table
    base_table = [[0, 1, 1],
                  [1, 2, 0],
                  [1, 0, 0]]
    base_n = 3
    #If our desired table is bigger than the current one...
    while (n > base_n):
        #Make a new table...
        base_n += 1
        empty_row = [0]*base_n
        new_base_table = []
        #Fill the new table in with 0s...
        for value in range(0, base_n):
            new_base_table.append(empty_row[:])
        #Fill in the first column by summing up the rows of the previous table
        for row_index in range(0, len(base_table)):
            row = base_table[row_index]
            new_base_table[row_index+1][0] = sum(row)
        #Fill in the individual values for the new table by using the diagonal relation.
        #The complicated bounds are set to avoid division by zero and overwriting of the first column
        for col in range(1, base_n):
            for row in range(0, base_n):
                if (col + row > base_n-1):
                    continue
                else:
                    new_base_table[row][col] = new_base_table[row+1][col-1]*(row+1)/col
        #Set this new table as the new base. Build another table if n is still not high enough
        base_table = new_base_table
    #Query the final table for the desired output
    return str(base_table[x-1][y-1])
