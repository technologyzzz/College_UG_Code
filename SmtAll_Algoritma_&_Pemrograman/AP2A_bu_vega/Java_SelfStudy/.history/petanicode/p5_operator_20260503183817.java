package petanicode;

public class p5_operator {
    public static void main(String[] args) {
        
    //  PENUGASAN
        int a;
        int b;

        // Pengisian nilai
        a = 5;
        b = 10;

        // penambahan
        b += a;
        // sekarang b = 15
        System.out.println("Penambahan : " + b);

        // pengurangan
        b -= a;
        // sekarang b = 10 (karena 15-5)
        System.out.println("Pengurangan : " + b);

        // perkalian
        b *= a;
        // sekarang b = 50 (karena 10*5)
        System.out.println("Perkalian : " + b);

        // Pembagian
        b /= a;
        // sekarang b=10
        System.out.println("Pembagian : " + b);

        // Sisa bagi
        b %= a;
        // sekarang b=0
        System.out.println("Sisa Bagi: " + b);



    //PERBANDINGAN 
        int nilaiA = 12;
        int nilaiB = 4;
        boolean hasil;

        // apakah A lebih besar dari B?
        hasil = nilaiA > nilaiB;
        System.out.println(hasil);

        // apakah A lebih kecil dari B?
        hasil = nilaiA < nilaiB;
        System.out.println(hasil);

        // apakah A lebih besar sama dengan B?
        hasil = nilaiA >= nilaiB;
        System.out.println(hasil);

        // apakah A lebih kecil sama dengan B?
        hasil = nilaiA <= nilaiB;
        System.out.println(hasil);

        // apakah nilai A sama dengan B?
        hasil = nilaiA == nilaiB;
        System.out.println(hasil);

        // apakah nilai A tidak sama dengan B?
        hasil = nilaiA != nilaiB;
        System.out.println(hasil);



    //LOGIKA

        boolean t = true ;
        boolean f = false;
        boolean c;

        // and (konjungsi)
        c = t && f ;
        System.out.println("true && false = " + c);

        // or (disjungsi)
        c = t || f ;
        System.out.println("true || false = " + c);

        // not (negasi)
        System.out.println("negasi !true = " + !t);
    

    //BITWISE
        int Ba = 60;    /* 60 = 0011 1100 */
        int Bb = 13;    /* 13 = 0000 1101 */
        int Bc = 0;

        Bc = Ba & Bb;       /* 12 = 0000 1100 */
        System.out.println("Ba & Bb = " + Bc);

        Bc = Ba | Bb;       /* 61 = 0011 1101 */
        System.out.println("Ba | Bb = " + Bc);

        Bc = Ba ^ Bb;       /* 49 = 0011 0001 */
        System.out.println("Ba ^ Bb = " + Bc);

        Bc = ~Ba;          /*-61 = 1100 0011 */
        System.out.println("~Ba = " + Bc);

        Bc = Ba << 2;     /* 240 = 1111 0000 */
        System.out.println("Ba << 2 = " + Bc);

        Bc = Ba >> 2;     /* 215 = 1111 */
        System.out.println("Ba >> 2  = " + Bc);

        Bc = Ba >>> 2;     /* 215 = 0000 1111 */
        System.out.println("Ba >>> 2 = " + Bc);


    //TERNARY
        boolean suka = true;
        String jawaban;

        // menggunakan operator ternary
        jawaban = suka ? "iya" : "tidak";

        // menampilkan jawaban
        System.out.println(jawaban);
    
    }
}
