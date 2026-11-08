#File untuk di kolaborasi

#Kode Iqbal Fadhil Tresnadarma

ObjekPiramid = (str(input("Masukkan string sebagai objek piramid : ")))

def Piramida (Baris):
    SpasiJarak = Baris
    Bintang = 1
    for SetiapBaris in range (Baris):
        print(" " * SpasiJarak, ObjekPiramid * Bintang)
        SpasiJarak -= 1
        Bintang +- 1


Piramida(int(input("Masukkan Tinggi Piramida Bintang : ")))


# Kode Muhammad Dimas Nugraha

# Kode Raditya Farras Sudrajat

alas = float(input("Masukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

# Rumus luas segitiga
luas = 0.5 * alas * tinggi

print(f"Luas segitiga adalah: {luas}")

# Kode Rayndra Sulaiman Fattaahillah

rayn = """
||||||   ||||||   ||  ||   ||   ||
||  ||   ||  ||   ||  ||   |||  ||
||||||   ||||||    ||||    || ||||
|| ||    ||  ||     ||     ||  |||
||  ||   ||  ||     ||     ||   ||
"""

print(rayn)
print("halo semua")
