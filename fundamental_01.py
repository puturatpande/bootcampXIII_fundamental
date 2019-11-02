"""
esensi sintaksis python:
sequential
branching/percabangan
loop/perulangan
modularisasi dengan:
a.fungsi
b.class
c.package
Program yang dibuat adalah blog dengan Django
"""
judul ="Menguasai Python dalam 3 Jam "
author = 'Eko Wibowo'
tanggal ='2009-11-02'

jumlah_artikel = 100

if jumlah_artikel >= 100:
    print('jumlah artikel besar , akan dipaginasi')
elif jumlah_artikel > 20 and jumlah_artikel <= 60:
    print ('menengah')
else:
    print('srtikel cukup kecil, tidak perlu paginasi')

# tugas: tampilkan
#perulangan
for i in range (1,11):
    print (i)
#while
#cetak angka dari suatu variabel bebas s/d 1 menurun
angka = 15
while angka >= 1:
    print (angka)
    angka = angka-1

#dynamically typed language => Javascript
angka = 'lima belas'
print (angka)

# Tipe data list / array
jenis_kelamin = ['pria','wanita']
for jk in jenis_kelamin:
    print (jk)

# Tipe data bebas
angka = [1, 'loro', 3, 4.0, True]
for a in angka:
    print (a)

#Dictionary
kamus_cinta = {}
kamus_cinta ['love'] = 'tresna'
kamus_cinta ['sayang'] = 'kangen'
print (kamus_cinta['love'])

manusia = [
    {
        'nama' : 'putu pande',
        'alamat' : {
            'line 1' : 'jl ketumbar no 7',
            'Kelurahan' :'Bendungan',
            'Kecamatan' : 'Cilegon',
            'Kota' : 'Cilegon',
            'Provinsi' : 'Banten',
        }
    },
    {
        'nama' : 'putu pande',
        'alamat' : {
            'line 1' : 'jl ketumbar no 7',
            'Kelurahan' :'Bendungan',
            'Kecamatan' : 'Cilegon',
            'Kota' : 'Cilegon',
            'Provinsi' : 'Banten',
        }
    }
]

print (manusia)