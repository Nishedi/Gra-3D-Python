class FileLoader:
    def __init__(self, filename):
        self.filename = filename

    def load(self, filename):
        with open(filename) as f:
            return f.read()
        
    def save(self, filename, value):
        with open(filename, 'w') as f:
            f.write(value)