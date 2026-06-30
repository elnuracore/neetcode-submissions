class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 1
        res = []
        count_final = 1
        count_zero = 0
        for i in nums:
            if i == 0:
                count_zero +=1
        if count_zero >= 2:
            for i in nums:
                res.append(0*i)
        elif count_zero == 1:
            for i in nums:
                if i != 0:
                    count *= i
            for i in nums:
                if i != 0:
                    res.append(0)
                else:
                    res.append(count)
        else:
            for i in nums:
                count *= i
            for i in nums:
                res.append(count//i)
        return res




