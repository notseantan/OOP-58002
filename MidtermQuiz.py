class TempConversion:
    def __init__(self, temp):
        self.temp = temp
        self.C = C
        self.F = F
        self.K = K

    def FtC(self):
      return (F-32) * 5/9

    def KtC(self):
      return K - 273.15

    def CtF(self):
      return (C * 9/5)+32

    def KtF(self):
      return (1.8*K)-459.67

    def CtK(self):
      return C+273.15

    def FtK(self):
      return (F+459.67) / 1.8

    def Display(self):
      print("Fahrenheit", self.F())
      print("Celsius", self.C())
      print("Kelvin", self.K())


temp = float(input("Input the temperature to be converted:"))
t = TempConversion
t.Display()

