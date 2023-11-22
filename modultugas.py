import modulebangundatar

print("Pilih bangun ruang yang akan dipilih")
print("1. Lingkaran")
print("2. Segitiga")

opsi = int(input("\nKetik Pilih: "))

if opsi == 1:
    print("Hitung Lingkaran ")
    r = int(input("Masukkan Nilai Jari-jari: "))
    modulebangundatar.lingkaran(r)
elif opsi == 2:
    print("Hitung Segitiga ")
    a = int(input("Masukkan Nilai Alas: "))
    t = int(input("Masukkan Nilai Tinggi: "))
    modulebangundatar.segitiga(a, t)