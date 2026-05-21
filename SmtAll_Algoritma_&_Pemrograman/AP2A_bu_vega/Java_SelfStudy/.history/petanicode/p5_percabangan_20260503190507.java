package petanicode;

import java.util.Scanner;

public class p5_percabangan {
    public static void main(String[] args) {
        
    //PROGRAM HADIAH - IF
        //var dan scanner
        int belanja = 0
        Scanner scan = new Scanner(System.in);
        
        //input
        System.out.print("Total Belanjaan : Rp ")
        belanja = scan.nextInt();

        //branch belanja diatas 100000
        if (belanja > 10000) {
            System.out.print("Selamat, anda mendapatkan hadiah!");
        }

        System.out.print("Terima kasih...");
    //PROGRAM CEK KELULUSAN - IF/ELSE
        //var dan scanner
        int nilai;
        String nama;
        Scanner scaN = new Scanner(System.in);

        //input
        System.out.print("Nama : ");
        nama = scaN.nextLine();
        System.out.print("Nilai : ");
        nilai = scaN.nextInt();

        if (nilai > 70) {
            System.out.print("Selamat "+ nama +", anda lulus");
        } else { 
            System.out.print("Maaf "+ nama + ", anda tidak lulus")
        }
    }
}
