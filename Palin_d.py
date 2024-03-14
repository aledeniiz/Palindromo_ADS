class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.count = 0
        self.file = None

    def open_file(self):
        self.file = open(self.filename, 'a')

    def log(self, message):
        if self.file is None:
            self.open_file()

        if self.count == 0:
            self.file.write("--Start log--\n")
        self.count += 1
        self.file.write(f"{message}\n")

    def close_file(self):
        if self.file:
            self.file.write(f"--End log: {self.count} log(s)--\n")
            self.file.close()
            self.file = None

class Test:
    def __init__(self):
        self.logger = Logger("log.txt")

    def llamada(self, message):
        self.logger.log(message)

    def __del__(self):
        self.logger.close_file()

# Ejemplo de uso
test = Test()
for i in range(1, 6):
    if i == 1:
        test.llamada("Primera llamada")
    else:
        test.llamada(f"{i}a llamada")