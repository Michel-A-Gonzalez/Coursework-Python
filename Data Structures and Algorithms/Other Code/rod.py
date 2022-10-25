def rod_cut (p, n):

    # p is the prices

    # n is the length of the given rod
    # that need to be optimized

    # r is the list of optimal pricing
    # s is the list that keeps track
    # of the cuts

    r = []

    s = []

    for i in range (n + 1):

        r.append(0)

        s.append(0)

    for j in range (1, n + 1):

        max_price = -1

        for k in range (1, j + 1):

            new_price = 0

            if (k < len(p)):

                new_price = p[k] + r[j - k]

            else:

                new_price = r[j - k]

            if (new_price > max_price):

                max_price = new_price

                s[j] = k

        r[j] = max_price

    return r

        

def main ():

    p = [0, 1, 5, 8, 9, 10, 17, 17, 20]

    n = 22

    result = rod_cut (p, n)

    print (result)

main ()
    
