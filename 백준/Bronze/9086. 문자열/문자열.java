import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        for(int i = 0; i < a; i++){
            String s1 = s.next();
            System.out.print(s1.charAt(0));
            System.out.println(s1.charAt(s1.length()-1));
        }
        
    }
}