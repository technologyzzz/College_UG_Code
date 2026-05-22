## IMPORT
import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit
)

### Membuat aplikasi
app = QApplication(sys.argv)

### Membuat window
window = QWidget()
window.setWindowTitle("Biodata Mahasiswa")
window.setGeometry(100, 100, 400, 300)

### Warna background
window.setStyleSheet("background-color: skyblue;")

### HEADER
header = QLabel("FORM BIODATA MAHASISWA", window)
header.move(90, 20)

### Mengatur ukuran tulisan
header.setStyleSheet("""
    font-size: 16px;
    font-weight: bold;
""")

### INPUT NAMA
label_nama = QLabel("Nama :", window)
label_nama.move(50, 80)

input_nama = QLineEdit(window)
input_nama.move(130, 80)


### INPUT NPM
label_npm = QLabel("NPM :", window)
label_npm.move(50, 120)

input_npm = QLineEdit(window)
input_npm.move(130, 120)

### INPUT KELAS
label_kelas = QLabel("Kelas :", window)
label_kelas.move(50, 160)

input_kelas = QLineEdit(window)
input_kelas.move(130, 160)

# HASIL
hasil = QLabel("", window)
hasil.move(50 , 240)

# Function Tombol
def tampilkan_data():
    hasil.setText(
        f"Nama : {input_nama.text()}\n"
        f"NPM : {input_npm.text()}\n"
        f"Kelas : {input_kelas.text()}"
    )

    hasil.adjustSize()

# BUTTON
button = QPushButton("Tampilkan", window)
button.move(140, 200)

button.clicked.connect(tampilkan_data)

# Menampilkan window
window.show()

# Menjalankan aplikasi
sys.exit(app.exec_())