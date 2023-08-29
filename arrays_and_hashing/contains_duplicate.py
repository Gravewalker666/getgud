class Solution:
  # time O(n), space O(n)
  def containDuplicate(self, nums: List[int]) -> bool:
    setOfNums = set()
    for n in nums:
      if n in setOfNums:
        return True
      setOfNums.add(n)
    return False
