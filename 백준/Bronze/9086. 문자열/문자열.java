import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        for(int i = 0; i < a; i++){
            String s1 = s.next();
            System.out.println(s1.substring(0, 1) + s1.substring(s1.length()-1, s1.length()));
        }
        
    }
}