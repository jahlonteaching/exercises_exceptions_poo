class SumFinder:
    def find_pairs(self, nums, target):
        if len(nums) < 2:
            raise ValueError("La lista debe contener al menos dos elementos")

        # Diccionario para almacenar los números y sus índices
        num_dict = {}

        # Lista para almacenar las parejas que suman el valor objetivo
        pairs = []

        for i, num in enumerate(nums):
            # Comprobamos si hay un número complementario en el diccionario
            complement = target - num
            if complement in num_dict:
                pairs.append((complement, num))

            # Añadimos el número y su índice al diccionario
            num_dict[num] = i

        return pairs
