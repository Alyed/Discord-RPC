class Jsonrw:
    import json

    def __init__(self, path_to_json_file: str):
        self.path = path_to_json_file

    def read(self):

        with open(self.path, "r") as file:
            return dict(Jsonrw.json.load(file))

    def write(self, data: dict, indent: int = 2):

        with open(self.path, "w") as file:
            Jsonrw.json.dump(data, file, indent=indent)
