import psycopg2

def get_buku(buku_id):
    conn = psycopg2.connect("dbname=perpustakaan user=postgres password=secret")
    cur = conn.cursor()
    cur.execute("SELECT * FROM buku WHERE id = %s", (buku_id,))
    buku_data = cur.fetchone()
    cur.close()
    conn.close()
    
    if buku_data:
        return Buku(buku_data[1], buku_data[2], buku_data[5], buku_data[3], buku_data[4], buku_data[6])
    else:
        return None

#penggunaan
buku = get_buku(1)
print(buku)
