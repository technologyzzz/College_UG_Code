# Ttile
print("Program Latihan")

# Input from user
name = input("Masukan Nama : ")
npm = input("Masukan NPM : ")
# Input integer
uts_score = int(input("Masukan Nilai UTS : "))

# If-else logic for status
if uts_score > 60:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

# Final output format
# F-string to combine text and variable
print(f"Nama Anda : {name} - NPM Anda : {npm} - Anda {status}")


"""
def get_valid_nama() -> str:
    
# Terus meminta input nama sampai valid.
# Valid: Tidak kosong dan hanya berisi huruf (termasuk spasi).
    
    while True:
        nama = input("Masukan Nama : ").strip()
        # Cek jika nama tidak kosong DAN (setelah spasi dihapus) semuanya adalah huruf
        if nama and nama.replace(" ", "").isalpha():
            return nama
        else:
            print("Error: Nama tidak boleh kosong dan hanya boleh berisi huruf/spasi. Coba lagi.")

def get_valid_npm() -> str:
    
# Terus meminta input NPM sampai valid.
# Valid: Tepat 8 karakter dan semuanya adalah angka.
    
    while True:
        npm = input("Masukan NPM : ").strip()
        # Cek apakah semuanya angka DAN panjangnya tepat 8
        if npm.isdigit() and len(npm) == 8:
            return npm
        else:
            print("Error: NPM harus terdiri dari 8 angka. Coba lagi.")

def get_valid_nilai() -> int:
    
# Terus meminta input nilai sampai valid.
# Valid: Berupa angka integer antara 0 dan 100 (inklusif).
    
    while True:
        nilai_str = input("Masukan Nilai UTS : ").strip()
        try:
            # Coba ubah input menjadi angka (integer)
            nilai_uts = int(nilai_str)
            # Cek apakah angka tersebut dalam rentang 0-100
            if 0 <= nilai_uts <= 100:
                return nilai_uts
            else:
                print("Error: Nilai harus di antara 0 dan 100. Coba lagi.")
        except ValueError:
            # Jika 'int()' gagal (misal: input "sembilanpuluh" atau "abc")
            print("Error: Masukan harus berupa angka yang valid. Coba lagi.")

# --- Program Utama ---
print("Program Latihan")

# Panggil fungsi untuk mendapatkan input yang sudah terjamin valid
nama = get_valid_nama()
npm = get_valid_npm()
nilai_uts = get_valid_nilai()

# Menentukan status. Ini adalah cara efisien (ternary operator)
status = "LULUS" if nilai_uts > 60 else "TIDAK LULUS"

# Menampilkan output akhir
print("-" * 20) # Garis pemisah
print(f"Nama Anda : {nama} NPM Anda : {npm} Anda {status}")
"""
