from manusia import Manusia
class Pegawai(Manusia):
  def __init__(self, name, year, gender, nip):
    super().__init__(name, year, gender)
    self.nip = nip

  def getNip(self):
      return self.nip


budi = Pegawai("Budi", 2000, "L", 22090095)
print(budi.getNip())
print(budi.checkAge(2024))