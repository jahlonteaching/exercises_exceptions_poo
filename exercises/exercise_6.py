class Statistics:
    def median(self, nums):
        if len(nums) == 0:
            raise ValueError("Lista vacía")
        try:
            nums = sorted(nums)
            if len(nums) % 2 == 0:
                return (nums[len(nums)//2 - 1] + nums[len(nums)//2])/2
            else:
                return nums[len(nums)//2]
        except TypeError:
            raise TypeError("La lista contiene valores no numéricos")

    def standard_deviation(self, nums):
        if len(nums) == 0:
            raise ValueError("Lista vacía")
        try:
            mean = sum(nums)/len(nums)
            variance = sum((x - mean)**2 for x in nums)/len(nums)
            return variance**0.5
        except TypeError:
            raise TypeError("La lista contiene valores no numéricos")
