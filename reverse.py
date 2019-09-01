def reverser(data):
    "A python method that reverses a single list passed to it as an argument"
    if isinstance(data, list):
        # a new list to hold the reversed list
        new_list = []
        # determie the length of the list passed
        objects = len(data)
        # determie the index of te first list item on the -ve scale
        first_index = int(objects - (2 * objects))
        # a for loop to populate new list with list items in reverse
        for i in range(-1, first_index-1, -1):
            new_list.append(data[i])
        return new_list
    # error message for invalid arguments
    return "This method only accepts a single list!"
