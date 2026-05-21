package petanicode;

public class p4_operator {
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
    
    }
}
