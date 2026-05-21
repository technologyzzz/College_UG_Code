import pandas as pd
import numpy as np

class WealthForecaster:
    def __init__(self, excel_path):
        self.file_path = excel_path
        
        self.data = None
        self.total_modal_awal = 0

    def load_data(self):
        # [Pandas] Load data & Pre-processing
        self.data = pd.read_excel(self.file_path)
        
        # Agregasi Data
        self.total_modal_awal = self.data['ModalInvestasi'].sum()
        self.data['Total_Return_Rate'] = self.data['AvgGrowth'] + self.data['AvgDividend']

    def predict(self):
        # [NumPy] Calculation Engine
        if self.data is None: return

        target_years = np.array([3, 5, 10]) 
        
        # Persiapan Matrix (Broadcasting)
        principals = self.data['ModalInvestasi'].values[:, np.newaxis] 
        rates = self.data['Total_Return_Rate'].values[:, np.newaxis]
        timeline = target_years[np.newaxis, :]
        
        # Rumus Compound Interest: P * (1+r)^t
        growth_matrix = principals * ((1 + rates) ** timeline)
        
        # Penjumlahan Vertikal (Axis 0) untuk Total Portofolio
        total_assets_per_target = np.sum(growth_matrix, axis=0)

        self._display_output(target_years, total_assets_per_target)

    def _display_output(self, years, assets):
        # [Output] Menampilkan laporan sesuai format final
        print("\n" + "="*50)
        print("📊 LAPORAN PREDIKSI KEKAYAAN (The Wealth Forecaster)")
        print("="*50)
        
        # Rincian Modal Awal
        print("\n💼 [RINCIAN MODAL AWAL]")
        print("-" * 50)
        print(f"{'KODE SAHAM':<12} | {'MODAL (IDR)':<20} | {'PORSI (%)':<10}")
        print("-" * 50)
        
        for index, row in self.data.iterrows():
            porsi_persen = (row['ModalInvestasi'] / self.total_modal_awal) * 100
            print(f"{row['KodeSaham']:<12} | Rp {row['ModalInvestasi']:,.0f}       | {porsi_persen:.1f}%")
            
        print("-" * 50)
        print(f"💰 TOTAL MODAL : Rp {self.total_modal_awal:,.0f} (100%)")
        print("=" * 50)
        
        # Rincian Prediksi
        print("\n🔮 [PROYEKSI MASA DEPAN]")
        for year, asset_val in zip(years, assets):
            growth_pct = ((asset_val - self.total_modal_awal) / self.total_modal_awal) * 100
            profit_rp = asset_val - self.total_modal_awal
            
            print("-" * 50)
            print(f"🕒 DALAM {year} TAHUN:")
            print(f"   Total Aset   : Rp {asset_val:,.0f}")
            print(f"   Profit (Rp)  : Rp {profit_rp:,.0f}")
            print(f"   Growth (%)   : +{growth_pct:.2f}%")
            
        print("=" * 50)

# --- EKSEKUSI ---
# Pastikan 'portfolio.xlsx' ada di folder yang sama saat menjalankan terminal!
app = WealthForecaster("portfolio.xlsx")
app.load_data()
app.predict()