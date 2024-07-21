class Buku:
    def __init__(self, judul, penulis, konten, penerbit=None, tahun_terbit=None, iktisar=None):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.konten = konten
        self.iktisar = iktisar

    def read(self, halaman):
        if halaman <= len(self.konten):
            return self.konten[:halaman]
        else:
            return "Halaman melebihi konten buku"

    def __str__(self):
        return f"{self.judul} by {self.penulis}"

#penggunaan
buku = Buku("Mathematics for Machine Learning", "Marc Peter Deisenroth", ["Bab 1", "Bab 2", "Bab 3"])
print(buku)
print(buku.read(2))
