import math

# =====================================================================
# BAGIAN INPUT DATA (Telah disesuaikan dengan Lembar L-1)
# =====================================================================

# Nilai Resistor Pengamatan (Ohm)
R1 = 150.0
R2 = 200.0
R3 = 200.0
R4 = 70.0 # R4 ada di data namun tidak dipakai di persamaan modul ini

# 1. Rangkaian Seri (Gambar 3)
E1_seri = 5.0
V_AB = 1.8
V_BC = 3.4
V_AC = 5.2
I_seri_mA = 15.0  

# 2. Rangkaian Paralel (Gambar 4)
E1_par = 5.0
I_par_mA = 65.0
I1_par_mA = 35.0
I2_par_mA = 170.0
I3_par_mA = 210.0

# 3. Multiloop (Gambar 6)
E1_ml = 5.0
E2_ml = 8.0
E3_ml = 9.0
I_ml_mA = 30.0
I1_ml_mA = 120.0
I2_ml_mA = 250.0

# =====================================================================
# CORE ENGINE - STRICT CHAINED ROUNDING (3 DECIMALS) & DETAILED OUTPUT
# =====================================================================

def generate_laporan_l1():
    print("="*75)
    print("LAPORAN AKHIR L-1 (HUKUM KIRCHOFF)".center(75))
    print("="*75)
    
    # ---------------------------------------------------------
    # MODUL 1: Rangkaian Seri
    # ---------------------------------------------------------
    print("\n[PERINCIAN DETAIL] 1. Rangkaian Seri")
    I_seri_A = round(I_seri_mA * 0.001, 3)
    print(f"Konversi Arus: I = {I_seri_mA} mA = {I_seri_A:.3f} A")
    
    # Perhitungan
    R1_per = round(V_AB / I_seri_A, 3)
    R2_per = round(V_BC / I_seri_A, 3)
    Rt_per = round(V_AC / I_seri_A, 3)
    print(f"R1_perhitungan = V_AB / I = {V_AB} / {I_seri_A} = {R1_per:.3f} Ω")
    print(f"R2_perhitungan = V_BC / I = {V_BC} / {I_seri_A} = {R2_per:.3f} Ω")
    print(f"Rt_perhitungan = V_AC / I = {V_AC} / {I_seri_A} = {Rt_per:.3f} Ω")
    
    # Pengamatan
    Rt_peng = round(R1 + R2, 3)
    print(f"Rt_pengamatan  = R1 + R2 = {R1} + {R2} = {Rt_peng:.3f} Ω")
    
    # Kesalahan Relatif
    def hitung_kesalahan(per, peng):
        if per == 0: return 0.0
        selisih = round(abs(per - peng), 3)
        return round((selisih / per) * 100.0, 3)

    err_R1_seri = hitung_kesalahan(R1_per, R1)
    err_R2_seri = hitung_kesalahan(R2_per, R2)
    err_Rt_seri = hitung_kesalahan(Rt_per, Rt_peng)

    print("\n1. Rangkaian Seri (Gambar 3)")
    print("-" * 65)
    print(f"| {'R':<2} | {'Pengamatan (Ω)':<15} | {'Perhitungan (Ω)':<16} | {'Kesalahan rel. %':<16} |")
    print("-" * 65)
    print(f"| R1 | {R1:<15.3f} | {R1_per:<16.3f} | {err_R1_seri:<16.3f} |")
    print(f"| R2 | {R2:<15.3f} | {R2_per:<16.3f} | {err_R2_seri:<16.3f} |")
    print(f"| Rt | {Rt_peng:<15.3f} | {Rt_per:<16.3f} | {err_Rt_seri:<16.3f} |")
    print("-" * 65)

    # ---------------------------------------------------------
    # MODUL 2: Rangkaian Paralel
    # ---------------------------------------------------------
    print("\n[PERINCIAN DETAIL] Rangkaian Paralel")
    I_par_A = round(I_par_mA * 0.001, 3)
    I1_par_A = round(I1_par_mA * 0.001, 3)
    I2_par_A = round(I2_par_mA * 0.001, 3)
    I3_par_A = round(I3_par_mA * 0.001, 3)
    
    print(f"Konversi I1 = {I1_par_mA} mA = {I1_par_A:.3f} A")
    print(f"Konversi I2 = {I2_par_mA} mA = {I2_par_A:.3f} A")
    print(f"Konversi I3 = {I3_par_mA} mA = {I3_par_A:.3f} A")
    print(f"Konversi I_tot = {I_par_mA} mA = {I_par_A:.3f} A")

    # Perhitungan
    R1_par_per = round(E1_par / I1_par_A, 3) if I1_par_A != 0 else 0
    R2_par_per = round(E1_par / I2_par_A, 3) if I2_par_A != 0 else 0
    R3_par_per = round(E1_par / I3_par_A, 3) if I3_par_A != 0 else 0
    Rt_par_per = round(E1_par / I_par_A, 3) if I_par_A != 0 else 0
    
    print(f"R1_perhitungan = E1 / I1 = {E1_par} / {I1_par_A} = {R1_par_per:.3f} Ω")
    print(f"R2_perhitungan = E1 / I2 = {E1_par} / {I2_par_A} = {R2_par_per:.3f} Ω")
    print(f"R3_perhitungan = E1 / I3 = {E1_par} / {I3_par_A} = {R3_par_per:.3f} Ω")
    print(f"Rt_perhitungan = E1 / I = {E1_par} / {I_par_A} = {Rt_par_per:.3f} Ω")
    
    # Pengamatan Rt Paralel (Hukum Kirchhoff)
    seper_R1 = round(1.0 / R1, 6) # Diekstrak lebih presisi sedikit sebelum dibulatkan 3
    seper_R2 = round(1.0 / R2, 6)
    seper_R3 = round(1.0 / R3, 6)
    seper_Rt = round(seper_R1 + seper_R2 + seper_R3, 6)
    Rt_par_peng = round(1.0 / seper_Rt, 3)
    print(f"Rt_pengamatan  = 1 / (1/{R1} + 1/{R2} + 1/{R3}) = {Rt_par_peng:.3f} Ω")
    
    err_R1_par = hitung_kesalahan(R1_par_per, R1)
    err_R2_par = hitung_kesalahan(R2_par_per, R2)
    err_R3_par = hitung_kesalahan(R3_par_per, R3)
    err_Rt_par = hitung_kesalahan(Rt_par_per, Rt_par_peng)

    print("\nRangkaian Paralel (Gambar 4)")
    print("-" * 65)
    print(f"| {'R':<2} | {'Pengamatan (Ω)':<15} | {'Perhitungan (Ω)':<16} | {'Kesalahan rel. %':<16} |")
    print("-" * 65)
    print(f"| R1 | {R1:<15.3f} | {R1_par_per:<16.3f} | {err_R1_par:<16.3f} |")
    print(f"| R2 | {R2:<15.3f} | {R2_par_per:<16.3f} | {err_R2_par:<16.3f} |")
    print(f"| R3 | {R3:<15.3f} | {R3_par_per:<16.3f} | {err_R3_par:<16.3f} |")
    print(f"| Rt | {Rt_par_peng:<15.3f} | {Rt_par_per:<16.3f} | {err_Rt_par:<16.3f} |")
    print("-" * 65)


    # ---------------------------------------------------------
    # MODUL 3: Multiloop
    # ---------------------------------------------------------
    print("\n[PERINCIAN DETAIL] 2. Multiloop")
    # Denominator: R1.R2 + R1.R3 + R2.R3
    R1R2 = round(R1 * R2, 3)
    R1R3 = round(R1 * R3, 3)
    R2R3 = round(R2 * R3, 3)
    denom_awal = round(R1R2 + R1R3, 3)
    denom = round(denom_awal + R2R3, 3)
    
    print(f"Penyebut = (R1.R2) + (R1.R3) + (R2.R3) = {R1R2} + {R1R3} + {R2R3} = {denom:.3f}")
    
    # Numerator I (Persamaan 1)
    E1_plus_E3 = round(E1_ml + E3_ml, 3)
    E1_min_E2 = round(E1_ml - E2_ml, 3)
    term1_I = round(R2 * E1_plus_E3, 3)
    term2_I = round(R3 * E1_min_E2, 3)
    num_I = round(term1_I + term2_I, 3)
    
    print(f"Pembilang I  = R2(E1+E3) + R3(E1-E2) = {term1_I} + {term2_I} = {num_I:.3f}")
    
    # Numerator I1 (Persamaan 2)
    E2_plus_E3 = round(E2_ml + E3_ml, 3)
    term1_I1 = round(R3 * E1_min_E2, 3)
    term2_I1 = round(R1 * E2_plus_E3, 3)
    num_I1 = round(term1_I1 - term2_I1, 3)
    
    print(f"Pembilang I1 = R3(E1-E2) - R1(E2+E3) = {term1_I1} - {term2_I1} = {num_I1:.3f}")
    
    # Numerator I2 (Persamaan 3)
    term1_I2 = round(R1 * E2_plus_E3, 3)
    term2_I2 = round(R2 * E1_plus_E3, 3)
    num_I2 = round(term1_I2 + term2_I2, 3)
    
    print(f"Pembilang I2 = R1(E2+E3) + R2(E1+E3) = {term1_I2} + {term2_I2} = {num_I2:.3f}")
    
    # Hitung Arus Ampere
    I_calc_A = round(num_I / denom, 3)
    I1_calc_A = round(num_I1 / denom, 3)
    I2_calc_A = round(num_I2 / denom, 3)
    
    # Konversi ke miliAmpere (x1000)
    I_calc_mA = round(I_calc_A * 1000.0, 3)
    I1_calc_mA = round(I1_calc_A * 1000.0, 3)
    I2_calc_mA = round(I2_calc_A * 1000.0, 3)
    
    print(f"I_perhitungan  = {num_I} / {denom} = {I_calc_A} A = {I_calc_mA} mA")
    print(f"I1_perhitungan = {num_I1} / {denom} = {I1_calc_A} A = {I1_calc_mA} mA")
    print(f"I2_perhitungan = {num_I2} / {denom} = {I2_calc_A} A = {I2_calc_mA} mA")
    
    # Kesalahan Multiloop
    err_I_ml = hitung_kesalahan(I_calc_mA, I_ml_mA)
    err_I1_ml = hitung_kesalahan(I1_calc_mA, I1_ml_mA)
    err_I2_ml = hitung_kesalahan(I2_calc_mA, I2_ml_mA)

    print("\n2. Multiloop (Gambar 6)")
    print("-" * 65)
    print(f"| {'Arus':<4} | {'Pengamatan (mA)':<15} | {'Perhitungan (mA)':<16} | {'Kesalahan rel %':<15} |")
    print("-" * 65)
    print(f"| I    | {I_ml_mA:<15.3f} | {I_calc_mA:<16.3f} | {err_I_ml:<15.3f} |")
    print(f"| I1   | {I1_ml_mA:<15.3f} | {I1_calc_mA:<16.3f} | {err_I1_ml:<15.3f} |")
    print(f"| I2   | {I2_ml_mA:<15.3f} | {I2_calc_mA:<16.3f} | {err_I2_ml:<15.3f} |")
    print("-" * 65)

    # ---------------------------------------------------------
    # MODUL 4: Output Template Text
    # ---------------------------------------------------------
    print("\n" + "="*75)
    print("3. Analisa Percobaan :")
    print("   [Ulas mengapa selisih persentase pada Multiloop bisa mencapai >100%.")
    print("    Fokuskan pada kesalahan pembacaan skala multimeter oleh praktikan saat")
    print("    praktikum, bukan menyalahkan rumus fisikanya.]")
    print("\n4. Kesimpulan dan saran :")
    print("   Kesimpulan:")
    print("   [Tuliskan bahwa Hukum Kirchoff terbukti pada perhitungan matematis, namun")
    print("    pengamatan fisis dipengaruhi oleh ketelitian alat ukur.]")
    print("   Saran:")
    print("   [Tuliskan pentingnya kalibrasi multimeter dan ketelitian membaca skala.]")
    print("="*75)

# Eksekusi
generate_laporan_l1()