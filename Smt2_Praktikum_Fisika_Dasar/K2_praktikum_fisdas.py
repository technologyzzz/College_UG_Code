import math

# =====================================================================
# BAGIAN INPUT DATA (Telah disesuaikan dengan Lembar Data Pengamatan)
# =====================================================================

# 1. Data Percobaan A (Menentukan nilai air kalorimeter)
M_k = 511         # Massa kalorimeter (gr)
M_ka1 = 632       # Massa kalorimeter & air (gr)
T_a = 25          # Suhu air dingin (°C)
T_p = 75          # Suhu air panas (°C)
T_s = 50          # Suhu setimbang (°C)
M_total = 892     # Massa M(k+a+p) (gr)
C_a = 1           # Panas jenis air (kal/gr°C)

# 2. Data Percobaan B (Menentukan Konstanta Joule)
M_ka2 = 618       # Massa kalorimeter & air percobaan 2 (gr)
V = 10            # Tegangan (Volt)
I = 2             # Kuat Arus (Ampere)

# Tabel Data: [Suhu T (°C), Waktu t (menit)]
# Sistem otomatis akan mengubah menit menjadi detik dalam perhitungan
data_joule = [
    [28.0, 0.0],
    [30.0, 2.0],
    [32.0, 4.0],
    [34.0, 6.0],
    [36.0, 8.0],
    [37.0, 10.0],
    [38.0, 12.0],
    [40.0, 14.0],
    [42.0, 16.0],
    [43.0, 18.0]
]

# =====================================================================
# CORE ENGINE - STRICT CHAINED ROUNDING (3 DECIMALS)
# =====================================================================

