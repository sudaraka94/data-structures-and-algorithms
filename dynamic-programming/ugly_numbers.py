def ugly(index):
    #This functions generates ugly numbers
    #https://www.geeksforgeeks.org/ugly-numbers

    ugly_array = [0] * index
    ugly_array[0] = 1

    index_2 = 0
    index_3 = 0
    index_5 = 0

    for i in range(1,index):
        print(i)
        print(index_2)
        val_2 = 2 * ugly_array[index_2]
        val_3 = 3 * ugly_array[index_3]
        val_5 = 5 * ugly_array[index_5]

        min_val = min(val_2, val_3, val_5)

        ugly_array[i] = min_val

        if min_val == val_2:
            index_2 += 1
        if min_val == val_3:
            index_3 += 1
        if min_val == val_5:
            index_5 += 1

    return ugly_array

print (ugly(10))
