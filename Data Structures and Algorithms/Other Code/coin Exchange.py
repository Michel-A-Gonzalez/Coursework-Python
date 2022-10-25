def coin_exchange (n, den_lst):

    den_lst.sort()

    coins = []

    for i in range (len(den_lst) - 1 ,-1, -1):

        number = n // den_lst[i]

        coins.append(number)

        n  = n % den_lst [i]

    return coins

def coin_memo (coins, n):

    # keeps track of the minimum number of
    # coins needed

    table = [0 for i in range (n + 1)]

    # base case 0 coins

    table[0] = 0

    for i in range (1, n + 1):

        # checks every coin value

        for j in range (len (coins)):

            if (coins[j] <= i):

                # gets the previous minimum value

                sub = table[i - coins[j]]

                if (table[i] == 0):

                    table[i] = sub + 1

    return table

                

            

def main ():

    lst = [1,7,13,23]

    n = 37

    coins = coin_exchange (n, lst)

    coins2 = coin_memo (lst, n)

    coins.reverse()

    print (coins)

    print (coins2)

    total = sum(coins)

    print(total)

main()

        

    
