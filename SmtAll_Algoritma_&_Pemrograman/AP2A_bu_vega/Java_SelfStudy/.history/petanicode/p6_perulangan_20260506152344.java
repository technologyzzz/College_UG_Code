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

//FOR
    // ULANG 1-10
        for(int i=0; i <= 10; i++){
            System.out.println( i + " " );
        }
    // ULANG GANJIL    
        for (int i=1; i <= 20; i += 2) {
            System.out.println( i + " ");
        }
    
    // ARRAY
        int angka[] = {3,1,42,24,12};

        // menggunakan perulangan For each untuk menampilkan angka
        for( int x : angka ){
            System.out.println(x + " ");
        }
//WHILE
    // CUM
    System.out.println("=== Program loop menghitung berapa kali melamar pekerjaan ===");
        // var & scanner
        Boolean running = true;
        int counter = 0 ;
        String jawab;
        Scanner sc = new Scanner (System.in);

        while (running) {
            //input
            System.out.print("Apakah anda sudah mendapat pekerjaan? (masih melamar/sudah) : ");
            jawab = sc.nextLine();
            //process
            if (jawab.equalsIgnoreCase("sudah")) {
                running = false;
            } 
            counter++;
        }    
        //output
        System.out.println("Anda sudah melamar pekerjaan sebanyak " + counter + " kali, stress yaaah? ^_^");

    //COUNTED LOOP DI DALAM UNCOUNTED LOOP (seperti pada pekerjaan sebelumnya)
        int ip = 0;

        while ( ip <= 10 ){
            // blok kode yang akan diulang
            System.out.println("Perulangan ke-" + ip);

            // increment nilai ip
            ip++;
        }
//DO/WHILE
    //KERJAKAN DULU LALU CEK KONDISI (struktur lebih mudah dibaca)  
        int i = 0;

        do {
            System.out.println("perulangan ke-" + i);
            i++;
        } while ( i <= 10);

//NESTED
        //
        int x, y;

        // melakukan parulang sebnayan x dan y kali
        for (x = 0; x <= 5; x++){ //0-5 = 6 bil
            for( y = 0; y <= 3; y++){ //0-3 = 4 bil
                System.out.format("Perulangan [x=%d, y=%d] %n", x, y);
            }
    }
}
