"""
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

class TwoSumProblem:
    def calculation(self,nums,target):
        # list compression
        # print([(i,j) for i in range(len(nums)) for j in range(i,len(nums)) if nums[i] + nums[j] == target ])

        #Nestes loop
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)) :
        #         if nums[i] + nums[j] == target:
        #             print(i,j)
        index = {}
        for i, value in enumerate(nums):
            import pdb;pdb.set_trace()
            remaining = target - nums[i]
            if remaining in index:
                return[i, index[remaining]]        
            index[value] = i        

nums = [2,7,11,15]
target = 9

print(TwoSumProblem().calculation(nums, target))