import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int input = s.nextInt();
        for(int i = 0; i < input; i++){
            for(int j = 0; j < i+1; j++){
                System.out.print("*");
            }
            System.out.println("");   
        }
    }
}