class InOutFile():
    @staticmethod
    def writeFile(filename, text):
        file = open(filename, "w+")
        file.write(text)
        file.close()

    @staticmethod
    def readFile(filename):
        file = open(filename, "r+")
        text1 = file.read()
        file.close()
        return text1
