def unique_elements(list1, list2):
    result = []
    
    for item in list1:
        if item not in list2:
            result.append(item)
    
    for item in list2:
        if item not in list1:
            result.append(item)
    
    return result

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = unique_elements(a, b)
print(result)
