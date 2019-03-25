class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

c0 = MhsTif("Salsa", 9, "Madiun", 240000)
c1 = MhsTif("Susi", 10, "Bojonegoro", 450000)
c2 = MhsTif("Lutfi", 11, "Karanganyar", 320000)
c3 = MhsTif("Kori", 12, "Karanganyar", 345000)
c4 = MhsTif("Rendra", 13, "Surakarta", 540000)
c5 = MhsTif("Fachrul", 14, "Indramayu", 350000)
c6 = MhsTif("Rima", 15, "Klaten", 245000)
c7 = MhsTif("Naufal", 16, "Bogor", 125000)
c8 = MhsTif("Fadel", 17, "Klaten", 245000)
c9 = MhsTif("Bayu", 18, "Sragen", 270000)
c10 = MhsTif("Haiqal", 19, "Pekalongan", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan)-1
    while low <= high:
        mid = (high+low)//2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
print(binSe(kumpulan, 5))
