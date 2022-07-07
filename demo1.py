
class SV:
    khoa = 'CNTT'
    #regular method
    def __init__(self, MSSV , Name) -> None:
        self.MSSV=MSSV
        self.Name=Name
    def Show(self):
        return 'MSSV = {0}, Name = {1}'.format(self.MSSV,self.Name)
    def G_Name_SV(self):
        return self.Name
    def S_Name_SV(self,Name):
        self.Name = Name
    @classmethod
    def fromstring(cls, s):
        s1 = s.split('-')
        s2 = [i.strip() for i in s1]
        MSSV, Name = s2
        return cls(MSSV,Name)
    #static method
    def View(s):
        return s
    #magic method
    def __str__(self) -> str:
        return 'MSSV = {0}, Name = {1}'.format(self.MSSV,self.Name)
class SVCNTT(SV):
    def __init__(self, MSSV, Name, LT) -> None:
        super().__init__(MSSV, Name)
        self.LT = LT
    def Show(self):
        return 'MSSV = {0}, Name = {1}, LT = {2}'.format(self.MSSV,self.Name,self.LT) 

sv1=SV(1,'NVA')
sv2=SV(2,'NVB')
print('{0} {1}'.format(sv1.MSSV,sv1.Name))
SV.khoa = 'Hoa'
print(sv2.khoa)
sv1.khoa='CNTT'
print(sv1.khoa)
print(sv2.khoa)
s = '4 - NVA'
s4 = SV.fromstring(s)
print(s4.__dict__)
print(SV.View('Static method'))
print(s4.__str__())

s5 = SVCNTT(1, 'NVA' , 'OK')
print(s5.__dict__)
print(s5.Show())



