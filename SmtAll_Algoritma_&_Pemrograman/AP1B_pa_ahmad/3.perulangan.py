"""
# Loop Structures in Python - For
# The for statement in Python has its own unique characteristics compared to other programming languages.
# It doesn't just repeat the numbers of an arithmetic expression, or provide flexibility in defining loop iterations and terminating the loop under certain conditions.
# In Python, the for statement works by looping over various sequential data types such as Lists, Strings, and Tuples.
for i in [5, 4, 3, 2, 1]:
    print(i)

for x in range(6):
    print(x)
else:
    print("Finally Finished")
    
#tipe data tuple - looping iterasi perulangan
T = [(1,2), (3,4), (5,6)]
for (a,b) in T:
    print(a,b)
    
nama = ['budi', 'andi', 'rudi', 'sandi']
usia = [20, 18, 22, 19]
for i in range(len(nama)):
    print(nama[i], 'berusia', usia[i], 'tahun.')


    
# Loop Structures in Python - While
# The while statement in Python is the most commonly used statement for iteration.
# The simple concept of the while statement is that it will repeat the execution of statements within the while block as long as the condition is true.
# It will exit or stop executing the statement block if the condition is false.
x = "Gunadarma"
while x:
    print(x)
    x=x[1:]

a = 0; b = 10
while a < b :
    print (a)
    a = a + 1

# Loop Structures in Python - Break
# The break command is used to stop the iteration process in a for or while statement.
# The statement below the break statement will not be executed, and the program will exit the loop.
xb = int(input("Angka berapapun <10 maka akan menghitung dari angka tsb lalu break di 6"))
while xb < 10:
    if xb == 6:
        break
    print(xb)
    xb = xb + 1
else:
    print("Loop sdh selesai dikerjakan")

xbb = int(input("Angka dibawah 12 akan menghitung dari 0 sampai 6"))
for xbb in range(12):
    if xbb == 6: break
    print(xbb)
else:
    print("Finally finished!")


# Loop Structure in Python - Continue
# The continue statement causes the program flow to return to the looping statement. 
# So, if a loop contains a continue statement, the program will return to the looping statement for the next iteration.

n = 10 #dari bilangan n terus mengulang -1 untuk print bilangan yang habis dibagi 2 atau bilangan genap
while n:
    n = n - 1
    if n % 2 != 0:
        continue 
    print(n)

# Loop Structures in Python - Pass
# The pass statement causes the program to perform no action.
# The pass statement is typically used to ignore a block of loop statements, conditionals, classes, and functions that have not yet been defined in the program body to avoid errors during compilation.
while True:
    pass

# Nested Loop Structure
# A loop within another loop is called a nested loop. Nested loops can use for or while statements, or a combination of both.
# Range diartikan sebagai deret dan selalu memulai iterasi dari 0
for i in range(1,4): # loop luar
    for j in range(11,14): #loop dalam - akan di eksekusi terlebih dahulu - 
        print(i,j)


# Memasukkan 3 bilangan, mengecek ganjil/genap dan positif/negatif.
for i in range(3):
    bilangan = int(input(f"Bilangan {i+1}: "))

    if bilangan % 2 == 0:
        status_ganjil_genap = "genap"
    else:
        status_ganjil_genap = "ganjil"

    if bilangan > 0:
        status_positif_negatif = "positif"
    elif bilangan < 0:
        status_positif_negatif = "negatif"
    else:
        status_positif_negatif = "bukan positif/negatif"
     
    print(f"{bilangan} adalah {status_ganjil_genap} dan {status_positif_negatif}")


# Buatlah program menampilkan tabel perkalian 7 (1 × 7 sampai 10 × 7)
for i in range(1, 11):
    num = 7
    final_num = i * num
    print(f"{i} x {num} = {final_num}")

for i in range(1, 11):
    print(f"{i} x 7 = {i*7}")


# Buat program permainan sederhana: komputer memilih angka rahasia antara 1–10, pemain harus menebak hingga benar,
import random
angka_rahasia = random.randint(1,10)
num = int(input("Tebak angka (1-10) :"))

while num != angka_rahasia:
    print("Salah, coba lagi!")
    num = int(input("Tebak angka (1-10) :"))
    
print("Selamat, tebakan Anda benar!")


# Buatlah program menggunakan nested loop untuk menampilkan tabel perkalian 1 sampai 5.
for ol in range(1, 6):
    for il in range(1, 6):
        print(ol * il, end=" ")
    print()
"""

# Buatlah program menggunakan python dengan ketentuan : bilangan dimasukkan melalui keyboard dan dapat berulang berkali-kali untuk memasukkan banyak baris serta mencetak dengan format output sebagai berikut:

while True:
    n = int(input("Masukkan banyak baris : "))    

    for baris in range(n, 0, -1):
        for kolom in range(1, baris+1):
            print(kolom, end=" ")
        print()