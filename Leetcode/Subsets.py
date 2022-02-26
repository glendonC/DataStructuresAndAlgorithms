class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = [[]]
        for n in nums:
            new_subs = []
            for sub in answer:
                new_subs.append(sub+[n])
            answer.extend(new_subs)
        return answer