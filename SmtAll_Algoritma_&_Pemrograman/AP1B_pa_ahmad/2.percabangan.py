"""
# Branching in Python - if
# The if statement is used to perform selection. If a condition is true, the program will execute the statement below it.
# In Python, the condition and statement are separated by a colon ( : ).
nama = "python"

if nama == "python"
    print("Hello" + nama)


# Branching in Python - If Else
# The if–else statement is used to select a condition. If the condition is true, the program will execute statement 1.
# However, if the condition is false, statement 2 will be executed.
kunci = "python"
password = input("Masukkan Password")

if password == kunci:
    print("Password Benar")
else:
    print("Password Salah")


# Branching in Python - If Elif Else
# The if-else-elif statement is used to select conditions when more than one condition is given or when multiple conditions are present.
# If the first condition is true, select the second condition, and so on.
angka = input("Masukkan sebuah bilangan:")

if angka > 0:
    print("Angka merupakan Bilangan Positif")
    elif angka < 0:
    print("Angka merupakan Bilangan Negatif")
else :
    print("Angka merupakan 0")
  
  
# Branching in Python - Nested If Statements
# A nested condition is a condition within a condition.
# If there are two conditional branches, one of the conditional branches can also contain a specific condition.

#input number positive/negative)
angka =int(input("Masukkan sebuah bilangan: "))

if angka > 0:
    print("Angka merupakan bilangan positif")
elif angka < 0: 
    print("Angka merupakan bilangan negatif")
else:
    print("Angka Nol")


if x==y:
    print(x,y "mempunyai nilai yang sama")
else :
    if x > y:
        print(x, "lebih besar dari", y)
    if x < y:
        print(x, "lebih kecil dari", y)

#input number 0-10 for difinition
x = int(input("Masukkan sebuah bilangan: "))
# if 1
if 0 < x : 
    if x < 10:
        print(x, "bil. positif terdiri dari satu digit")

# if 2        
if 0 < x and x < 10:
        print(x, "bil. positif terdiri dari satu digit")

# if 3
if 0 < x < 10:
        print(x, "bil. positif terdiri dari satu digit")


# Latihan percabangan
# Buatlah program percabangan untuk membedakan angka yang diinput termasuk bilangan ganjil atau bilangan genap


# Tugas 
1. Buatlah program menggunakan Python untuk mencetak bilangan ganjil atau genap dengan ketentuan sebagai berikut :
a. Masukkan bilangan melalui keyboard 
b. Jika bilangan yang dimasukkan adalah 0 maka literal yang tercetak adalah “ 0 bukan bilangan ganjil atau genap” 
c. Jika bilangan yang dimasukkan ganjil atau genap maka cetak bilangannya dan keterangan ganjil atau genap

i = int(input("Input angka"))

if i % 2 == 0 :
    if i != 0 : 
        print(i, "adalah bilangan genap.")
    else :
        print(i, "bukan bilangan ganjil atau genap")
else:
    print(i, "adalah bilangan ganjil.")
    
# Tugas 2  
Buatlah program menggunakan bahasa Python dengan ketentuan sebagai berikut: 
a. Masukkan nanma, npm, kelas, mata kuliah, nilai uts dan nilai ujian utama  melalui keyboard
b. Terdapat proses perhitungan dengan rumus : Nilai total = 50 % uts + 50 % ujian utama 
c. Pada nilai total hasil proses perhitungan akan menghasilkan grade sebagai berikut : 
 1.86 – 100 : A
 2.71 – 85 : B
 3.61 – 70 : C
 4.<= 60 : D 
d. Cetak nama, npm, kelas, mata kuliah, total dan grade pada layar output !

nama = input("masukkan nama : ")
kelas = input("masukkan kelas : ")
matkul = input("masukkan matkul : ")
npm = input("masukkan npm : ")
uts = int(input("masukkan nilai uts : "))
ujian_utama = int(input("masukkan nilai ujian utama : "))

# Meminta pengguna untuk memasukkan sebuah bilangan
angka = int(input("Masukkan sebuah bilangan bulat: "))

if angka == 0:
    print(f"Bilangan {angka} adalah bilangan NOL.")
elif angka % 2 == 0:
    print(f"Bilangan {angka} adalah bilangan GENAP.")
else:
    print(f"Bilangan {angka} adalah bilangan GANJIL.")
"""

# Tugas 2
"""
Buatlah program menggunakan bahasa Python dengan ketentuan sebagai berikut: 
a. Masukkan nanma, npm, kelas, mata kuliah, nilai uts dan nilai ujian utama  melalui keyboard
b. Terdapat proses perhitungan dengan rumus : Nilai total = 50 % uts + 50 % ujian utama 
c. Pada nilai total hasil proses perhitungan akan menghasilkan grade sebagai berikut : 
 1.86 - 100 : A
 2.71 - 85 : B
 3.61 - 70 : C
 4.<= 60 : D 
d. Cetak nama, npm, kelas, mata kuliah, total dan grade pada layar output 
"""
name = input("Masukan Nama : ")
npm = input("Masukan NPM : ")
kelas = input("Masukan Kelas : ")
matkul = input("Masukan Mata Kuliah : ")
uts = int(input("Masukan Nilai UTS : "))
ua = int(input("Masukan Nilai Ujian Utama : "))
total_score = (0.5 *uts) + (0.5 * ua)

if total_score < 100 :
    if total_score >= 86:
        grade = 'A'
    elif total_score >= 71:
        grade = 'B'
    elif total_score >= 61:
        grade = 'C'
    else:
        grade = 'D'
else:
    print("Angka tidak valid. Input angka 0-100")

print(f"Nama : {name}, Kelas : {kelas}, Matkul : {matkul}, Total : {total_score}, Grade : {grade}")
    
  