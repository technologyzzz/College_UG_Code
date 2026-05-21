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
        System.out.print("Nama : ");
        nama = scaN.nextLine();
        System.out.print("Nilai : ");
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

        if (kartu.equals("yes")) { //punya kartu member
            System.out.print("Berapa rupiah anda belanja? : ");
            belanjaM = scanK.nextInt();

            if (belanjaM > 5000000) {
                System.out.println("Selamat anda mendapat diskon Rp 50.000");
                diskon = 50000;
            } else if (belanjaM > 100000) {
                System.out.println("Selamat anda mendapat diskon Rp 15.000");
                diskon = 15000;
            } else {
                System.out.println("Maaf anda tidak mendapat diskon");
            }        
        

        } else if (kartu.equals("no")) {  //tidak punya kartu member
            System.out.print("Berapa rupiah anda belanja? : ");
            belanjaM = scanK.nextInt();

            if (belanja > 100000) {
                System.out.println("Selamat anda mendapat diskon Rp 5.000");
                diskon = 5000;
            } else {
                System.out.println("Maaf anda tidak mendapat diskon");
            }
            
        } else {
            System.out.println("Anda tidak menginput yes/no");
            diskon = 0;
        }

        //process diskon
        bayar = belanjaM - diskon;
        System.out.println("Belanjaan yang harus anda bayar adalah : " + bayar);


    //DIKON KARTU MEMBER - NESTED (ringkas petanicode) 
    System.out.println("=== Program diskon kartu member ===");
    

        // deklarasi variabel dan Scanner
        int sbelanjaan, sdiskon, sbayar;
        String skartu;
        Scanner sscan = new Scanner(System.in);

        // mengambil input
        System.out.print("Apakah ada kartu member: ");
        skartu = sscan.nextLine();
        System.out.print("Total belanjaan: ");
        sbelanjaan = sscan.nextInt();

        // proses
        if (skartu.equalsIgnoreCase("ya")) {
            if (sbelanjaan > 500000) {
                sdiskon = 50000;
            } else if (sbelanjaan > 100000) {
                sdiskon = 15000;
            } else {
                sdiskon = 0;
            }

        } else {
            if (sbelanjaan > 100000) {
                sdiskon = 5000;
            } else {
                sdiskon = 0;
            }
        }

        // total yang harus dibayar
        sbayar = sbelanjaan - sdiskon;

        // output
        System.out.println("Total Bayar: Rp " + sbayar);
    

    //TILANG POLISI PRINT
    System.out.println("=== Program razia tilang adanya SIM dan STNK");
        //var and scanner
        String sim, stnk;
        Scanner razia = new Scanner(System.in);

        //input
        System.out.println("Apakah anda punya SIM?(yes/no) : ");
        sim = razia.nextLine();
        
        //process
        if (sim.equals("yes")) {
            System.out.println("Apakah anda punya STNK(yes/no) : ");
            stnk = razia.nextLine();
                
            if (stnk.equals("yes")) { 
                //output
                System.out.println("Ok benar anda memiliki SIM dan STNK, anda boleh melanjutkan perjalanan");

            } else {
                //output
                System.out.println("Anda ditilang karena berkendara tanpa membawa STNK padahal anda memiliki SIM");
            }
        
        } else {
            //output
            System.out.println("Anda ditilang karena berkendara tanpa memiliki SIM");
        }

    //TILANG DENGAN NESTED
        boolean SIMN = false;
        boolean STNKN = true;

        // cek apakah dia akan ditilang atau tidak
        if(SIMN == true){
            if( STNKN == true ) {
                System.out.println("Tidak ditilang!");
            }
        } else {
            System.out.println("Anda ditilang!");

    //TILANG WITH LOGIC OPERATOR
        boolean SIML = false;
        boolean STNKL = true;

        // cek apakah dia akan ditilang atau tidak
        if(SIML == true && STNKL == true){
            System.out.println("Tidak ditilang!");
        } else {
            System.out.println("Anda ditilang!");
        }    

    }
}
