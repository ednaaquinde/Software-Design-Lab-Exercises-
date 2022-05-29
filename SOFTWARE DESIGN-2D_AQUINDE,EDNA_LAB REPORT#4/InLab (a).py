def minmax(lst):
    if(len(lst) == 1):
        return (lst[0], lst[0])
    else:
        (minVal, maxVal) = minmax(lst[1:])
        if(minVal > lst[0]):
            minVal = lst[0]
        if(maxVal < lst[0]):
            maxVal = lst[0]
        return minVal, maxVal


# Testing
lst = [2,4,1,5,3]
minVal, maxVal = minmax(lst)
print(minVal)
print(maxVal)

