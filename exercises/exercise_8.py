class ProductFinder:
    def largest_product(self, nums):
        if len(nums) < 3:
            raise ValueError("La lista debe contener al menos tres elementos")

        # Ordenamos la lista para obtener los tres números más grandes
        nums.sort(reverse=True)

        # Posibilidades: producto de los tres números más grandes, producto del número más grande y los dos más pequeños
        return max(nums[0] * nums[1] * nums[2], nums[0] * nums[-1] * nums[-2])
