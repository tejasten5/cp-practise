
# def  two_sum(arr,target):
#     li = []
#     for i in range(len(arr)):
#         diff  = target - arr[i]

#         if diff in arr:
#             print((i,arr.index(diff)))
#             break


def two_sum(arr,target):
    context = {}
    for idx,val in enumerate(arr):
        diff = target - val
        if diff in context:    
            return (context[diff],idx)        
        context[val] = idx


print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))

