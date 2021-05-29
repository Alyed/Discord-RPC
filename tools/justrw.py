class Justrw:
    def __init__(self, filename: str):
        self.file = filename

    def write(self, data: str):
        with open(self.file, "w") as f:
            f.write(data)

    def read(self):
        with open(self.file, "r") as f:
            return f.read()

    def append(self, data: str):
        with open(self.file, "a") as f:
            f.write(data)