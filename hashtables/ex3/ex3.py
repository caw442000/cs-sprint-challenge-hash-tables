def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    hold_count = {}
    curr_arr = 0

    
    #while in range of lists
    while curr_arr < len(arrays):
        # this will be used to make sure no dups are added to the count
        dup_check = set()
        #for number in current list
        for n in arrays[curr_arr]:
            #if that number is in the hashtable--
            if n in hold_count:
                # check to make sure we are not adding duplicates to the count from the same array
                if n not in dup_check: 
                    dup_check.add(n)
                    hold_count[n] += 1
            else:
                hold_count[n] = 1
        curr_arr += 1
    # list comp adds k (key) from hold_count if value is the the count of the arrays  
    results = [k for k, v in hold_count.items() if v == len(arrays)]
    return results




if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
