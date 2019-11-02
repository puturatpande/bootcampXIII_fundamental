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
Class
segitiga1 = Segitiga(10, 4)
print(segitiga1.alas)
print(segitiga1.hitung_luas())

#enheritance