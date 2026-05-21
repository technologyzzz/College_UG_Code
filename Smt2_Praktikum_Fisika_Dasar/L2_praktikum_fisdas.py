"""
data_hambatan_murni = [
    [100, 51.9, 48.1],  # Data 1
    [200, 33.7, 66.3],  # Data 2
    [300, 24.8, 75.2],  # Data 3
    [400, 19.8, 80.2],  # Data 4
    [500, 15.8, 84.2],  # Data 5
    [600, 13.5, 86.5],  # Data 6
    [700, 11.7, 88.3],  # Data 7
    [800, 10.2, 89.8],  # Data 8
    [900, 9.2, 90.8],  # Data 9
    [1000, 7.7, 92.3]   # Data 10
]

data_termistor = [
    [300, 43.9, 56.1],  # Data 1 (T0 akan diambil dari baris ini)
    [303, 40, 60],  # Data 2
    [306, 38.1, 61.9],  # Data 3
    [309, 36.9, 63.1],  # Data 4
    [312, 34.6, 65.4],  # Data 5
    [315, 31.9, 68.1],  # Data 6
    [318, 31, 69],  # Data 7
    [321, 29, 71],  # Data 8
    [324, 27.2, 72.8],  # Data 9
    [327, 26.3, 73.7]   # Data 10
]
"""

"""

"""

import math

# =====================================================================
# BAGIAN INPUT DATA (SILAKAN GANTI ANGKA DENGAN DATA ASLI ANDA)
# =====================================================================

# 1. Data Hambatan Murni
# Format list: [Rs (ohm), l1 (cm), l2 (cm)]
data_hambatan_murni = [
    [100, 51, 49],  # Data 1
    [200, 34.2, 65.8],  # Data 2
    [300, 24.8, 75.2],  # Data 3
    [400, 19.8, 80.2],  # Data 4
    [500, 16, 84],  # Data 5
    [600, 13.7, 86.3],  # Data 6
    [700, 12.2, 87.8],  # Data 7
    [800, 10.6, 89.4],  # Data 8
    [900, 9.4, 90.6],  # Data 9
    [1000, 8.7, 91.3]   # Data 10
]

# 2. Data Koefisien Temperatur (Termistor)
Rs_termistor = 3.0  # Isi nilai Rs (ohm) yang digunakan untuk termistor

# Format list: [Suhu T (Celcius), l1 (cm), l2 (cm)]
data_termistor = [
    [27, 44.3, 55.7],  # Data 1 (T0 akan diambil dari baris ini)
    [30, 33.5, 66.5],  # Data 2
    [33, 32.4, 67.6],  # Data 3
    [36, 30.7, 69.3],  # Data 4
    [39, 29.5, 70.5],  # Data 5
    [42, 28.5, 71.5],  # Data 6
    [45, 26.8, 73.2],  # Data 7
    [48, 25, 75],  # Data 8
    [51, 23.7, 76.3],  # Data 9
    [54, 21, 79]   # Data 10
]

# =====================================================================
# CORE ENGINE - WITH STRICT CHAINED ROUNDING (3 DECIMALS)
# =====================================================================

