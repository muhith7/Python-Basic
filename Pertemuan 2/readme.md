1. Komentar (Comment):

Komentar digunakan untuk memberikan penjelasan pada kode.
Tanda # digunakan untuk komentar satu baris, dan ''' atau """ digunakan untuk komentar beberapa baris.
python
Copy code
# Ini adalah komentar satu baris
'''
Ini adalah komentar
beberapa baris
'''
2. Variabel (Variable):

Variabel digunakan untuk menyimpan data atau nilai.
Nama variabel dapat diawali dengan huruf atau garis bawah dan dapat mengandung huruf, angka, dan garis bawah.
python
Copy code
nama = "John"
umur = 25
3. Number:

Jenis-jenis number termasuk int (integer) dan float (floating-point).
python
Copy code
angka_bulat = 10
angka_desimal = 3.14
4. Casting:

Mengubah tipe data dari satu tipe ke tipe lain.
python
Copy code
angka = int("5")
desimal = float(10)
5. String:

String digunakan untuk menyimpan teks.
Dapat diapit oleh tanda kutip tunggal (') atau ganda (").
python
Copy code
teks = "Halo, ini adalah string."
6. Boolean:

Boolean memiliki dua nilai: True atau False.
Digunakan dalam ekspresi logika.
python
Copy code
benar = True
salah = False
7. Operator:

Operator digunakan untuk melakukan operasi pada variabel dan nilai.
python
Copy code
x = 5
y = 2

penjumlahan = x + y
pengurangan = x - y
8. List:

List adalah struktur data yang dapat menyimpan banyak nilai.
Dapat diubah (mutable) dan berurutan.
python
Copy code
my_list = [1, 2, 3, "empat"]
9. Tuple:

Tuple adalah struktur data yang mirip dengan list tetapi bersifat tidak dapat diubah (immutable).
python
Copy code
my_tuple = (1, 2, 3, "empat")
10. Sets:
- Sets adalah struktur data yang tidak memiliki indeks dan tidak memperbolehkan duplikasi.

python
Copy code
my_set = {1, 2, 3, 3}
11. If-Else:
- Digunakan untuk pengambilan keputusan berdasarkan kondisi.

python
Copy code
x = 10
if x > 5:
    print("Lebih besar dari 5")
else:
    print("Kurang dari atau sama dengan 5")
12. While Loop:
- Looping selama kondisi tertentu benar.

python
Copy code
angka = 1
while angka <= 5:
    print(angka)
    angka += 1
13. For Loop:
- Digunakan untuk mengulangi elemen dalam urutan tertentu.

python
Copy code
for angka in range(1, 6):
    print(angka)
14. Function:
- Blok kode yang dapat dipanggil dengan nama dan menerima argumen.

python
Copy code
def tambah(x, y):
    return x + y
15. Class/Object/Inheritance:
- Class adalah blueprint untuk objek.
- Objek adalah instance dari class.
- Inheritance memungkinkan kelas untuk mewarisi properti dan metode dari kelas lain.

python
Copy code
class Manusia:
    def __init__(self, name, year, gender):
        self.nama = name
        self.tahun = year
        self.jenis = gender

class Pegawai(Manusia):
    def __init__(self, name, year, gender, nip):
        super().__init__(name, year, gender)
        self.nip = nip
Rangkuman ini memberikan gambaran umum tentang konsep-konsep dasar dalam bahasa pemrograman Python. Anda dapat mempelajari lebih lanjut tentang masing-masing konsep melalui dokumentasi resmi Python atau sumber belajar lainnya.