import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        for(int i = 0; i < num ; i++){
            for(int j = num - 1; i < j; j--){
                System.out.print(" ");
            }
            for(int k = 0; k < 2 * i + 1; k++){
                System.out.print("*");
            }
            System.out.println("");
        }
        for(int i = 1; i < num; i++){
            for(int j = 0; j < i; j++){
                System.out.print(" ");
            }
            for(int k = 0; k < 2 * num - (2 * i + 1); k++){
                System.out.print("*");
            }
            System.out.println("");
        }
    }
}