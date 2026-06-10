#Logical operators

# x=10
# y = 20
# print(x>0 and y<9)
#===============================================================================
# x = 0
# print(x and 10)
#===============================================================================
# print(not(0 or False))
#===============================================================================
# x = 1
# y = 1
# z = x + y
# print(id(x) , id(y))

#===============================================================================
# DICTIONARY
#===============================================================================

# person = {"name": "Reyona","age":28, "Designation":"Validation Engineer"}

# person["college"] = "AVB"
# person["place"]="Kochi"
# print(person)
# person["age"] = 21
# print(person["age"])
# print(person["Designation"])




#===============================================================================

class Solution(object):
    # def findingDef(self,diff,nums):
    #     if diff in nums:
    #         return nums.index(diff)
    #     return -1
    # def twoSum(self, nums, target):
    #     # self.nums = nums
    #     # self.target = target
    #     seen ={}
    #     diff = 0
    #     for i in range(len(nums)):
    #         diff = target - nums[i]
    #         diffIndex = self.findingDef(diff,nums)
    #         if diffIndex != -1 and diffIndex != i :
    #             return [i, diffIndex ]


    

    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            print("**********************************",seen)
            if diff in seen:
                print("seen[difference]",seen[diff], "and i is", i)
                return [seen[diff], i]
            print("num[i]",nums[i])
            seen[nums[i]] = i
            
            print("seen[nums[i]] = i" , seen[nums[i]])


nums = [2,11,7,15]
target = 9
obj = Solution()
result = obj.twoSum(nums,target)
print(result)


# num = [2,7,11]
# seen ={}

# seen[2] = 0
# seen[11] = 44

# print(seen)










