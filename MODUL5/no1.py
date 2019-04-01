class mhs(object) :
    """Class mahasiswa dengan berbagai metode"""
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__ (self) :
        s = self.nama + ', NIM' + str(self.NIM)\
            +'.Tinggal di ' + self.kotaTinggal \
            +'. Uang saku Rp' + str(self.uangSaku)\
            +' tiap bulannya.'
        return s
    def ambilNama(self) :
        return self.nama
    def ambilNIM(self) :
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku

a0 = mhs("Fadel", 9, "Madiun", 240000)
a1 = mhs("Rima", 10, "Klaten", 230000)
a2 = mhs("Fachrul", 14, "Indramayu", 250000)
a3 = mhs("Kori", 18, "Karanganyar", 2350000)
a4 = mhs("Rendra", 25, "Surkarta", 230000)
a5 = mhs("Susi", 28, "Bojonegoro", 250000)
a6 = mhs("Naufal", 13, "Bogor", 245000)
a7 = mhs("Bayu", 20, "Sragen", 245000)
a8 = mhs("Lutfi", 23, "Karanganyar", 245000)
a9 = mhs("Salsa", 30, "Madiun", 270000)
a10 = mhs("Haiqal", 17, "Pekalongan", 265000)

daftar = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]

kumpulan = []
for a in daftar :
    kumpulan.append(a.ambilNIM())
def insertionSort(kumpulan):
    n = len(kumpulan)    
    for i in range (1, n):
        nilai = kumpulan[i]
        pos = i
        while pos > 0 and nilai < kumpulan[pos - 1] :
            kumpulan[pos] = kumpulan[pos -1]
            pos = pos -1
            kumpulan[pos] = nilai

insertionSort(kumpulan)
print (kumpulan)
