def permute (a, idx, b):

    b.append(a)

    hi = len(a)

    if(idx >= hi):

        print(a)

        

    else:

        for i in range(idx, hi):

            a[idx], a[i] = a[i], a[idx]

            permute (a, idx + 1, b)

            a[idx], a[i] = a[i], a[idx]

    return b

def main():

    a = ['A','B','C']

    a = permute (a, 0, [])

    print(a)

main()

    
