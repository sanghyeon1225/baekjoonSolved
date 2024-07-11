import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = b + c;
        b = d % 60;
        a = a + (d / 60);
        if (a >= 24)
            a -= 24;
        
        System.out.println(a + " " + b);
            
    }
}