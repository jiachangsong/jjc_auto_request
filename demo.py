class Bicycle(object):
    def __init__(self):
        pass
    @classmethod
    def run(self, km):
        print(type(km))
        if (type(km) == int):
            print(f"骑行公里数{km}")
        else:
            print("请输出数字")


class EBicycle(Bicycle):
    valume = 100;

    def __init__(self,valume):
        self.valume = valume


    @classmethod
    def fill_charge(self,vol):
        self.valume = vol


    def run(self,distence):
        print("111")
        ev = int(distence/10)
        print(ev)
        if(self.valume<=ev):
            print("333")
            self.valume = 0
            Bicycle().run(distence-10*ev)
            print("444")
        else:
            print("555")
            self.valume = self.valume - ev







eb = EBicycle(10)
print(eb.valume)
eb.run(105)