def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for nums in a:
        if abs(nums) not in cache:
            cache[abs(nums)] = 1
        else:
            result.append(abs(nums))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
