from results import lottoResult

"""lotto entry objects, inherit from lottResult
using the same static method saved within"""
class lottoEntry(lottoResult):
    def __init__(self, f):
        line = next(lottoResult.fileRead(f))
        items = line.split(";")
        balls = items[1].split(":")
        self.ID = items[0]
        self.__balls = balls
        self.__sub1 = items[2]
        if items[3] != "":
            self.__sub2 = items[3]
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