def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create a hash to hold the index and value
    weights_hash = {}
    # create a hash to hold the index value in case of duplicates
    dups = {}

    # loop through length of weights
    for i in range(length):
        # add weight as key and index as value
        weights_hash[weights[i]] = i
        # calculate target value based on limit
        target = limit - weights[i]


        # check to see if target is in weights hash and dups hash
        # adding the value to the dups hash last ensures that the
        # dups hash will not have the target overwritten 
        if target in weights_hash and target in dups: 
            return (i, dups[target])
        # check if target is in weights hash and target != weights value
        # if it does that means it is a duplicate and would have been taken
        # care of with first case
        elif target in weights_hash and target != weights[i]:
            return (i, weights_hash[target])
        else:
            # add value to dups 
            dups[weights[i]] = i

    return None
