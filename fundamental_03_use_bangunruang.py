from bangun_ruang.segitiga_base import Segitiga
from bangun_ruang.segitiga_samakaki import Segitiga_samakaki
from bangun_ruang.segitiga_samasisi import Segitiga_samasisi

segitiga1 = Segitiga(10, 4)
print(segitiga1.alas)
print(segitiga1.hitung_luas())

sama_kaki = Segitiga_samakaki(10, 10)
print(sama_kaki.is_Segitiga_samakaki())

sama_sisi = Segitiga_samasisi(90, 20)
print(sama_sisi.is_Segitiga_samasisi())
