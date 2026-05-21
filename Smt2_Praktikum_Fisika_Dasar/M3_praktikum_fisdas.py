import math

# =====================================================================
# BAGIAN INPUT DATA (Telah disesuaikan dengan Lembar Pengamatan M-3)
# =====================================================================

# Dimensi Benda (Trapesium Berlubang) - Satuan: cm & gram
a = 17.3
b = 25.0
c = 20.0
r = 3.0
m = 306.9

# Jarak titik ayun ke pusat massa (cm)
l_A = 14.0
l_B = 12.5
l_C = 16.5
l_D = 10.5

# Jarak pusat massa masing-masing bangun ke pusat massa total (cm)
l1 = 3.4
l2 = 9.0
l3 = 3.5

# Waktu Ayunan (detik)
t_A = 9.36
t_B = 9.31
t_C = 10.27
t_D = 9.80

n_ayunan = 10.0  # Asumsi waktu di atas adalah untuk 10 getaran
g = 980.0        # Percepatan gravitasi (cm/s^2)
pi = 3.14        # Konstanta Pi

# =====================================================================
# CORE ENGINE - STRICT CHAINED ROUNDING (3 DECIMALS)
# =====================================================================

def generate_laporan_m3():
    print("="*75)
    print("LAPORAN AKHIR M-3 (MOMEN KELEMBAMAN)".center(75))
    print("="*75)
    
    # ---------------------------------------------------------
    # MODUL 1: Momen Inersia Secara Fisis
    # ---------------------------------------------------------
    print("\n1. Menentukan momen inersia secara fisis untuk benda trapesium :")
    print("Rumus Dasar: I_A = (P^2 * m * g * l) / (4 * pi^2)\n")
    
    pi2 = round(3.14 ** 2, 3)
    penyebut_I = round(4.0 * pi2, 3)
    
    def hitung_fisis(nama, t, l):
        # 1. Cari Periode (P)
        P = round(t / n_ayunan, 3)
        P2 = round(P ** 2, 3)
        
        # 2. Cari I_A (Inersia di titik ayun)
        I_pembilang = round(P2 * m * g * l, 3)
        I_titik = round(I_pembilang / penyebut_I, 3)
        
        # 3. Cari I_pm (Inersia Pusat Massa) = I_A - ml^2
        l2 = round(l ** 2, 3)
        ml2 = round(m * l2, 3)
        I_pm = round(I_titik - ml2, 3)
        
        # Proteksi nilai absolut jika terjadi anomali alat lab
        if I_pm < 0: I_pm = abs(I_pm)
        
        print(f"Titik {nama}:")
        print(f"  P_{nama}   = {t} / {n_ayunan} = {P:.3f} s")
        print(f"  I_{nama}   = {I_titik:.3f} gr.cm^2")
        print(f"  I_pm_{nama} = {I_titik:.3f} - {ml2:.3f} = {I_pm:.3f} gr.cm^2\n")
        return I_pm

    I_pm_A = hitung_fisis("A", t_A, l_A)
    I_pm_B = hitung_fisis("B", t_B, l_B)
    I_pm_C = hitung_fisis("C", t_C, l_C)
    I_pm_D = hitung_fisis("D", t_D, l_D)
    
    sum_I_pm = round(I_pm_A + I_pm_B, 3)
    sum_I_pm = round(sum_I_pm + I_pm_C, 3)
    sum_I_pm = round(sum_I_pm + I_pm_D, 3)
    
    I_pm_tot = round(sum_I_pm / 4.0, 3)
    print(f"I_pm_tot (Fisis) = ({I_pm_A:.3f} + {I_pm_B:.3f} + {I_pm_C:.3f} + {I_pm_D:.3f}) / 4")
    print(f"I_pm_tot (Fisis) = {I_pm_tot:.3f} gr.cm^2\n")

    # ---------------------------------------------------------
    # MODUL 2: Momen Inersia Secara Matematis
    # ---------------------------------------------------------
    print("-" * 75)
    print("2. Menentukan momen inersia secara matematis untuk benda trapesium :\n")
    
    # Perhitungan Massa Pecahan (m1, m2, m3)
    ac = round(a * c, 3)
    b_plus_c = round(b + c, 3)
    setengah_a = round(0.5 * a, 3)
    term_luas1 = round(setengah_a * b_plus_c, 3)
    
    r2 = round(r ** 2, 3)
    pi_r2 = round(pi * r2, 3)
    
    penyebut_m1 = round(term_luas1 - pi_r2, 3)
    m1_pemb = round(ac * m, 3)
    m1 = round(m1_pemb / penyebut_m1, 3)
    
    a_kali_bc = round(a * b_plus_c, 3)
    dua_pi_r2 = round(2.0 * pi_r2, 3)
    penyebut_m2 = round(a_kali_bc - dua_pi_r2, 3)
    m2_pemb = round(a_kali_bc * m, 3)
    m2 = round(m2_pemb / penyebut_m2, 3)
    
    m3_pemb = round(pi_r2 * m, 3)
    m3 = round(m3_pemb / penyebut_m1, 3) # Penyebut m3 sama dgn m1 sesuai rumus

    print(f"m1 = {m1:.3f} gr")
    print(f"m2 = {m2:.3f} gr")
    print(f"m3 = {m3:.3f} gr\n")
    
    # Perhitungan I_pm pecahan
    a2 = round(a ** 2, 3)
    b2 = round(b ** 2, 3)
    a2_plus_b2 = round(a2 + b2, 3)
    
    I_pm1_term = round(m1 * a2_plus_b2, 3)
    I_pm1 = round(I_pm1_term / 12.0, 3)
    
    I_pm2_term = round(m2 * a2_plus_b2, 3)
    I_pm2 = round(I_pm2_term / 18.0, 3)
    
    I_pm3_term = round(m3 * r2, 3)
    I_pm3 = round(I_pm3_term / 2.0, 3)
    
    # Pergeseran sumbu sejajar
    l1_sq = round(l1 ** 2, 3)
    m1_l1_sq = round(m1 * l1_sq,     3)
    
    l2_sq = round(l2 ** 2, 3)
    m2_l2_sq = round(m2 * l2_sq, 3)
    
    l3_sq = round(l3 ** 2, 3)
    m3_l3_sq = round(m3 * l3_sq, 3)
    
    # Akumulasi Matematis Total (Mengikuti tanda persis di buku petunjuk)
    I_pm_mat = round(I_pm1 + I_pm2, 3)
    I_pm_mat = round(I_pm_mat + I_pm3, 3) # Berdasarkan tanda '+' di lembar
    I_pm_mat = round(I_pm_mat + m1_l1_sq, 3)
    I_pm_mat = round(I_pm_mat + m2_l2_sq, 3)
    I_pm_mat = round(I_pm_mat - m3_l3_sq, 3)
    
    print(f"I_pm1 = {I_pm1:.3f} gr.cm^2")
    print(f"I_pm2 = {I_pm2:.3f} gr.cm^2")
    print(f"I_pm3 = {I_pm3:.3f} gr.cm^2")
    print(f"\nI_pm_tot (Matematis) = {I_pm_mat:.3f} gr.cm^2\n")

    # ---------------------------------------------------------
    # MODUL 3 & 4: Tabel Perbandingan dan Girasi
    # ---------------------------------------------------------
    print("-" * 75)
    print("3. Perbandingan perhitungan momen inersia secara matematis dan fisis :\n")
    
    selisih_I = round(abs(I_pm_mat - I_pm_tot), 3)
    kesalahan_I = round((selisih_I / I_pm_mat) * 100.0, 3)
    
    print(f"| Benda                 | Ipm matematis | Ipm fisis    | Kesalahan (%) |")
    print(f"|-----------------------|---------------|--------------|---------------|")
    print(f"| Trapesium Berlubang   | {I_pm_mat:<13.3f} | {I_pm_tot:<12.3f} | {kesalahan_I:<13.3f} |")
    
    print("\n" + "-" * 75)
    print("4. Menentukan Jari - jari Girasi :\n")
    
    K_mat_sq = round(I_pm_mat / m, 3)
    K_mat = round(math.sqrt(K_mat_sq), 3)
    
    K_fis_sq = round(I_pm_tot / m, 3)
    K_fis = round(math.sqrt(K_fis_sq), 3)
    
    selisih_K = round(abs(K_mat - K_fis), 3)
    kesalahan_K = round((selisih_K / K_mat) * 100.0, 3)
    
    print(f"| Benda                 | K matematis   | K fisis      | Kesalahan (%) |")
    print(f"|-----------------------|---------------|--------------|---------------|")
    print(f"| Trapesium Berlubang   | {K_mat:<13.3f} | {K_fis:<12.3f} | {kesalahan_K:<13.3f} |")

    # ---------------------------------------------------------
    # MODUL 5 & 6: Output Template
    # ---------------------------------------------------------
    print("\n" + "="*75)
    print("5. Analisa Percobaan:")
    print("   [Ulas mengapa selisih persentase di atas bisa terjadi. Fokus pada:")
    print("    1. Gesekan udara saat ayunan.")
    print("    2. Ketidaktepatan menentukan titik pusat massa secara manual.")
    print("    3. Waktu reaksi manusia saat menekan stopwatch.]")
    print("\n6. Kesimpulan dan Saran")
    print("   Kesimpulan: [Tuliskan perbandingan akhir I_pm dan K dari fisis vs matematis]")
    print("   Saran: [Sarankan penggunaan sensor gerak digital untuk akurasi waktu]")
    print("="*75)

# Eksekusi fungsi
generate_laporan_m3()