def generate_laporan():
    print("="*75)
    print("LAPORAN AKHIR L-2".center(75))
    print("="*75)
    
    # ---------------------------------------------------------
    # MODUL 1: Menghitung besar Rx untuk hambatan murni
    # ---------------------------------------------------------
    print("\n1. Menghitung besar Rx untuk hambatan murni.")
    print("   Rx = (l1 / l2) * Rs\n")
    
    print("-" * 68)
    print(f"| {'No':<2} | {'Rs (ohm)':<10} | {'l1 (cm)':<10} | {'l2 (cm)':<10} | {'Rx (ohm)':<10} | {'Rx^2':<10} |")
    print("-" * 68)
    
    sum_Rx = 0.0
    sum_Rx2 = 0.0
    n1 = len(data_hambatan_murni)
    
    for i, row in enumerate(data_hambatan_murni):
        Rs, l1, l2 = row
        
        # LOGIC ROUNDING
        Rx = round((l1 / l2) * Rs, 3)
        Rx2 = round(Rx ** 2, 3)
        
        sum_Rx = round(sum_Rx + Rx, 3)
        sum_Rx2 = round(sum_Rx2 + Rx2, 3)
        
        print(f"| {i+1:<2} | {Rs:<10.3f} | {l1:<10.3f} | {l2:<10.3f} | {Rx:<10.3f} | {Rx2:<10.3f} |")
    
    print("-" * 68)
    print(f"| {'n='+str(n1):<42} | ΣRx={sum_Rx:.3f} | ΣRx²={sum_Rx2:.3f}|")
    print("-" * 68)
    
    # Perhitungan Statistik Bagian 1
    Rx_bar = round(sum_Rx / n1, 3)
    
    # Ralat Delta Rx
    kuadrat_sum_Rx = round(sum_Rx ** 2, 3)
    n_kali_sum_Rx2 = round(n1 * sum_Rx2, 3)
    delta_Rx_pembilang = round(n_kali_sum_Rx2 - kuadrat_sum_Rx, 3)
    delta_Rx_penyebut = round((n1 ** 2) * (n1 - 1), 3)
    
    if delta_Rx_pembilang < 0: delta_Rx_pembilang = 0.0
    
    if delta_Rx_penyebut != 0:
        delta_Rx = round(math.sqrt(delta_Rx_pembilang / delta_Rx_penyebut), 3)
    else:
        delta_Rx = 0.0
        
    if Rx_bar != 0:
        kesalahan_relatif_1 = round((delta_Rx / Rx_bar) * 100, 3)
    else:
        kesalahan_relatif_1 = 0.0
    
    print(f"\nRata-rata Rx (R_bar)   = {Rx_bar:.3f} ohm")
    print(f"ΔRx                    = {delta_Rx:.3f} ohm")
    print(f"Jadi besarnya hambatan murni = ({Rx_bar:.3f} ± {delta_Rx:.3f}) ohm")
    print(f"Kesalahan Relatif      = {kesalahan_relatif_1:.3f} %\n")
    
    
    # ---------------------------------------------------------
    # MODUL 2: Menentukan koefisien temperatur (b)
    # ---------------------------------------------------------
    print("\n2. Menentukan koefisien temperatur (b).")
    print(f"   Rs = {Rs_termistor:.3f} ohm\n")
    
    T0_C = round(data_termistor[0][0], 3)
    T0_K = round(T0_C + 273.0, 3)
    
    print("TABEL 1: Perhitungan Hambatan Termistor (RT)")
    print("-" * 65)
    print(f"| {'No':<2} | {'T (K)':<8} | {'l1 (cm)':<8} | {'l2 (cm)':<8} | {'RT (ohm)':<8} | {'ΔT (K)':<8} |")
    print("-" * 65)
    
    tabel2_data = []
    sum_lnRt = 0.0
    sum_deltaT = 0.0
    sum_deltaT2 = 0.0
    sum_lnRt_deltaT = 0.0
    n2 = len(data_termistor)
    RT0 = 0.0 
    
    for i, row in enumerate(data_termistor):
        T_C, l1, l2 = row
        T_K = round(T_C + 273.0, 3)
        delta_T = round(T_K - T0_K, 3)
        
        RT = round((l1 / l2) * Rs_termistor, 3)
        if i == 0:
            RT0 = RT
            
        ln_RT = round(math.log(RT), 3)
        delta_T2 = round(delta_T ** 2, 3)
        lnRT_x_deltaT = round(ln_RT * delta_T, 3)
        
        # Akumulasi Sigma dengan strict rounding
        sum_lnRt = round(sum_lnRt + ln_RT, 3)
        sum_deltaT = round(sum_deltaT + delta_T, 3)
        sum_deltaT2 = round(sum_deltaT2 + delta_T2, 3)
        sum_lnRt_deltaT = round(sum_lnRt_deltaT + lnRT_x_deltaT, 3)
        
        tabel2_data.append([ln_RT, delta_T, delta_T2, lnRT_x_deltaT])
        
        print(f"| {i+1:<2} | {T_K:<8.3f} | {l1:<8.3f} | {l2:<8.3f} | {RT:<8.3f} | {delta_T:<8.3f} |")
        
    print("-" * 65)
    
    print("\nTABEL 2: Perhitungan Regresi Linear (Least Square)")
    print("-" * 66)
    print(f"| {'No':<2} | {'ln RT':<10} | {'ΔT':<10} | {'ΔT^2':<10} | {'ln RT . ΔT':<12} |")
    print("-" * 66)
    
    for i, row in enumerate(tabel2_data):
        print(f"| {i+1:<2} | {row[0]:<10.3f} | {row[1]:<10.3f} | {row[2]:<10.3f} | {row[3]:<12.3f} |")
    
    print("-" * 66)
    print(f"| {'n=' + str(n2):<2} | Σ={sum_lnRt:<8.3f} | Σ={sum_deltaT:<8.3f} | Σ={sum_deltaT2:<8.3f} | Σ={sum_lnRt_deltaT:<10.3f} |")
    print("-" * 66)
    
    # Perhitungan Regresi dengan strict rounding step-by-step
    kuadrat_sum_deltaT = round(sum_deltaT ** 2, 3)
    n_kali_sum_deltaT2 = round(n2 * sum_deltaT2, 3)
    pembagi = round(n_kali_sum_deltaT2 - kuadrat_sum_deltaT, 3)
    
    if pembagi == 0:
        print("\n[!] ERROR: Pembagi regresi 0. Pastikan nilai Suhu bervariasi (tidak sama semua).")
        return
    
    # Menghitung a
    a_term1 = round(sum_deltaT2 * sum_lnRt, 3)
    a_term2 = round(sum_deltaT * sum_lnRt_deltaT, 3)
    a_pembilang = round(a_term1 - a_term2, 3)
    a = round(a_pembilang / pembagi, 3)
    
    # Menghitung b
    b_term1 = round(n2 * sum_lnRt_deltaT, 3)
    b_term2 = round(sum_deltaT * sum_lnRt, 3)
    b_pembilang = round(b_term1 - b_term2, 3)
    b = round(b_pembilang / pembagi, 3)
    
    # Menghitung R0 dan Kesalahan
    R0_calc = round(math.exp(a), 3)
    
    if RT0 != 0:
        selisih_RT0 = round(abs(RT0 - R0_calc), 3)
        kesalahan_literatur = round((selisih_RT0 / RT0) * 100, 3)
    else:
        kesalahan_literatur = 0.0
        
    print(f"\nNilai a (ln R0)          = {a:.3f}")
    print(f"Nilai b (koef. suhu)     = {b:.3f}")
    print(f"Jadi koefisien temperaturnya = {b:.3f} °K^-1")
    
    print("\nDari hasil a dan b di atas didapat persamaan garis :")
    print("ln RT = b . ΔT + ln R0")
    print(f"ln RT = {b:.3f} . ΔT + {a:.3f}")
    
    print(f"\nR0 = e^a = e^({a:.3f}) = {R0_calc:.3f} Ω")
    print(f"Kesalahan literatur = |(RT0 - R0) / RT0| x 100% = {kesalahan_literatur:.3f} %")
    
    # ---------------------------------------------------------
    # MODUL 3 & 4: Output Teks Template
    # ---------------------------------------------------------
    print("\n" + "="*75)
    print("3. Analisa percobaan :")
    print("   Berisi ulasan dan pendapat terhadap pelaksanaan pengambilan data dan")
    print("   pengolahannya serta hasil yang didapat dibandingkan dengan teori yang dipakai.")
    print("\n4. Kesimpulan dan Saran :")
    print("   Kesimpulan:")
    print("   Berisi kesimpulan hasil percobaan sesuai dengan tujuan percobaan dan teorinya.")
    print("   Saran:")
    print("   Berisi bagaimana perbaikan terhadap perbedaan hasil praktikum dan teori yang dipakai.")
    print("="*75)

# Eksekusi fungsi utama
generate_laporan()