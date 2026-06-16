class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # Hash map solution
       # we know that our solution is the item
       # target - cur index = another remaining index
       # if this is true, then we have found our solution

      prevMap = {} # val : index

      for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
      return

