from manusia import Manusia
from pegawai import Pegawai

ahmad = Manusia('ahmad','L',1999,berat=10,tinggi=10)

print('Nama = ', ahmad.name)
print('JK= ', ahmad.gender)
print('Tahun = ', ahmad.year)
print('BB = ', ahmad.berat)
print('TB', ahmad.tinggi)


budi = Pegawai('Budi','L',2000,'4323424')
print(budi.getName())
print(budi.nip)