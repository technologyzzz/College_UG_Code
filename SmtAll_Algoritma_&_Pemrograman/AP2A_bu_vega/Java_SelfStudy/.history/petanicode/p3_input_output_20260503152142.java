package petanicode;

import java.util.Scanner;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p3_input_output {
    public static void main(String[] args) throws IOException {
    
    //DATA KARYAWAN    
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

    
        
    //YOUR KAMU

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
    }
}