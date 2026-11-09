#File untuk di kolaborasi

print(""" 
KODE KELOMPOK 6
1. Kode buatan Iqbal Fadhil Tresnadarma
2. Kode buatan Muhammad Dimas Nugraha
3. Kode buatan Raditya Farras Sudrajat
4. Kode buatan Rayndra Sulaiman Fattaahillah
5. Kode buatan Hasbi khoirul fikri saputra

""")
MenuInput = (str(input("Masukkan kode yang ingin anda jalankan : ")))

if MenuInput == 1 :
#Kode Iqbal Fadhil Tresnadarma

    ObjekPiramid = (str(input("Masukkan string sebagai objek piramid : ")))

    def Piramida (Baris):
        SpasiJarak = Baris
        Bintang = 1
        for SetiapBaris in range (Baris):
            print(" " * SpasiJarak, ObjekPiramid * Bintang)
            SpasiJarak -= 1
            Bintang += 1


    Piramida(int(input("Masukkan Tinggi Piramida Bintang : ")))

elif MenuInput == 2 :
    # Kode Muhammad Dimas Nugraha
    # Mengambil input nilai dari user
    nilai = float(input("Masukkan nilai angka: "))

    # Proses pengecekan kondisi nilai
    if nilai >= 90:
        nilai_huruf = "A"
    elif nilai >= 80:
        nilai_huruf = "B"
    elif nilai >= 70:
        nilai_huruf = "C"
    else:
        nilai_huruf = "D"

    # Menampilkan hasil
    print(f"Nilai Huruf: {nilai_huruf}")

elif MenuInput == 3:
# Kode Raditya Farras Sudrajat

    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))

    # Rumus luas segitiga
    luas = 0.5 * alas * tinggi

    print(f"Luas segitiga adalah: {luas}")

elif MenuInput == 4:
# Kode Rayndra Sulaiman Fattaahillah
        
    rayn = ("""
    ||||||   ||||||   ||  ||   ||   ||
    ||  ||   ||  ||   ||  ||   |||  ||
    ||||||   ||||||    ||||    || ||||
    || ||    ||  ||     ||     ||  |||
    ||  ||   ||  ||     ||     ||   ||
    """)

    print(rayn)
    print("halo semua")

elif MenuInput == 5:
    # Kode Hasby
        print()

else:
    print("Tidak ada opsi itu")