def generate_laporan_k2():
    print("="*75)
    print("LAPORAN AKHIR K-2".center(75))
    print("="*75)
    
    # ---------------------------------------------------------
    # MODUL 1: Menentukan nilai kalorimeter
    # ---------------------------------------------------------
    print("\n1. Menentukan nilai kalorimeter")
    print("Persamaan yang digunakan :")
    print("Map . Ca . (Tap - Ts) = (Ma . Ca + Na) . (Ts - Ta)\n")
    
    # Logika Chained Rounding
    M_ap = round(M_total - M_ka1, 3)
    M_a = round(M_ka1 - M_k, 3)
    
    # Perhitungan Na terpisah
    pembilang_Na = round(round(M_ap * C_a, 3) * round(T_p - T_s, 3), 3)
    penyebut_Na = round(T_s - T_a, 3)
    suku1_Na = round(pembilang_Na / penyebut_Na, 3)
    suku2_Na = round(M_a * C_a, 3)
    
    Na = round(suku1_Na - suku2_Na, 3)
    
    print(f"dimana : Map = M(k+a+p) - M(k+a) = {M_total:.3f} - {M_ka1:.3f} = {M_ap:.3f} gram")
    print(f"         Ma  = M(k+a) - Mk     = {M_ka1:.3f} - {M_k:.3f}  = {M_a:.3f} gram")
    print(f"         Tap = Suhu air panas  = {T_p:.3f} °C")
    print(f"         Ta  = Suhu air dingin = {T_a:.3f} °C")
    print(f"         Ts  = Suhu setimbang  = {T_s:.3f} °C")
    print(f"         Ca  = Panas jenis air = {C_a:.3f} kal/gr°C\n")
    
    print(f"         Didapat Na = {Na:.3f} kal/°C")
    
    # ---------------------------------------------------------
    # MODUL 2: Menentukan Konstanta Joule (J)
    # ---------------------------------------------------------
    print("\n2. Menentukan konstanta Joule (J)")
    
    M_a2 = round(M_ka2 - M_k, 3)
    print(f"\nMa2 = M(k+a)2 - Mk = {M_ka2:.3f} - {M_k:.3f} = {M_a2:.3f} gr\n")
    
    # Ekstraksi T0
    T0 = round(data_joule[0][0], 3)
    
    print("TABEL PERCOBAAN:")
    print("-" * 65)
    print(f"| {'No':<2} | {'ΔT (°C)':<10} | {'t (detik)':<10} | {'t²':<12} | {'ΔT . t':<15} |")
    print("-" * 65)
    
    sum_delta_T = 0.0
    sum_t = 0.0
    sum_t2 = 0.0
    sum_delta_T_t = 0.0
    n = len(data_joule)
    
    for i, row in enumerate(data_joule):
        T_n = row[0]
        t_menit = row[1]
        
        # Logika Rounding Step-by-step
        delta_T = round(T_n - T0, 3)
        t_detik = round(t_menit * 60.0, 3)
        t2 = round(t_detik ** 2, 3)
        deltaT_x_t = round(delta_T * t_detik, 3)
        
        # Akumulator
        sum_delta_T = round(sum_delta_T + delta_T, 3)
        sum_t = round(sum_t + t_detik, 3)
        sum_t2 = round(sum_t2 + t2, 3)
        sum_delta_T_t = round(sum_delta_T_t + deltaT_x_t, 3)
        
        # Output label T1-T0, T2-T0
        label_T = f"T{i}-T0"
        print(f"| {i+1:<2} | {delta_T:<10.3f} | {t_detik:<10.3f} | {t2:<12.3f} | {deltaT_x_t:<15.3f} |")
        
    print("-" * 65)
    print(f"| N={n} | Σ={sum_delta_T:<8.3f} | Σ={sum_t:<8.3f} | Σ={sum_t2:<10.3f} | Σ={sum_delta_T_t:<13.3f} |")
    print("-" * 65)
    
    # Perhitungan Regresi Linear
    n_kali_sum_t2 = round(n * sum_t2, 3)
    kuadrat_sum_t = round(sum_t ** 2, 3)
    penyebut_ab = round(n_kali_sum_t2 - kuadrat_sum_t, 3)
    
    if penyebut_ab == 0:
        print("[!] Pembagi nol pada regresi linear.")
        return
        
    # Mencari nilai a
    a_term1 = round(sum_t2 * sum_delta_T, 3)
    a_term2 = round(sum_t * sum_delta_T_t, 3)
    a_pembilang = round(a_term1 - a_term2, 3)
    a = round(a_pembilang / penyebut_ab, 3) # sengaja diperlebar sementara untuk stabilitas b, 
    a_tampil = round(a, 3)                  # tapi tampilan tetap 3 desimal
    
    # Mencari nilai b
    b_term1 = round(n * sum_delta_T_t, 3)
    b_term2 = round(sum_t * sum_delta_T, 3)
    b_pembilang = round(b_term1 - b_term2, 3)
    b = round(b_pembilang / penyebut_ab, 3) # sengaja diperlebar sementara untuk stabilitas b
    b_tampil = round(b, 3)                  # b gradien sering bernilai sangat kecil
    
    print(f"\nDengan demikian didapatkan persamaan garis lurus :")
    print(f"a = {a_tampil:.3f}")
    print(f"b = {b_tampil:.3f}") # menggunakan 5 desimal khusus b karena nilainya sangat kecil
    print(f"ΔT = {b_tampil:.3f} t + ({a_tampil:.3f})\n")
    
    # Perhitungan J
    V_kali_I = round(V * I, 3)
    Ma2_kali_Ca = round(M_a2 * C_a, 3)
    Na_tambah_Ma2Ca = round(Na + Ma2_kali_Ca, 3)
    penyebut_J = round(Na_tambah_Ma2Ca * b, 3)
    
    J = round(V_kali_I / penyebut_J, 3)
    
    J_lit = 4.2
    selisih_J = round(abs(J_lit - J), 3)
    kesalahan_lit = round((selisih_J / J_lit) * 100.0, 3)
    
    print(f"J = V.I / ((Na + Ma2.Ca) * b)")
    print(f"J = {V_kali_I:.3f} / ({Na_tambah_Ma2Ca:.3f} * {b_tampil:.3f})")
    print(f"J = {J:.3f} (Joule / Kalori)\n")
    
    print(f"J_LIT = 4.2 Joule / Kalori")
    print(f"Kesalahan literatur = |(J_lit - J) / J_lit| x 100% = {kesalahan_lit:.3f} %")
    
    # ---------------------------------------------------------
    # MODUL Output Template
    # ---------------------------------------------------------
    print("\n" + "="*75)
    print("4. Analisa Percobaan")
    print("   [Tulis ulasan eksekusi praktikum, kenapa nilai error bisa terjadi]")
    print("\n5. Kesimpulan dan Saran")
    print("   Kesimpulan:")
    print("   [Tulis hasil akhir nilai Kalorimeter dan Konstanta Joule di sini]")
    print("   Saran:")
    print("   [Tulis apa perbaikan praktikum untuk mengurangi nilai error]")
    print("="*75)

# Eksekusi fungsi utama
generate_laporan_k2()