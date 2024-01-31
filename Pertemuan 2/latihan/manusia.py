class Manusia:
  def __init__(self, name, year, gender):
    self.nama = name
    self.tahun = year
    self.jenis = gender


  def getNama(self):
    return self.nama

  def getTahun(self):
    return self.tahun

  def getJenis(self):
    return self.jenis

  def checkAge(self, curent_year):
    usia = curent_year - self.tahun
    if usia > 60:
      return print("sangat tua")
    elif usia < 40:
      return print("Sangat Muda")
    else:
      return print("Tengah Usia")



ahmad = Manusia("Akhmad",2000,"L")
print(ahmad.getNama())
print(ahmad.getTahun())
print(ahmad.getJenis())
print(ahmad.checkAge(2024))
