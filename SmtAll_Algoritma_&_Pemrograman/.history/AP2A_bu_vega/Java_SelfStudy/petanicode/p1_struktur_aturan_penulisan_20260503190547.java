package petanicode; // 1. package

// import java.util.Scanner; // 2. import

public class p1_struktur_aturan_penulisan { // 3. public class dan class dalam OOP java
    public static void main(String args[]){ // 4. public static void main string args
    
    //HELLO WORD
        System.out.println("Hello World"); // println sederhana
    
    //DATADIRI    
        //mendefinisikan tipe data variable
        String nama, alamat ;
        int usia;
        double tinggi;

        //mengisi variable
        nama = "Maulana Abdul Aziz";
        alamat = "Jl Kaja2b";
        usia = 22;
        tinggi = 169;

        //print variable dan isinya
        System.out.println("Nama: " + nama);
        System.out.println("Alamat: " + alamat);
        System.out.println("Usia: " + usia + "tahun");
        System.out.println("tinggi: " + tinggi + " cm");


    
    
    }
}

