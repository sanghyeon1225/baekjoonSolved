import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int result = 0;
        for(int i = 0; i < a; i++){
            result += (i+1);
        }
        System.out.println(result);
    }
}