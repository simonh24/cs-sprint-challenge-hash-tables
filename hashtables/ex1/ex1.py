def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i in range(len(weights)):
        if weights[i] not in cache:
            cache[weights[i]] = i
        num = limit - weights[i]
        if num in cache and cache[num] is not i:
            second_ind = cache[num]
            if i > second_ind:
                return [i, second_ind]
            else:
                return [cache[num], i]
    return None
