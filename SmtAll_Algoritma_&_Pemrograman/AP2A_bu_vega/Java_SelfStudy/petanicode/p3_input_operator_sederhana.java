package petanicode;

import java.util.Scanner;

public class p3_input_operator_sederhana {
    public static void main(String args[]){
        
    //LUAS LINGKARAN
        //deklarasi var
        Double luasr, pi;
        int r;

        //var input
        pi = 3.14;
        r = 14;

        //var proses
        luasr = pi * r * r;

        //output
        System.out.print("Luas lingkaran adalah : " );
        System.out.println(luasr);


    //LUAS SEGITIGA - INPUT
        // deklarasi var
        Double luass;
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
        luass = Double.valueOf((alas * tinggi)/2);

        //output
        System.out.println("Luas = " + luass);
    


    //KELILING PERSEGI PANJANG
        //deklarasi var
        double kll, p, l ;
        
        //input
        p = 6.0;
        l = 3.0;

        //proses
        kll = (2*p) + (2*l);

        //output
        System.out.println(kll);
    }
}