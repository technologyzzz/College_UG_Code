import pandas as pd
import os

# 1. Definisikan Data dalam bentuk Dictionary Python
data_saham = {
    'KodeSaham': ['BBCA', 'BBRI', 'TLKM'],
    'ModalInvestasi': [50000000, 30000000, 20000000], # Angka Murni (Int)
    'AvgGrowth': [0.12, 0.10, 0.05],       # Desimal (12%, 10%, 5%)
    'AvgDividend': [0.02, 0.05, 0.04]      # Desimal (2%, 5%, 4%)
}

# 2. Ubah menjadi DataFrame (Tabel Pandas)
df = pd.DataFrame(data_saham)

# 3. Tentukan lokasi simpan (Otomatis di sebelah script ini)
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'portfolio.xlsx')

print(f"🛠️ [GENERATOR] Sedang membuat file Excel di: {file_path}...")

# 4. Simpan ke Excel (Membutuhkan openpyxl)
try:
    df.to_excel(file_path, index=False, engine='openpyxl')
    print("✅ [SUKSES] File 'portfolio.xlsx' berhasil diciptakan!")
    print("   -> Sekarang jalankan script wealth_final.py mu.")
except Exception as e:
    print(f"❌ [ERROR] Gagal membuat file: {e}")
    print("   -> Pastikan kamu sudah install openpyxl (pip install openpyxl)")