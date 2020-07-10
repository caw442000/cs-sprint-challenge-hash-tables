def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    numbers = set()

    result = []

    # add all numbers to a set
    for num in a:
        numbers.add(num)
        # if the inverse of the number is in the set
        # add the positive one to the negatives array
        # exclude zero
        if num != 0 and -num in numbers:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
