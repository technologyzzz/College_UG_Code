"""
import math

def hitung_luas(jari_jari):
    # Rumus: π * r^2
    return math.pi * (jari_jari ** 2)

def hitung_keliling(jari_jari):
    # Rumus: 2 * π * r
    return 2 * math.pi * jari_jari

# --- Program Utama ---
r = float(input("Masukkan jari-jari lingkaran: "))

# 2. Panggil fungsi untuk perhitungan
luas = hitung_luas(r)
keliling = hitung_keliling(r)

# 3. Tampilkan hasil
# :.2f digunakan untuk membulatkan hasil menjadi 2 angka di belakang koma
print("\n--- Hasil ---")
print(f"Luas Lingkaran: {luas:.2f}")
print(f"Keliling Lingkaran: {keliling:.2f}")
"""



# --- 1. Definisi Fungsi-Fungsi Operasi ---

def tambah(a, b):
    """Menjumlahkan dua angka."""
    return a + b

def kurang(a, b):
    """Mengurangkan dua angka."""
    return a - b

def kali(a, b):
    """Mengalikan dua angka."""
    return a * b

def bagi(a, b):
    """Membagi dua angka. Mengembalikan pesan error jika b = 0."""
    if b == 0:
        # Menangani kasus pembagian dengan nol
        return "Error: Pembagian dengan nol tidak diizinkan."
    return a / b

def sisa_bagi(a, b):
    """Mencari sisa bagi (modulus). Mengembalikan pesan error jika b = 0."""
    if b == 0:
        # Menangani kasus modulus dengan nol
        return "Error: Operasi modulus dengan nol tidak diizinkan."
    return a % b

# --- 2. Fungsi untuk Menampilkan Menu ---

def tampilkan_menu():
    """Mencetak menu pilihan ke layar."""
    print("\n--- Menu Kalkulator Sederhana ---")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Hasil Sisa Bagi (%)")
    print("6. Keluar")

# --- 3. Fungsi Utama (Main Program) ---

def main():
    """Fungsi utama untuk menjalankan alur program kalkulator."""
    
    # Loop program agar terus berjalan sampai user memilih '6' (Keluar)
    while True:
        tampilkan_menu()
        
        # --- Ambil Pilihan Menu dari User ---
        pilihan = input("Masukkan pilihan Anda (1-6): ")
        
        # --- OPSI 6: Keluar ---
        if pilihan == '6':
            print("Terima kasih, program selesai.")
            break # Hentikan perulangan (while loop)
        
        # --- OPSI 1-5: Operasi Matematika ---
        if pilihan in ('1', '2', '3', '4', '5'):
            # --- Ambil Input Angka ---
            try:
                nilai1 = float(input("Masukkan nilai 1: "))
                nilai2 = float(input("Masukkan nilai 2: "))
            except ValueError:
                # Jika input bukan angka
                print("Error: Input tidak valid. Harap masukkan angka.")
                continue # Ulangi dari awal loop

            # --- Panggil Fungsi Sesuai Pilihan ---
            if pilihan == '1':
                hasil = tambah(nilai1, nilai2)
                print(f"Hasil: {nilai1} + {nilai2} = {hasil}")
            
            elif pilihan == '2':
                hasil = kurang(nilai1, nilai2)
                print(f"Hasil: {nilai1} - {nilai2} = {hasil}")
            
            elif pilihan == '3':
                hasil = kali(nilai1, nilai2)
                print(f"Hasil: {nilai1} * {nilai2} = {hasil}")
            
            elif pilihan == '4':
                hasil = bagi(nilai1, nilai2)
                # Cek apakah hasilnya adalah string (pesan error) atau angka
                if isinstance(hasil, str):
                    print(hasil) # Cetak pesan error-nya
                else:
                    print(f"Hasil: {nilai1} / {nilai2} = {hasil:.2f}")
            
            elif pilihan == '5':
                hasil = sisa_bagi(nilai1, nilai2)
                # Cek apakah hasilnya adalah string (pesan error) atau angka
                if isinstance(hasil, str):
                    print(hasil) # Cetak pesan error-nya
                else:
                    print(f"Hasil: {nilai1} % {nilai2} = {hasil}")

        else:
            # --- Jika Pilihan Tidak Valid (bukan 1-6) ---
            print("Pilihan tidak valid. Silakan masukkan angka dari 1 sampai 6.")

# --- Menjalankan Program ---
if __name__ == "__main__":
    main()