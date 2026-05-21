import math

# =====================================================================
# BAGIAN INPUT DATA (Sesuai Lembar M-1 Bandul Matematis)
# =====================================================================

# L (cm)
data_L = [100.0, 98.0, 93.0, 89.0, 85.0, 81.0, 77.0, 72.0, 67.0, 63.0]

# t (detik) untuk 10 ayunan
data_t = [20.20, 19.40, 19.17, 19.06, 18.02, 17.53, 17.09, 16.75, 16.34, 14.07]

n_ayunan = 10.0
g_lit = 980.0
theta = 30.0

# =====================================================================
# CORE ENGINE - STRICT CHAINED ROUNDING (3 DECIMALS) & DETAILED OUTPUT
# =====================================================================

def generate_laporan_m1():
    print("="*75)
    print("LAPORAN AKHIR M-1 (BANDUL MATEMATIS)".center(75))
    print("="*75)
    
    # Pre-kalkulasi Konstanta Pi dengan Rounding
    pi = 3.14
    pi2 = round(pi ** 2, 3)
    empat_pi2 = round(4.0 * pi2, 3)
    
    print(f"\n[KONSTANTA DASAR]")
    print(f"π = {pi}")
    print(f"π² = {pi2:.3f}")
    print(f"4π² = {empat_pi2:.3f}\n")

    # ---------------------------------------------------------
    # MODUL 1: Menentukan g secara Matematis
    # ---------------------------------------------------------
    print("1. Menentukan g secara Matematis untuk θ = 30°")
    print("   T = t / banyaknya ayunan")
    print("   g = (4π² . l) / T²\n")
    
    print("[PERINCIAN DETAIL MATEMATIS]")
    
    sum_g = 0.0
    sum_g2 = 0.0
    n_data = len(data_L)
    tabel1_data = []

    for i in range(n_data):
        l = data_L[i]
        t = data_t[i]
        
        # Chained Rounding
        T = round(t / n_ayunan, 3)
        T2 = round(T ** 2, 3)
        
        pembilang_g = round(empat_pi2 * l, 3)
        g = round(pembilang_g / T2, 3)
        g2 = round(g ** 2, 3)
        
        sum_g = round(sum_g + g, 3)
        sum_g2 = round(sum_g2 + g2, 3)
        
        tabel1_data.append([l, T, T2, g, g2])
        
        print(f"Data Ke-{i+1} (l={l}):")
        print(f"  T  = {t} / {n_ayunan} = {T:.3f} dt")
        print(f"  T² = {T:.3f}² = {T2:.3f} dt²")
        print(f"  g  = ({empat_pi2} . {l}) / {T2} = {pembilang_g} / {T2} = {g:.3f} cm/dt²")
        print(f"  g² = {g:.3f}² = {g2:.3f} (cm/dt²)²\n")

    print("-" * 75)
    print(f"| {'No':<2} | {'l (cm)':<8} | {'T (dt)':<8} | {'T² (dt²)':<10} | {'g (cm/dt²)':<12} | {'g² (cm²/dt⁴)':<14} |")
    print("-" * 75)
    for i, row in enumerate(tabel1_data):
        print(f"| {i+1:<2} | {row[0]:<8.3f} | {row[1]:<8.3f} | {row[2]:<10.3f} | {row[3]:<12.3f} | {row[4]:<14.3f} |")
    print("-" * 75)
    print(f"| {'n=' + str(n_data):<33} | Σg={sum_g:<9.3f} | Σg²={sum_g2:<12.3f} |")
    print("-" * 75)

    # Perhitungan Statistik Modul 1
    g_bar = round(sum_g / n_data, 3)
    
    n_kali_sum_g2 = round(n_data * sum_g2, 3)
    kuadrat_sum_g = round(sum_g ** 2, 3)
    delta_g_pembilang = round(n_kali_sum_g2 - kuadrat_sum_g, 3)
    delta_g_penyebut = round((n_data ** 2) * (n_data - 1), 3)
    
    if delta_g_pembilang < 0: delta_g_pembilang = 0.0
    delta_g = round(math.sqrt(delta_g_pembilang / delta_g_penyebut), 3)
    
    kesalahan_relatif = round((delta_g / g_bar) * 100.0, 3)
    selisih_lit1 = round(abs(g_bar - g_lit), 3)
    kesalahan_literatur1 = round((selisih_lit1 / g_lit) * 100.0, 3)

    print(f"\nDimana : g_bar = Σg / n = {sum_g} / {n_data} = {g_bar:.3f} cm/dt²")
    print(f"Sehingga diperoleh : g = ( g_bar ± Δg )")
    print(f"                     = ( {g_bar:.3f} ± {delta_g:.3f} ) cm/dt²")
    print(f"Kesalahan relatif  = (Δg / g_bar) x 100% = {kesalahan_relatif:.3f} %")
    print(f"Kesalahan Literatur= |(g_bar - g_Lit) / g_Lit| x 100% = {kesalahan_literatur1:.3f} %\n")

    # ---------------------------------------------------------
    # MODUL 2: Menentukan g dengan metode kuadrat terkecil
    # ---------------------------------------------------------
    print("2. Menentukan g dengan metode kuadrat terkecil untuk θ = 30°")
    
    print("\n[PERINCIAN DETAIL LEAST SQUARES (X = l, Y = T²)]")
    
    sum_X = 0.0
    sum_Y = 0.0
    sum_X2 = 0.0
    sum_XY = 0.0
    tabel2_data = []

    for i in range(n_data):
        X = data_L[i]
        Y = tabel1_data[i][2] # Mengambil T2 dari modul sebelumnya
        
        X2 = round(X ** 2, 3)
        XY = round(X * Y, 3)
        
        sum_X = round(sum_X + X, 3)
        sum_Y = round(sum_Y + Y, 3)
        sum_X2 = round(sum_X2 + X2, 3)
        sum_XY = round(sum_XY + XY, 3)
        
        tabel2_data.append([X, Y, X2, XY])
        
        print(f"Data {i+1}: X={X}, Y={Y} | X²={X2:.3f}, XY={XY:.3f}")

    print("\n" + "-" * 55)
    print(f"| {'No':<2} | {'l (cm)':<8} | {'T² (dt²)':<10} | {'l²':<8} | {'l . T²':<10} |")
    print("-" * 55)
    for i, row in enumerate(tabel2_data):
        print(f"| {i+1:<2} | {row[0]:<8.3f} | {row[1]:<10.3f} | {row[2]:<8.3f} | {row[3]:<10.3f} |")
    print("-" * 55)
    print(f"| {'N=' + str(n_data):<2} | Σ={sum_X:<6.3f} | Σ={sum_Y:<8.3f} | Σ={sum_X2:<6.3f} | Σ={sum_XY:<8.3f} |")
    print("-" * 55)

    # Perhitungan a dan b
    n_kali_sum_X2 = round(n_data * sum_X2, 3)
    kuadrat_sum_X = round(sum_X ** 2, 3)
    penyebut_ab = round(n_kali_sum_X2 - kuadrat_sum_X, 3)

    a_term1 = round(sum_X2 * sum_Y, 3)
    a_term2 = round(sum_X * sum_XY, 3)
    a_pembilang = round(a_term1 - a_term2, 3)
    a = round(a_pembilang / penyebut_ab, 3)

    b_term1 = round(n_data * sum_XY, 3)
    b_term2 = round(sum_X * sum_Y, 3)
    b_pembilang = round(b_term1 - b_term2, 3)
    b = round(b_pembilang / penyebut_ab, 3) # Gradien b di-expand ke 5 desimal untuk presisi J

    print(f"\na = (ΣX²ΣY - ΣXΣXY) / (NΣX² - (ΣX)²) = {a_pembilang} / {penyebut_ab} = {a:.3f}")
    print(f"b = (NΣXY - ΣXΣY) / (NΣX² - (ΣX)²) = {b_pembilang} / {penyebut_ab} = {b:.5f}")
    print(f"\nPersamaan garis: T² = {b:.5f} l + ({a:.3f})")

    # Menghitung g perc
    g_perc = round(empat_pi2 / b, 3)
    selisih_lit2 = round(abs(g_perc - g_lit), 3)
    kesalahan_literatur2 = round((selisih_lit2 / g_lit) * 100.0, 3)

    print(f"\ng = 4π² / b = {empat_pi2} / {b:.5f} = {g_perc:.3f} cm/dt²")
    print(f"Kesalahan literatur = |(g_perc - g_Lit) / g_Lit| x 100% = {kesalahan_literatur2:.3f} %\n")

    # ---------------------------------------------------------
    # MODUL 3: Tabel Perbandingan
    # ---------------------------------------------------------
    print("3. Bandingkan hasil yang diperoleh dari no.1 dan no.2.")
    print("-" * 65)
    print(f"| {'':<15} | {'Metode Matematis':<20} | {'Kwadrat terkecil':<20} |")
    print(f"| {'':<15} | {'30°':<20} | {'30°':<20} |")
    print("-" * 65)
    print(f"| {'g (cm/dt²)':<15} | {g_bar:<20.3f} | {g_perc:<20.3f} |")
    print(f"| {'Kes.lit (%)':<15} | {kesalahan_literatur1:<20.3f} | {kesalahan_literatur2:<20.3f} |")
    print("-" * 65)

    # ---------------------------------------------------------
    # Output Teks Template
    # ---------------------------------------------------------
    print("\n" + "="*75)
    print("4. Analisa Percobaan:")
    print("   [Ulas anomali pada data ke-10 (L=63) yang merusak nilai g menjadi >1000.")
    print("    Ini adalah bukti empiris bahwa akurasi metode ini sangat bergantung")
    print("    pada presisi human-timing dan stabilitas lintasan bandul.]")
    print("\n5. Kesimpulan dan Saran")
    print("   Kesimpulan:")
    print("   [Metode matematis dan kuadrat terkecil menghasilkan perbedaan akurasi.")
    print("    Kuadrat terkecil mendistribusikan error sehingga lebih stabil.]")
    print("   Saran:")
    print("   [Gunakan photogate sensor alih-alih stopwatch manual untuk Lanjutannya.]")
    print("="*75)

# Eksekusi
generate_laporan_m1()