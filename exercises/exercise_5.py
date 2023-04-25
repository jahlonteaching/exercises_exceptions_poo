import re


class PatternMatcher:

    def match(self, strings, pattern):
        """
        Devuelve una lista de cadenas que coinciden con el patrón.
        :param strings: lista de cadenas a buscar
        :param pattern: cadena de patrón, que puede contener los siguientes caracteres:
                        - '?' que representa un solo carácter
                        - '*' que representa cero o más caracteres
        :return: lista de cadenas que coinciden con el patrón
        """
        if not all(isinstance(s, str) for s in strings):
            raise TypeError("La lista de cadenas debe contener solo cadenas")
        if not isinstance(pattern, str):
            raise TypeError("El patrón debe ser una cadena")

        # Convertir el patrón en una expresión regular
        pattern = pattern.replace('?', '.').replace('*', '.*')

        # Buscar las cadenas que coinciden con el patrón
        matches = []
        for string in strings:
            if re.match(pattern, string):
                matches.append(string)

        return matches
