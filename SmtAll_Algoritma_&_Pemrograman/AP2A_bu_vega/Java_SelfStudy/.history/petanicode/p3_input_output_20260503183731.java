package petanicode;

import java.util.Scanner; // 1

import java.io.BufferedReader; // 2
import java.io.IOException;
import java.io.InputStreamReader;

import java.io.Console; // 3

public class p3_input_output {
    public static void main(String[] args) throws IOException {

// INPUT
    //DATA KARYAWAN - SCANNER    
         // deklarasi variabel
        String nama, alamat;
        int usia, gaji;

        // membuat scanner baru
        Scanner data = new Scanner(System.in);

        // Tampilkan output ke user
        System.out.println("### Pendataan Karyawan PT. Petani Kode ###");
        
        // menggunakan scanner dan menyimpan apa yang diketik di variabel nama
        System.out.print("Nama karyawan: ");
        nama = data.nextLine();
        // Tampilkan output lagi
        System.out.print("Alamat: ");
        // menggunakan scanner lagi
        alamat = data.nextLine();

        System.out.print("Usia: ");
        usia = data.nextInt();

        System.out.print("Gaji: ");
        gaji = data.nextInt();

        // Menampilkan apa yang sudah simpan di variabel
        System.out.println("--------------------");
        System.out.println("Nama Karyawan: " + nama);
        System.out.println("Alamat: " + alamat);
        System.out.println("Usia: " + usia + " tahun");
        System.out.println("Gaji: Rp " + gaji);

    
        
    //YOUR NAME - BUFFERED READER
        String name;

        // Membuat objek inputstream
        InputStreamReader isr = new InputStreamReader(System.in);

        // membuat objek bufferreader
        BufferedReader br = new BufferedReader(isr);

        // Mengisi variabel nama dengan Bufferreader
        System.out.print("What is your name? : ");
        name = br.readLine();

        // tampilkan output isi variabel nama
        System.out.println("So, your name is " + name + "😏"); 
        

        
    //NAMA USIA - INPUT CONSOLE
        String namaC;
        int usiaC;

        // membuat objek console
        Console con = System.console();

        // mengisi variabel nama dan usia dengan console
        System.out.print("Inputkan nama: ");
        namaC = con.readLine();
        System.out.print("Inputkan usia: ");
        usiaC = Integer.parseInt(con.readLine());

        // menampilkan isi variabel nama dan usia
        System.out.println("Nama kamu adalah: " + namaC);
        System.out.println("Saat ini berusia " + usiaC + " tahun");

// OUTPUT
    // PRINT VS PRINTLN 
        System.out.print("ini teks yang dicetak dengan print()");
        System.out.println("sedangkan ini teks yang dicetak dengan println()"); // bersambung dengan line sebelumnya
        System.out.print("pakai print() lagi"); // line baru
    
    // MENGGABUNGKAN STRING MANUAL   
        String namaDepan = "Maulana";
        String namaBelakang = "Abdul";

        System.out.print(namaDepan);
        System.out.print(namaBelakang);

        System.out.print(namaDepan + " " + namaBelakang + "Aziz");

    // MENGGABUNGKAN STRING KOMPLEKS DENGAN FORMAT ()
        String namaDepanF = "Petani";
        String namaBelakangF = "Kode";

        System.out.format("Nama saya %s %s %n", namaDepanF, namaBelakangF);
        // s untuk string, d untuk desimal angka, f untuk pecahan, n dan /n untuk baris baru    
    }
}