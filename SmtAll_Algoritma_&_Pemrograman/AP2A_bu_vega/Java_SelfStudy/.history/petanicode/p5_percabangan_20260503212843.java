package petanicode;

import java.util.Scanner;

public class p5_percabangan {
    public static void main(String[] args) {
        
    //PROGRAM HADIAH - IF
    System.out.println("=== Program hadiah jika belanja diatas 100.000 ===");
        //var dan scanner
        int belanja = 0;
        Scanner scan = new Scanner(System.in);
        
        //input
        System.out.print("Total Belanjaan : Rp ");
        belanja = scan.nextInt();

        //branch belanja diatas 100000
        if (belanja > 10000) {
            System.out.println("Selamat, anda mendapatkan hadiah!");
        }

        System.out.println("Terima kasih...");



    //PROGRAM CEK KELULUSAN - IF/ELSE
    System.out.println("=== Program untuk mengecek kelulusan jika nilai diatas 70 ===");
    
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


    //PROGRAM HITUNG GRADE - IF/ELSE IF
    System.out.println("=== Program untuk menenetukan grade ABCD berdasarkan nilai 0-100 ===");

        //var dan scanner
        int nilaiF;
        String grade;
        Scanner scanF = new Scanner(System.in);

        //input
        System.out.print("Inputkan nilai: ");
        nilaiF = scanF.nextInt();

        //process
        if ( nilaiF >= 90 ) {
            grade = "A";
        } else if ( nilaiF >= 80 ){
            grade = "B+";
        } else if ( nilaiF >= 70 ){
            grade = "B";
        } else if ( nilaiF >= 60 ){
            grade = "C+";
        } else if ( nilaiF >= 50 ){
            grade = "C";
        } else if ( nilaiF >= 40 ){
            grade = "D";
        } else {
            grade = "E";
        }

        //output
        System.out.println("Grade: " + grade);


    //SIMULASI PERINTAH LAMPUR LALU LINTAS - SWITCH/CASE
    System.out.println("=== Program untuk menampilkan perintah untuk warna lampu lalu lintas yang diinput ===");
        
        //var dan scanner
        String lampu;
        Scanner scanL = new Scanner(System.in);
        
        //input
        System.out.print("Inputkan nama warna lampu lalu lintas : ");
        lampu = scanL.nextLine();

        //process
        switch(lampu){
            case "merah":
                System.out.println("Lampu merah, berhenti");
                break;
            case "kuning":
                System.out.println("Lampu kunging, harap hati-hati");
                break;
            case "hijau":
                System.out.println("Lampu hijau, silakan jalan!");
                break;
            default:
                System.out.println("Warna lampu salah");
        }



    //DISKON KARTU MEMBER - NESTED
    System.out.println("=== Program diskon kartu member ===");
        
        //var dan scanner
        String kartu;
        int belanjaM = 0, diskon = 0, bayar;
        Scanner scanK = new Scanner(System.in);

        //io kartu
        System.out.print("Apakah anda punya kartu? (yes/no) : ");
        kartu = scanK.nextLine();

        if (kartu == "yes") { //punya kartu member
            System.out.print("Berapa rupiah anda belanja? : ");
            belanjaM = scanK.nextInt();

            if (belanjaM > 5000000) {
                System.out.println("Selamat anda mendapat diskon Rp 50.000");
                diskon = 50000;
            } else if (belanjaM > 100000) {
                System.out.println("Selamat anda mendapat diskon Rp 15.000");
                diskon = 15000;
            } else {
                System.out.println(:"Maaf anda tidak mendapat diskon");
            }        
        

        } else if (kartu == "no") {  //tidak punya kartu member
            System.out.print("Berapa rupiah anda belanja? : ");
            belanjaM = scanK.nextInt();

            if (belanja > 100000) {
                System.out.println("Selamat anda mendapat diskon Rp 5.000");
                diskon = 5000;
            } else {
                System.out.println("Maaf anda tidak mendapat diskon");
            }
            
        } else {
            System.out.println("Anda tidak menginput yes/no")
        }

        //process diskon
        bayar = belanja - diskon;
        System.out.print("Belanjaan yang harus anda bayar adalah : " + bayar);



    }
}
