
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int time = sc.nextInt();
        for(int i = 0 ; i < time ; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            long result = 1;
            
            for(int j = 0; j < a; j++){
                result *= (b-j);
                result /= (j+1);
            }
            
            System.out.println(result);
        }
    }
}