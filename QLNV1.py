

class NV():
    def __init__(self, STT, Ten, Tuoi, GioiTinh, Phong ) -> None:
        self.STT = STT
        self.Ten = Ten
        self.Tuoi = Tuoi
        self.GioiTinh = GioiTinh
        self.Phong = Phong
    # def Show(self):
    #     return 'STT = {0}, Ten = {1}, Tuoi = {2}, GioiTinh = {3}, Phong = {4}'.format(self.STT,self.Ten,self.Tuoi,self.GioiTinh,self.Phong)
    # @classmethod
    # def AddNV(cls, STT, Ten, Tuoi, GioiTinh):
    #     return cls(STT, Ten, Tuoi, GioiTinh)
class QLNV():
    def __init__(self, NVs) -> None:
        self.NVs = NVs
    def Show(self):
        for i in self.NVs:
            print('STT = {0}, Ten = {1}, Tuoi = {2}, GioiTinh = {3}, Phong = {4}'.format(i.STT,i.Ten,i.Tuoi,i.GioiTinh,i.Phong))
    def AddNV(self, nv):
        self.NVs.append(nv)
        return self.NVs
nv1 = NV(1,'NVA',21,0,'KeToan1')
nv2 = NV(2,'NVB',21,0,'KeToan2')
nv3 = NV(3,'NVC',21,1,'KeToan3')
listnv = [NV]
ql1 = QLNV(listnv)
ql1.AddNV(nv1)
ql1.AddNV(nv2)
ql1.AddNV(nv3)
ql1.Show()

