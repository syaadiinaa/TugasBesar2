def post_buku(buku):
    conn = psycopg2.connect("dbname=perpustakaan user=postgres password=secret")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, iktisar) VALUES (%s, %s, %s, %s, %s, %s)",
        (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, buku.konten, buku.iktisar)
    )
    conn.commit()
    cur.close()
    conn.close()

#penggunaan
buku_baru = Buku("New Book", "New Author", ["Chapter 1", "Chapter 2"])
post_buku(buku_baru)
