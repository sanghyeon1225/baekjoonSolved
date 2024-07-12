import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        for(int i = 0; i < a; i++){
            int b = s.nextInt();
            int c = s.nextInt();
            int d = b + c;
            System.out.println("Case #" + (i+1) + ": " + d);
        }
    }
}