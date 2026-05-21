package petanicode;

import java.util.Scanner;

public class p6_perulangan {
    public static void main(String[] args) {
    
    // ULANG "Maul" 10x    
        for (int hitungan = 0; hitungan <= 10; hitungan++) {
        System.out.println("Maul");
        }
    //COUNTED LOOP
        // FOR & FOR EACH
    //UNCOUNTED LOOP
        // WHILE & DOWHILE

    // ULANG 1-10
        for(int i=0; i <= 10; i++){
            System.out.print( i + " " );
        }
    // ULANG GANJIL    
        for (int i=1; i <= 20; i += 2) {
            System.out.print( i + " ");
        }
    
    // ARRAY
        int angka[] = {3,1,42,24,12};

        // menggunakan perulangan For each untuk menampilkan angka
        for( int x : angka ){
            System.out.print(x + " ");
        }

    // CUM
    System.out.println("=== Program loop menghitung berapa kali cum ===");
        // var & scanner
        Boolean running = true;
        int counter = 0 ;
        String jawab;
        Scanner sc = new Scanner (System.in);

        while (running) {
            //input
            System.out.println("Apakah anda sudah cum (ahhh/belom)? : ");
            jawab = sc.nextLine();
            //process
            if (jawab.equalsIgnoreCase("ahh")) {
                running = true;
            } 
            counter++;
        }    
        //output
        System.out.println("Anda sudah cum sebanyak " + counter + " kali, waaaw...");

    }
}
