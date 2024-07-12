import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String s1 = s.nextLine();
        int a = s.nextInt() - 1;
        System.out.println(s1.charAt(a));
    }
}