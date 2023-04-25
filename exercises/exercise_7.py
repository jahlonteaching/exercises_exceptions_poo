class FileSearcher:
    def search(self, file_names, search_string):
        result = []
        for file_name in file_names:
            try:
                with open(file_name, 'r') as f:
                    for line in f:
                        if search_string in line:
                            result.append(line)
            except FileNotFoundError:
                print(f"{file_name} no encontrado")
            except IOError:
                print(f"No se puede leer {file_name}")
        return result
