package petanicode;

import java.util.Scanner;

public class p5_percabangan {
    public static void main(String[] args) {
        
    //PROGRAM HADIAH - IF
        System.out.println("Program hadiah jika belanja diatas 100.000");
        //var dan scanner
        int belanja = 0;
        Scanner scan = new Scanner(System.in);
        
        //input
        System.out.println("Total Belanjaan : Rp ");
        belanja = scan.nextInt();

        //branch belanja diatas 100000
        if (belanja > 10000) {
            System.out.print("Selamat, anda mendapatkan hadiah!");
        }

        System.out.print("Terima kasih...");



    //PROGRAM CEK KELULUSAN - IF/ELSE
    System.out.println("Program untuk mengecek kelulusan jika nilai diatas 70");
        //var dan scanner
        int nilai;
        String nama;
        Scanner scaN = new Scanner(System.in);

        //input
        System.out.println("Nama : ");
        nama = scaN.nextLine();
        System.out.println("Nilai : ");
        nilai = scaN.nextInt();

        if (nilai > 70) {
            System.out.println("Selamat "+ nama +", anda lulus");
        } else { 
            System.out.println("Maaf "+ nama + ", anda tidak lulus");
        }
    }
}
