print("=== SISTEM MANAJEMEN NILAI SISWA ===")

nama = input("masukkan nama mahasiswa: ")
npm = int(input("masukkan npm mahasiswa: "))
jumlah_matkul = int(input("Jumlah mata kuliah: "))

nilai_matkul = []

for i in range(jumlah_matkul):
    nilai = float(input(f"Masukkan nilai mata kuliah ke-{i+1}: ")) 
    nilai_matkul.append(nilai)

total = sum(nilai_matkul)
rata = total / jumlah_matkul

if rata >= 85 and rata <= 100: 
    status = "Lulus - Predikat A" 
elif rata >= 75 and rata < 85: 
    status = "Lulus - Predikat B" 
elif rata >= 65 and rata < 75: 
    status = "Lulus - Predikat C" 
elif rata >= 0 and rata < 65:
    status = "Tidak Lulus"
else:
    status = "Nilai di luar rentang 0-100"
    
print("\n=== HASIL NILAI ===")
print("Nama         :", nama)
print("NPM          :", npm)
print("Daftar Nilai :", nilai_matkul)
print("Rata-rata    :", round(rata, 2))
print("Status       :", status)


print("\nProgram selesai.")

