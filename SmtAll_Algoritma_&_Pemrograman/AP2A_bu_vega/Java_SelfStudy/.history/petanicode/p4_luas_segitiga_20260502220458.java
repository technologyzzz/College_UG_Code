package petanicode;

import java.util.Scanner;

public class p4_luas_segitiga {
    
    public static void main(String args[]){
        // deklarasi var
        Double luas;
        int alas, tinggi;

        //membuat inisiasi scanner baru
        Scanner baca = new Scanner(System.in);

        //Input
        System.out.println("== Program hitung luas Segitiga ==");

        System.out.print("Input alas : ");
        alas = baca.nextInt();

        System.out.print("Input tinggi: ");
        tinggi = baca.nextInt();

        //proses
        luas = Double.valueOf((alas*tinggi)/2);

        //output
        System.out.println("Luas = " + luas);
    }
}
