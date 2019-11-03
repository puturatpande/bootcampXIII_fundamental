alas = 2
tinggi = 5
luas_segitiga = alas * tinggi / 2

print (luas_segitiga)

#segitiga 2
alas = 7
tinggi = 2
luas_segitiga = alas * tinggi / 2

print (luas_segitiga)

#sederhanakan dengan membuat fungsi
def hitung_luas_segitiga(alas, tinggi):
    return alas * tinggi / 2
segitiga1 = hitung_luas_segitiga(10,2)
print (segitiga1)

segitiga2 = hitung_luas_segitiga(5,2)
print (segitiga2)

#OOP/Class
#Encapsulation
#inheritance
#Polymorphism
# Encapsulation ==> membuat class
class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return self.alas*self.tinggi / 2

class Segitiga_samasisi(Segitiga):
    def is_Segitiga_samasisi(self):
        return True

class Segitiga_samakaki(Segitiga):
    def is_Segitiga_samakaki(self):
        return False



segitiga1 = Segitiga(10, 4)
print(segitiga1.alas)
print(segitiga1.hitung_luas())

sama_kaki = Segitiga_samakaki(10, 10)
print(sama_kaki.is_Segitiga_samakaki())

sama_sisi = Segitiga_samasisi(90, 20)
print(sama_sisi.is_Segitiga_samasisi())


#enheritance