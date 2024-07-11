import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int tot = sc.nextInt();
        int time = sc.nextInt();
        int sum = 0;
        for(int i = 0; i < time; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            sum += (a*b);
        }
       if(tot == sum)
           System.out.println("Yes");
        else
           System.out.println("No");
    }
}