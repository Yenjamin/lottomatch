"""lotto result objects, also the parent class for lottoEntry"""
class lottoResult:
    def __init__(self, f):
        line = next(lottoResult.fileRead(f))
        items = line.split(";")
        balls = items[0].split(":")
        self.__balls = balls
        self.__sub1 = items[1]
        if items[2] != "":
            self.__sub2 = items[2]
        else:
            self.__sub2 = -1

    @property
    def ballset(self):
        return self.__balls

    @property
    def additionals(self):
        adnum = []
        adnum.append(self.__sub1)
        if self.__sub2 != -1:
            adnum.append(self.__sub2)
        return adnum

    @staticmethod
    def fileRead(file):
        """read file into a list of strings and return the processed result"""
        line = file.readline()
        while line:
            if line == "\n" or "mainballs" in line:
                line = file.readline()
            else:
                processed = line.strip("\n")
                yield(processed)