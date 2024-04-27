original_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]


def bigger_than(num):
    return num > 6




def intersection(originallist, biggerthan):
    return [element for element in originallist if biggerthan(element)]


result = intersection(original_list, bigger_than)


print(result)
