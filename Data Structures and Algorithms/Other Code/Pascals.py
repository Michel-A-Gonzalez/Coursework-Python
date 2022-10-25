def pascal (n):

    # get all previous coefficients
    # for faster computation

    memo = [[0 for j in range (n) ]for i in range (n)]

    for i in range (n):

        # coefficients at the end are always one

        row  = [0 for i in range (n + 1)]

        row[0], row[-1] = 1, 1

        for j in range (1, len (row) - 1):

            print (row)

            row[j] = memo[i - 1][j - 1] + memo[i - 1][j]

        memo[i].append (row)

    return memo

                

            

            

            

            

            

        
            

    
