def longest_sub (lst):

    # the longest subsequence for a single number
    # is one

    max = 1

    # goes through the eniter 

    for i in range (1, len(lst)):

        count = 1

        for j in range (0, i - 1):

            if (lst[j] < lst[i]):

                count += 1

            else:

                continue

        if (count > max):

            max = count
            
    return max

            
def main ():

    lst = [3,5,1,6,2,14,51,7,12,13]

    print (longest_sub (lst))

main()
