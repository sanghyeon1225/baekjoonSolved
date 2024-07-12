import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int a;
        int b;
        while(true) {
            a = s.nextInt();
            b = s.nextInt();
            if (a != 0 || b != 0)
                System.out.println(a + b);
            else
                break;
        }
    }
}